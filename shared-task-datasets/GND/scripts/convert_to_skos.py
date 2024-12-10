import json
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import SKOS, RDF, DCTERMS
from rdflib.term import _is_valid_uri


GND_NS = 'http://d-nb.info/gnd/'
GND_SC_NS = 'https://d-nb.info/standards/vocab/gnd/gnd-sc#'

def gnd_code_to_uri(code):
    return URIRef(code.replace('gnd:', GND_NS))

def sc_code_to_uri(code):
    return URIRef(GND_SC_NS + code)

def convert_to_skos_graph(json_filepath, rdf_filepath, rdf_format='turtle'):
    with open(json_filepath) as f:
        gnd_data = json.load(f)

    graph = Graph()
    graph.namespace_manager.bind('gnd', GND_NS)
    graph.namespace_manager.bind('gnd_sc', GND_SC_NS)

    # 1st pass: construct label to URI mapping
    label_to_uri = { rec['Name']: gnd_code_to_uri(rec['Code'])
                     for rec in gnd_data }

    # 2nd pass: convert each record to a SKOS Concept
    for rec in gnd_data:
        uri = gnd_code_to_uri(rec['Code'])
        graph.add((uri, RDF.type, SKOS.Concept))
        # Name / skos:prefLabel
        graph.add((uri, SKOS.prefLabel, Literal(rec['Name'], lang='de')))

        # Alternate Name / skos:altLabel
        for alt in rec['Alternate Name']:
            graph.add((uri, SKOS.altLabel, Literal(alt, lang='de')))

        # Definition / skos:definition
        if 'Definition' in rec:
            graph.add((uri, SKOS.definition, Literal(rec['Definition'], lang='de')))

        # Source URL / dcterms:source (with URI value, if URI is valid)
        if 'Source URL' in rec:
            url = rec['Source URL']
            if _is_valid_uri(url):
                graph.add((uri, DCTERMS.source, URIRef(url)))
            else:  # not a valid URL, represent it as literal instead
                graph.add((uri, DCTERMS.source, Literal(url, lang='de')))

        # Related Subjects / skos:related
        for rel in rec['Related Subjects']:
            rel_uri = label_to_uri.get(rel)
            if rel_uri:
                # related links go both ways in SKOS
                graph.add((uri, SKOS.related, rel_uri))
                graph.add((rel_uri, SKOS.related, uri))

        # Subject Categories / skos:Collection and skos:member
        sc_no = rec['Classification Number']
        sc_uri = sc_code_to_uri(sc_no)
        graph.add((sc_uri, RDF.type, SKOS.Collection))
        graph.add((sc_uri, SKOS.prefLabel, Literal(rec['Classification Name'], lang='de')))
        graph.add((sc_uri, SKOS.notation, Literal(sc_no)))
        graph.add((sc_uri, SKOS.member, uri))

    graph.serialize(rdf_filepath, format=rdf_format)


# Convert TIB Core subjects to SKOS
convert_to_skos_graph('../dataset/GND-Subjects-tib-core.json',
                      '../dataset/GND-Subjects-tib-core-skos.ttl')

# Convert all subjects to SKOS
convert_to_skos_graph('../dataset/GND-Subjects-all.json',
                      '../dataset/GND-Subjects-all-skos.ttl')
