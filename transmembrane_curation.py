#!/usr/bin/python3
import sys, os

hydrophobic_aminoacids=['A', 'I', 'L', 'M', 'V', 'F', 'W', 'Y']
hydrophilic_aminoacids=['R', 'K', 'D', 'E', 'Q', 'N', 'H', 'S', 'T', 'C', 'W', 'G', 'P']



def curation_of_aminoacids(firstgroup,secondgroup):

    tmp_secondgroup=secondgroup
    removed=""
    for aa in secondgroup:
        if aa not in hydrophobic_aminoacids:
            removed+=aa
            tmp_secondgroup=tmp_secondgroup[1:]
        else:
            break
    if removed=="":

        tmp_firstgroup=firstgroup
        to_move=""
        for position in range(1,6):
            if firstgroup[-position] in hydrophobic_aminoacids:
                to_move = firstgroup[-position] + to_move
                tmp_firstgroup=tmp_firstgroup[:-1]
            else:
                break
        if to_move == "":
            pass
        else:
            firstgroup=tmp_firstgroup
            secondgroup=to_move + secondgroup
    else:
        secondgroup=tmp_secondgroup
        firstgroup+=firstgroup + removed

    return (firstgroup, secondgroup)


def tm_protein_position_curate(sequence, minposition, maxposition):
    """ protein position curation """
    pre_helix=sequence[:minposition]
    tmhelix=sequence[minposition:maxposition+1]
    post_helix=sequence[maxposition+1:]

    pre_helix, tmhelix = curation_of_aminoacids(pre_helix, tmhelix)


    post_helix=post_helix[::-1]
    tmhelix=tmhelix[::-1]
    post_helix, tmhelix = curation_of_aminoacids(post_helix,tmhelix)
    post_helix=post_helix[::-1]
    tmhelix=tmhelix[::-1]


    print(pre_helix + "---" + tmhelix + "---" + post_helix)



sequences=dict()
# read the fasta file
fastahandle=open(sys.argv[1])
for line in fastahandle:
    line=line.rstrip()
    if line.startswith('>'):
        sequenceid=line[1:]
    else:
        seq=line.rstrip()
        sequences[sequenceid]=seq
fastahandle.close()

#print(sequences)

inputhandler=open(sys.argv[2])
for line in inputhandler:
    line=line.rstrip()

    data=line.split()
    if data[2] == "TMhelix":
        if int(data[3]) >=25 and (int(data[4]) - int(data[3]) >=20):
            seqid=data[0]
            minposition=int(data[3])
            maxposition=int(data[4])

            tm_protein_position_curate(sequences[seqid], minposition, maxposition)
    else:
        continue



exit(0)
