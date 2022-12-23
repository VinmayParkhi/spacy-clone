from django.shortcuts import render
from django.shortcuts import  render, redirect
from urllib.request import Request
from requests import request
from spacy.pipeline import EntityRuler
from django.http import JsonResponse

import spacy
nlp_segment = spacy.load("en_core_web_sm")

# Create your views here.
patterns = []
segment_ruler = nlp_segment.add_pipe("entity_ruler")


def home_page(request):
    return render(request,"home_page.html")


def take_para_and_que(request):
    # if request.method =='POST':
        print("###----------------###")
        paraghraph = request.GET.get('Notes_data')
        question = request.GET.get('Question')

        if question == 'Did the Insured driver take appropriate evasive action?':
            nlp_pipes = nlp_segment.pipe_names
            if 'segment_ruler' in nlp_pipes:
                nlp_segment.remove_pipe('segment_ruler')
            patterns = [{'label': 'evasive_action','pattern': 'applied brakes','id': 'Yes - Applied Brakes'},
             {'label': 'evasive_action','pattern': 'beeped horn','id': 'Yes - Sounded Horn'}]
            # segment_ruler = nlp_segment.add_pipe("entity_ruler")
            segment_ruler.add_patterns(patterns)
            segment_ruler.name = 'segment_ruler'
            token = nlp_segment(str(paraghraph))
            for ent in token.ents:
                if ent.ent_id_:
                    print("1111 ",ent.ent_id_)
                    break
            data = {'ent_id':ent.ent_id_}

        elif question == 'Traffic Conditions':
            nlp_pipes = nlp_segment.pipe_names
            if 'segment_ruler' in nlp_pipes:
                nlp_segment.remove_pipe('segment_ruler')
            patterns = [{'label': 'traffic_condition','pattern': 'heavy traffic','id': 'Heavy'},
             {'label': 'traffic_condition','pattern': 'no traffic','id': 'Light'}]
            # segment_ruler = nlp_segment.add_pipe("entity_ruler")
            segment_ruler.add_patterns(patterns)
            segment_ruler.name = 'segment_ruler'
            token = nlp_segment(str(paraghraph))
            for ent in token.ents:
                if ent.ent_id_:
                    print("1111 ",ent.ent_id_)
                    break
            data = {'ent_id':ent.ent_id_}

        elif question == 'Who changed lanes?':
            nlp_pipes = nlp_segment.pipe_names
            if 'segment_ruler' in nlp_pipes:
                nlp_segment.remove_pipe('segment_ruler')
            patterns = [{'label': 'lane_change','pattern': 'OV changed lanes','id': 'Claimant'},
             {'label': 'lane_change','pattern': 'OV switched lanes','id': 'Claimant'}]
            # segment_ruler = nlp_segment.add_pipe("entity_ruler")
            segment_ruler.add_patterns(patterns)
            segment_ruler.name = 'segment_ruler'
            token = nlp_segment(str(paraghraph))
            print("!!! ",paraghraph)
            for ent in token.ents:
                if ent.ent_id_:
                    print("1111 ",ent.ent_id_)
                    break
            data = {'ent_id':ent.ent_id_}

        elif question == 'Was the Claimant driver distracted?':
            nlp_pipes = nlp_segment.pipe_names
            if 'segment_ruler' in nlp_pipes:
                nlp_segment.remove_pipe('segment_ruler')
            patterns = [{'label': 'distraction','pattern': 'looking at cellphone','id': 'Yes - Cell Phone'},
             {'label': 'distraction','pattern': 'smoking a cigarette','id': 'Yes - Smoking'}]
            # segment_ruler = nlp_segment.add_pipe("entity_ruler")
            segment_ruler.add_patterns(patterns)
            segment_ruler.name = 'segment_ruler'
            token = nlp_segment(str(paraghraph))
            for ent in token.ents:
                if ent.ent_id_:
                    print("1111 ",ent.ent_id_)
                    break

            data = {'ent_id':ent.ent_id_}
            # if ent.label_ == label:
            #     print(ent.label_)
            #     print("### ",ent.ent_id_)

        return JsonResponse(data , content_type ="application/json", safe=False)

    #return render(request,"home_page.html")

#print(patterns)