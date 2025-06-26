#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:43:57 2020

@author: Debapriya
"""

import os
import sys
import argparse
#import gmpy2 
from random import randint
import numpy as np
#from scipy.ndimage.interpolation import shift
import math

def ADD(instr):
    opcode=0
    funct=0x20
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rs=int(str_list[2])
    rt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def SUB(instr):
    opcode=0
    funct=0x21
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rs=int(str_list[2])
    rt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def AND(instr):
    opcode=0
    funct=0x24
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rs=int(str_list[2])
    rt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def NOR(instr):
    opcode=0
    funct=0x27
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rs=int(str_list[2])
    rt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def OR(instr):
    opcode=0
    funct=0x25
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rs=int(str_list[2])
    rt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def XOR(instr):
    opcode=0
    funct=0x26
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rs=int(str_list[2])
    rt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def ADDI(instr):
    opcode=9
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    rs=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,16)
    
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3
    
def ANDI(instr):
    opcode=0xC
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    rs=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,16)
    
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3
    


def ORI(instr):
    opcode=0xD
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    rs=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,16)
    
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3

def XORI(instr):
    opcode=0xE
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    rs=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,16)
    
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3
    
def SLL(instr):
    opcode=0
    funct=0x0
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    shamt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(shamt,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
    
def SRA(instr):
    opcode=0
    funct=0x3
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    shamt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(shamt,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def SRL(instr):
    opcode=0
    funct=0x2
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    shamt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(shamt,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def SLLV(instr):
    opcode=0
    funct=0x4
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def SRAV(instr):
    opcode=0
    funct=0x7
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
def SRLV(instr):
    opcode=0
    funct=0x6
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def LW(instr):
    opcode=0x23
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    rs=int(str_list[2])
    offset=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(offset,16)
    
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3


def SW(instr):
    opcode=0x2B
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    rs=int(str_list[2])
    offset=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(offset,16)
    
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3

def LUI(instr):
    opcode=0xF
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    imm=int(str_list[2])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(imm,16)
    
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3

 
def SLT(instr):
    opcode=0x0
    funct=0x2a
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rs=int(str_list[2])
    rt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rd,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5
    
    
    
def BEQ(instr):
    opcode=0x4
    instr=instr.strip()
    str_list=instr.split(',')
    rs=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(label,16)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3
    
def JUMP(instr):
    opcode=0x2
    instr=instr.strip()
    str_list=instr.split(',')
    target=int(str_list[1])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(target,26)
    
    return instr_val_0+instr_val_1
    
def JAL(instr):
    opcode=0x3
    instr=instr.strip()
    str_list=instr.split(',')
    target=int(str_list[1])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(target,26)
    
    return instr_val_0+instr_val_1
    
def JR(instr):
    opcode=0x0
    funct=0x8
    instr=instr.strip()
    str_list=instr.split(',')
    rs=int(str_list[1])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rs,5)
    instr_val_2 =np.binary_repr(0,15)
    instr_val_3 =np.binary_repr(func,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3
    
def FINISH(instr):
    opcode=0x3f
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,26)
    return instr_val_0+instr_val_1
 
    

   


file_a=open("machine_code.txt","w")


file_b=open("assembly.txt")

Instrs=file_b.readlines()

for instrs in Instrs:
    if(instrs[0:3]=="ADD" and instrs[0:4]!="ADDI"):
        ret_instr=ADD(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SUB"):
        ret_instr=SUB(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="AND" and instrs[0:4]!="ANDI"):
        ret_instr=AND(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="NOR"):
        ret_instr=NOR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="OR" and instrs[0:3]!="ORI"):
        ret_instr=OR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="XOR" and instrs[0:4]!="XORI"):
        ret_instr=XOR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="ADDI"):
        ret_instr=ADDI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="ANDI"):
        ret_instr=ANDI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="ORI"):
        ret_instr=ORI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="XORI"):
        ret_instr=XORI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLL" and instrs[0:4]!="SLLV"):
        ret_instr=SLL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SRA" and instrs[0:4]!="SRAV"):
        ret_instr=SRA(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SRL" and instrs[0:4]!="SRLV"):
        ret_instr=SRL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SLLV"):
        ret_instr=SLLV(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SRAV"):
        ret_instr=SRAV(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SRLV"):
        ret_instr=SRLV(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="LW"):
        ret_instr=LW(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="SW"):
        ret_instr=SW(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="LUI"):
        ret_instr=LUI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLT"):
        ret_instr=SLT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BEQ"):
        ret_instr=BEQ(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="JUMP"):
        ret_instr=JUMP(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="JAL"):
        ret_instr=JAL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="JR"):
        ret_instr=JR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:6]=="FINISH"):
        ret_instr=FINISH(instrs)
        file_a.write(ret_instr +','+'\n')
    else:
        print(instrs[0:14])
        print("danger danger undefined instruction!!!!")
        
        

file_a.close()
file_b.close()
    
























