import pdb
from collections import defaultdict

def preprocess(page_rank, N):
    fi=open('web-Google.txt','r')
    out_degree =defaultdict(int)
    in_edges = defaultdict(list)
    for line in fi:
        arr = map(int, line.strip().split('\t'))
        # calculates out_degree of vertices
        out_degree[arr[0]] +=1

        # calculate in_edges for a vertex
        in_edges[arr[1]].append(arr[0])
        
        # initializes page rank vector
        page_rank[arr[0]] = 1.0/N
        page_rank[arr[1]] = 1.0/N
            
    
    fi.close()
    return [out_degree, in_edges]


if __name__=='__main__':
    N = 875713 
    beta = 0.8
    
    page_rank = defaultdict(float)
    [out_degree, in_edges]= preprocess(page_rank, N)
    
    page_rank_p = defaultdict(float)
    counter =0
    while(counter <200 ):
        print "in interation: %d" %counter
        S=0
        for key in page_rank:
            page_rank_p[key] = 0
            if len(in_edges[key])==0:
                continue
            for eye in in_edges[key]:
                page_rank_p[key] +=beta * page_rank[eye]/out_degree[eye]
            S+= page_rank_p[key]
        
        # re-insert the leaked page rank
        print "value of S is : %.17f" %S
        for key in page_rank:
            page_rank[key] = page_rank_p[key] + (1-S)/N
        counter+=1
        print "answer is %.17f " %page_rank[99]
    
