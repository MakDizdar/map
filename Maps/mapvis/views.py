from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
from django.http import HttpResponse
import datetime
from time import sleep
from extract_nodes import extract_osm_nodes , select_nodes_in_rectangle
from extract_shortest_path import find_node, shortestPath
from extract_edges import *
from store import *


def hello(request):
    now = datetime.datetime.now() 
    html = "<html><body>Hello world!<b> It is now %s.</b> </body></html>" %now   
    return HttpResponse(html)


class Member:
     def __init__(self,name,age):
        self.name = name
        self.age = age

def memb_reg(request):
    members = dict()
    members[2] = Member("Kurt", 64)
    members[5] = Member("Anne", 39)
    members[3] = Member("Berit", 15)
    members[8] = Member("Julius_Caesar", 2113)

    c = Context({
                    'NUMBER_OF_MEMBERS': len(members),
                    'MEMBER_INFO': members,  # Important, note the last ","!
                })

    return render_to_response('mapvis/projekt_lace.html', c)
    

# Create your views here.
def mapapp(request):
    if request.method == 'GET':
        node_set=NodeSet()
        node_set = extract_osm_nodes("mapvis/osmmap.osm")
        node_set = select_nodes_in_rectangle(node_set,
                                                 58.40807, 58.40968,
                                                 15.56111, 15.56424)
        c = RequestContext(request,{'GMAPS_API_KEY': '+++YOUR_GMAPS_API_KEY+++',
                                    'COORDS': node_set.get_nodes().values(), 'DISTANCE':[] ,
                                    'PLACEDMARKER': []})
        return render_to_response('mapvis/mapapp.html', c) 

    elif request.method == 'POST':
        pparser = POST_parser(request)
        start_mrk_lat = pparser.lat1
        start_mrk_lng = pparser.lng1
        end_mrk_lat= pparser.lat2
        end_mrk_lng= pparser.lng2
        node_set = extract_osm_nodes("mapvis/osmmap.osm")
        iter_nodeset = node_set.get_nodes()
        edgeset = extract_osm_ways("mapvis/osmmap.osm")
        upt_edgeset = update_edgeset_weights(edgeset,node_set)
        graph = extract_graph_alt(upt_edgeset)        
        start_node = find_node(start_mrk_lat, start_mrk_lng, node_set)[1]
        end_node = find_node(end_mrk_lat, end_mrk_lng, node_set)[1]
        seq=[]
        errMSG= False
        try:
            dist, path =shortestPath(graph, str(int(start_node.id)), str(int(end_node.id)))
            for node in path:
                seq.append(iter_nodeset[float(node)])
        except:
            dist, path = "wut", "NOT FOUND"
            errMSG=True
            
        
            
        c = RequestContext(request, {'GMAPS_API_KEY': '+++YOUR_GMAPS_API_KEY+++','PATHNODES': seq,
                                     'DISTANCE': dist , 'START':start_node, 'BEND': end_node.lat,
                                      'LEND': end_node.lng,'FEND': end_node.id, 'errMSG': errMSG})
        return render_to_response('mapvis/mapapp.html', c)


def get_float(request, id):
    value = request.POST.get(id)
    # Check that it's possible to convert input to float.
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def get_str(request, id):
    return request.POST.get(id)


class POST_parser:
    def __init__(self, request):
        # You can choose what variables you want to
        # get from POST and what to call them.
        self.lat1 = get_float(request, 'lat1')
        self.lng1 = get_float(request, 'lng1')
        self.lat2 = get_float(request, 'lat2')
        self.lng2 = get_float(request, 'lng2')

