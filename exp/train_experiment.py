import os
from runner import Run 
from bongardGenerator.bongardGenerator import generate_bongard_example
from Benchmark.train.toLogic import toLogic
from Benchmark.train.toGraph import toGraph
import pandas as pd


dataset_name = "train"
ilpSettings = {
            "tilde": {
                "node_only" :[
                    f"predict({dataset_name}(+B,-C)).\n",
                    "warmode(has_car(+id,+-car_id)).\n",
                    "warmode(has_load(+id,+-car_id,+-load_id)).\n",
                    "warmode(short(+id,+-car_id)).\n",
                    "warmode(long(+id,+-car_id)).\n",
                    "warmode(two_wheels(+id,+-car_id)).\n",
                    "warmode(three_wheels(+id,+-car_id)).\n",
                    "warmode(roof_open(+id,+-car_id)).\n",
                    "warmode(roof_closed(+id,+-car_id)).\n",
                    "warmode(zero_load(+id,+-load_id)).\n",
                    "warmode(one_load(+id,+-load_id)).\n",
                    "warmode(two_load(+id,+-load_id)).\n",
                    "warmode(three_load(+id,+-load_id)).\n",
                    "warmode(circle(+id,+-load_id)).\n",
                    "warmode(triangle(+id,+-load_id)).\n",
                    "warmode(edge(+id,+-object,+-object)).\n",
                ],
                "node_edge": [
                    f"predict({dataset_name}(+B,-C)).\n",
                    "warmode(has_car(+id,+-car_id)).\n",
                    "warmode(has_load(+id,+-car_id,+-load_id)).\n",
                    "warmode(short(+id,+-car_id)).\n",
                    "warmode(long(+id,+-car_id)).\n",
                    "warmode(two_wheels(+id,+-car_id)).\n",
                    "warmode(three_wheels(+id,+-car_id)).\n",
                    "warmode(roof_open(+id,+-car_id)).\n",
                    "warmode(roof_closed(+id,+-car_id)).\n",
                    "warmode(zero_load(+id,+-load_id)).\n",
                    "warmode(one_load(+id,+-load_id)).\n",
                    "warmode(two_load(+id,+-load_id)).\n",
                    "warmode(three_load(+id,+-load_id)).\n",
                    "warmode(circle(+id,+-load_id)).\n",
                    "warmode(triangle(+id,+-load_id)).\n",
                ],
                "edge_based": [
                    f"predict({dataset_name}(+B,-C)).\n",
                    "warmode(has_car(+id,+-node_id,+-node_id)).\n",
                    "warmode(has_load(+id,+-node_id,+-node_id)).\n",
                    "warmode(edge(+id,+-node_id,+-object)).\n",
                    "warmode(instance(+id,+-node_id)).\n",
                    "warmode(train(+object)).\n",
                    "warmode(car(+object)).\n",
                    "warmode(load(+object)).\n",
                    "warmode(short(+object)).\n",
                    "warmode(long(+object)).\n",
                    "warmode(two_wheels(+object)).\n",
                    "warmode(three_wheels(+object)).\n",
                    "warmode(roof_open(+object)).\n",
                    "warmode(roof_closed(+object)).\n",
                    "warmode(zero_load(+object)).\n",
                    "warmode(one_load(+object)).\n",
                    "warmode(two_load(+object)).\n",
                    "warmode(three_load(+object)).\n",
                    "warmode(circle(+object)).\n",
                    "warmode(triangle(+object)).\n",
                ],
                "Klog": [
                    f"predict({dataset_name}(+B,-C)).\n",
                    "warmode(has_car(+id,+-car_id)).\n",
                    "warmode(has_load(+id,+-load_id)).\n",
                    "warmode(short(+id,+-car_id)).\n",
                    "warmode(long(+id,+-car_id)).\n",
                    "warmode(two_wheels(+id,+-car_id)).\n",
                    "warmode(three_wheels(+id,+-car_id)).\n",
                    "warmode(roof_open(+id,+-car_id)).\n",
                    "warmode(roof_closed(+id,+-car_id)).\n",
                    "warmode(zero_load(+id,+-load_id)).\n",
                    "warmode(one_load(+id,+-load_id)).\n",
                    "warmode(two_load(+id,+-load_id)).\n",
                    "warmode(three_load(+id,+-load_id)).\n",
                    "warmode(circle(+id,+-load_id)).\n",
                    "warmode(triangle(+id,+-load_id)).\n",
                    "warmode(edge(+id,+-object,+-object)).\n",
                ],
            },
            "aleph":{
                "node_only": [
                    ":- modeb(*,short(+id, -car_id)).\n",
                    ":- modeb(*,long(+id, -car_id)).\n",
                    ":- modeb(*,two_wheels(+id, -car_id)).\n",
                    ":- modeb(*,three_wheels(+id, -car_id)).\n",
                    ":- modeb(*,roof_open(+id, -car_id)).\n",
                    ":- modeb(*,roof_closed(+id, -car_id)).\n",
                    ":- modeb(*,zero_load(+id, -load_id)).\n",
                    ":- modeb(*,one_load(+id, -load_id)).\n",
                    ":- modeb(*,two_load(+id, -load_id)).\n",
                    ":- modeb(*,three_load(+id, -load_id)).\n",
                    ":- modeb(*,circle(+id, -load_id)).\n",
                    ":- modeb(*,triangle(+id, -load_id)).\n",
                    ":- modeb(*,edge(+puzzle, -object, -object)).\n",
                    f":- determination({dataset_name}/1,short/2).\n",
                    f":- determination({dataset_name}/1,long/2).\n",
                    f":- determination({dataset_name}/1,two_wheels/2).\n",
                    f":- determination({dataset_name}/1,three_wheels/2).\n",
                    f":- determination({dataset_name}/1,roof_open/2).\n",
                    f":- determination({dataset_name}/1,roof_closed/2).\n",
                    f":- determination({dataset_name}/1,zero_load/2).\n",
                    f":- determination({dataset_name}/1,one_load/2).\n",
                    f":- determination({dataset_name}/1,two_load/2).\n",
                    f":- determination({dataset_name}/1,three_load).\n"
                    f":- determination({dataset_name}/1,circle/2).\n",
                    f":- determination({dataset_name}/1,triangle/2).\n",
                    f":- determination({dataset_name}/1,edge/3).\n",
                ],
                "node_edge": [
                    ":- modeb(*,has_car(+id, -car_id)).\n",
                    ":- modeb(*,has_load(+id, -car_id, -load_id)).\n",
                    ":- modeb(*,short(+id, -car_id)).\n",
                    ":- modeb(*,long(+id, -car_id)).\n",
                    ":- modeb(*,two_wheels(+id, -car_id)).\n",
                    ":- modeb(*,three_wheels(+id, -car_id)).\n",
                    ":- modeb(*,roof_open(+id, -car_id)).\n",
                    ":- modeb(*,roof_closed(+id, -car_id)).\n",
                    ":- modeb(*,zero_load(+id, -load_id)).\n",
                    ":- modeb(*,one_load(+id, -load_id)).\n",
                    ":- modeb(*,two_load(+id, -load_id)).\n",
                    ":- modeb(*,three_load(+id, -load_id)).\n",
                    ":- modeb(*,circle(+id, -load_id)).\n",
                    ":- modeb(*,triangle(+id, -load_id)).\n",
                    f":- determination({dataset_name}/1,has_car/2).\n",
                    f":- determination({dataset_name}/1,has_load/3).\n",
                    f":- determination({dataset_name}/1,short/2).\n",
                    f":- determination({dataset_name}/1,long/2).\n",
                    f":- determination({dataset_name}/1,two_wheels/2).\n",
                    f":- determination({dataset_name}/1,three_wheels/2).\n",
                    f":- determination({dataset_name}/1,roof_open/2).\n",
                    f":- determination({dataset_name}/1,roof_closed/2).\n",
                    f":- determination({dataset_name}/1,zero_load/2).\n",
                    f":- determination({dataset_name}/1,one_load/2).\n",
                    f":- determination({dataset_name}/1,two_load/2).\n",
                    f":- determination({dataset_name}/1,three_load).\n"
                    f":- determination({dataset_name}/1,circle/2).\n",
                    f":- determination({dataset_name}/1,triangle/2).\n",
                ],
                "edge_based": [
                    ":- modeb(*,has_car(+id,-node_id,-node_id)).\n",
                    ":- modeb(*,has_load(+id,-node_id,-node_id)).\n",
                    ":- modeb(*,edge(+id,-node_id,-object)).\n",
                    ":- modeb(*,instance(+id,-node_id)).\n",
                    ":- modeb(*,train(+object)).\n",
                    ":- modeb(*,car(+object)).\n",
                    ":- modeb(*,load(+object)).\n",
                    ":- modeb(*,short(+object)).\n",
                    ":- modeb(*,long(+object)).\n",
                    ":- modeb(*,two_wheels(+object)).\n",
                    ":- modeb(*,three_wheels(+object)).\n",
                    ":- modeb(*,roof_open(+object)).\n",
                    ":- modeb(*,roof_closed(+object)).\n",
                    ":- modeb(*,zero_load(+object)).\n",
                    ":- modeb(*,one_load(+object)).\n",
                    ":- modeb(*,two_load(+object)).\n",
                    ":- modeb(*,three_load(+object)).\n",
                    ":- modeb(*,circle(+object)).\n",
                    ":- modeb(*,triangle(+object)).\n",
                    f":- determination({dataset_name}/1,has_car/3).\n",
                    f":- determination({dataset_name}/1,has_load/3).\n",
                    f":- determination({dataset_name}/1,edge/3).\n",
                    f":- determination({dataset_name}/1,instance/2).\n",
                    f":- determination({dataset_name}/1,train/1).\n",
                    f":- determination({dataset_name}/1,car/1).\n",
                    f":- determination({dataset_name}/1,load/1).\n",
                    f":- determination({dataset_name}/1,short/1).\n",
                    f":- determination({dataset_name}/1,long/1).\n",
                    f":- determination({dataset_name}/1,two_wheels/1).\n",
                    f":- determination({dataset_name}/1,three_wheels/1).\n",
                    f":- determination({dataset_name}/1,roof_open/1).\n",
                    f":- determination({dataset_name}/1,roof_closed/1).\n",
                    f":- determination({dataset_name}/1,zero_load/1).\n",
                    f":- determination({dataset_name}/1,one_load/1).\n",
                    f":- determination({dataset_name}/1,two_load/1).\n",
                    f":- determination({dataset_name}/1,three_load/1).\n",
                    f":- determination({dataset_name}/1,circle/1).\n",
                    f":- determination({dataset_name}/1,triangle/1).\n",

                ],
                "Klog": [
                    ":- modeb(*,has_car(+id, -car_id)).\n",
                    ":- modeb(*,has_load(+id, -load_id)).\n",
                    ":- modeb(*,short(+id, -car_id)).\n",
                    ":- modeb(*,long(+id, -car_id)).\n",
                    ":- modeb(*,two_wheels(+id, -car_id)).\n",
                    ":- modeb(*,three_wheels(+id, -car_id)).\n",
                    ":- modeb(*,roof_open(+id, -car_id)).\n",
                    ":- modeb(*,roof_closed(+id, -car_id)).\n",
                    ":- modeb(*,zero_load(+id, -load_id)).\n",
                    ":- modeb(*,one_load(+id, -load_id)).\n",
                    ":- modeb(*,two_load(+id, -load_id)).\n",
                    ":- modeb(*,three_load(+id, -load_id)).\n",
                    ":- modeb(*,circle(+id, -load_id)).\n",
                    ":- modeb(*,triangle(+id, -load_id)).\n",
                    ":- modeb(*,edge(+id, -object, -object)).\n",
                    f":- determination({dataset_name}/1,has_car/2).\n",
                    f":- determination({dataset_name}/1,has_load/2).\n",
                    f":- determination({dataset_name}/1,short/2).\n",
                    f":- determination({dataset_name}/1,long/2).\n",
                    f":- determination({dataset_name}/1,two_wheels/2).\n",
                    f":- determination({dataset_name}/1,three_wheels/2).\n",
                    f":- determination({dataset_name}/1,roof_open/2).\n",
                    f":- determination({dataset_name}/1,roof_closed/2).\n",
                    f":- determination({dataset_name}/1,zero_load/2).\n",
                    f":- determination({dataset_name}/1,one_load/2).\n",
                    f":- determination({dataset_name}/1,two_load/2).\n",
                    f":- determination({dataset_name}/1,three_load).\n"
                    f":- determination({dataset_name}/1,circle/2).\n",
                    f":- determination({dataset_name}/1,triangle/2).\n",
                    f":- determination({dataset_name}/1,edge/3).\n",
                ]
            },
            "popper":{
                "node_only": [
                    "body_pred(short,2).\n",
                    "body_pred(long,2).\n",
                    "body_pred(two_wheels,2).\n",
                    "body_pred(three_wheels,2).\n",
                    "body_pred(roof_open,2).\n",
                    "body_pred(roof_closed,2).\n",
                    "body_pred(zero_load,2).\n",
                    "body_pred(one_load,2).\n",
                    "body_pred(two_load,2).\n",
                    "body_pred(three_load,2).\n",
                    "body_pred(circle,2).\n",
                    "body_pred(triangle,2).\n",
                    "body_pred(edge,3).\n",
                    "type(train,(id,)).\n",
                    "type(short,(id,car_id)).\n",
                    "type(long,(id,car_id)).\n",
                    "type(two_wheels,(id,car_id)).\n",
                    "type(three_wheels,(id,car_id)).\n",
                    "type(roof_open,(id,car_id)).\n",
                    "type(roof_closed,(id,car_id)).\n",
                    "type(zero_load,(id,load_id)).\n",
                    "type(one_load,(id,load_id)).\n",
                    "type(two_load,(id,load_id)).\n",
                    "type(three_load,(id,load_id)).\n",
                    "type(circle,(id,load_id)).\n",
                    "type(triangle,(id,load_id)).\n"
                ],
                "node_edge": [
                    "body_pred(has_car,2).\n",
                    "body_pred(has_load,3).\n",
                    "body_pred(short,2).\n",
                    "body_pred(long,2).\n",
                    "body_pred(two_wheels,2).\n",
                    "body_pred(three_wheels,2).\n",
                    "body_pred(roof_open,2).\n",
                    "body_pred(roof_closed,2).\n",
                    "body_pred(zero_load,2).\n",
                    "body_pred(one_load,2).\n",
                    "body_pred(two_load,2).\n",
                    "body_pred(three_load,2).\n",
                    "body_pred(circle,2).\n",
                    "body_pred(triangle,2).\n",
                    "type(train,(id,)).\n",
                    "type(has_car,(id,car_id)).\n",
                    "type(has_load,(id,car_id,load_id)).\n",
                    "type(short,(id,car_id)).\n",
                    "type(long,(id,car_id)).\n",
                    "type(two_wheels,(id,car_id)).\n",
                    "type(three_wheels,(id,car_id)).\n",
                    "type(roof_open,(id,car_id)).\n",
                    "type(roof_closed,(id,car_id)).\n",
                    "type(zero_load,(id,load_id)).\n",
                    "type(one_load,(id,load_id)).\n",
                    "type(two_load,(id,load_id)).\n",
                    "type(three_load,(id,load_id)).\n",
                    "type(circle,(id,load_id)).\n",
                    "type(triangle,(id,load_id)).\n",
                ],
                "edge_based": [
                    "body_pred(has_car,3).\n",
                    "body_pred(has_load,3).\n",
                    "body_pred(edge,3).\n",
                    "body_pred(instance,2).\n",
                    "body_pred(train,1).\n",
                    "body_pred(car,1).\n",
                    "body_pred(load,1).\n",
                    "body_pred(short,1).\n",
                    "body_pred(long,1).\n",
                    "body_pred(two_wheels,1).\n",
                    "body_pred(three_wheels,1).\n",
                    "body_pred(roof_open,1).\n",
                    "body_pred(roof_closed,1).\n",
                    "body_pred(zero_load,1).\n",
                    "body_pred(one_load,1).\n",
                    "body_pred(two_load,1).\n",
                    "body_pred(three_load,1).\n",
                    "body_pred(circle,1).\n",
                    "body_pred(triangle,1).\n",
                    "type(train,(id,)).\n",
                    "type(has_car,(id,node_id,node_id)).\n",
                    "type(has_load,(id,node_id,node_id)).\n",
                    "type(edge,(id,node_id,object)).\n",
                    "type(instance,(id,node_id)).\n",
                    "type(car,(object,)).\n",
                    "type(load,(object,)).\n",
                    "type(short,(object,)).\n",
                    "type(long,(object,)).\n",
                    "type(two_wheels,(object,)).\n",
                    "type(three_wheels,(object,)).\n",
                    "type(roof_open,(object,)).\n",
                    "type(roof_closed,(object,)).\n",
                    "type(zero_load,(object,)).\n",
                    "type(one_load,(object,)).\n",
                    "type(two_load,(object,)).\n",
                    "type(three_load,(object,)).\n",
                    "type(circle,(object,)).\n",
                    "type(triangle,(object,)).\n",
                ],
                "Klog": [
                    "body_pred(has_car,2).\n",
                    "body_pred(has_load,2).\n",
                    "body_pred(short,2).\n",
                    "body_pred(long,2).\n",
                    "body_pred(two_wheels,2).\n",
                    "body_pred(three_wheels,2).\n",
                    "body_pred(roof_open,2).\n",
                    "body_pred(roof_closed,2).\n",
                    "body_pred(zero_load,2).\n",
                    "body_pred(one_load,2).\n",
                    "body_pred(two_load,2).\n",
                    "body_pred(three_load,2).\n",
                    "body_pred(circle,2).\n",
                    "body_pred(triangle,2).\n",
                    "body_pred(edge,3).\n",
                    "type(train,(id,)).\n",
                    "type(has_car,(id,car_id)).\n",
                    "type(has_load,(id,load_id)).\n",
                    "type(short,(id,car_id)).\n",
                    "type(long,(id,car_id)).\n",
                    "type(two_wheels,(id,car_id)).\n",
                    "type(three_wheels,(id,car_id)).\n",
                    "type(roof_open,(id,car_id)).\n",
                    "type(roof_closed,(id,car_id)).\n",
                    "type(zero_load,(id,load_id)).\n",
                    "type(one_load,(id,load_id)).\n",
                    "type(two_load,(id,load_id)).\n",
                    "type(three_load,(id,load_id)).\n",
                    "type(circle,(id,load_id)).\n",
                    "type(triangle,(id,load_id)).\n"
                ]
            }
        }

for num_examples in [20,50,70,100,125,175,200,225,250,275,300]:

    # only select the num_examples training examples
    df = pd.read_csv(os.path.join("docker","Experiment","train","relational","original","train.csv"))
    df = df.sample(num_examples)
    df.to_csv(os.path.join("docker","Experiment","train","relational","train","train.csv"),index=False)
    
    bongard_experiment_runner = Run(
        "train",
        ["node_edge","edge_based","Klog"],
        "class",
        "id",
        toGraph,
        toLogic,
        ilpSettings,
        "Experiment",
        num_examples,
        split_data=False
    )
    bongard_experiment_runner.TILDE = True
    bongard_experiment_runner.ALEPH = True
    bongard_experiment_runner.POPPER = False
    bongard_experiment_runner.GNN = True

    
    bongard_experiment_runner.run()
