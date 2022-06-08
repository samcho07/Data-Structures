#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:09:00 2022

@author: mertsamast
"""

"""
Linked Lists
Mert SAMAST


Linked List: bağlı listelerdir.
Bir listedeki herhangi bir eleman, kendinden sonraki elemanın adresini işaret eder.

Önce bir node ve Linked list classları oluşturulur.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        
    
    # Linked Listteki elemanları yazdırmak için kullanılacak olan fonk.
    def printLList(self):
        # ilk olarak head'den başlıyoruz.
        tmp = self.head
        while tmp:
            print(tmp.data)     # Gördüğü elemanı yazdır.
            tmp = tmp.next      # Sonraki bağlanan elemana git.
    
    def insertBegin(self, new_data):
        #Eklenecek node'u belirtiyoruz.
        new_node = Node(new_data)
        #head'i, yeni eklenen datanın next kısmına atadık.
        new_node.next = self.head
        #Head, yeni düğümü işaret edecek şekilde kaydırdık.
        self.head = new_node
        
    def insertAfter(self, prevNode, newData):
        if prevNode is None:
            print("There is no prevNode. Please try again later.")
            return
    
        # create a new node:
        new_node = Node(newData)
        # 4
        new_node.next = prevNode.next
        # 5
        prevNode.next = new_node
        




"""
Linked list operations

Traverse:   Her bir elemana ulaşır.
Insertion:  Linked Liste'ye yeni eleman ekler.
Deletion:   Eleman siler
Search:     Belirtilen Node'u arar
Sort:       Listedeki elemanları sıralar.
    
"""


# =============================================================================
# Insert Element
# =============================================================================

# =============================================================================
# 1.Insert at the begenning
# .Allocate memory for new node
# .Store data
# .Change next of new node to point to head
# .Change head to point to recently created node
# =============================================================================

def insertBegin(self, new_data):
    #Eklenecek node'u belirtiyoruz.
    new_node = Node(new_data)
    #head'i, yeni eklenen datanın next kısmına atadık.
    new_node.next = self.head
    #Head, yeni düğümü işaret edecek şekilde kaydırdık.
    self.head = new_node
    
    

# =============================================================================
# 2.Insert After
# 1. check if the given prev_node exists
# 2. Create new node 
# 3. Put in the data
# 4. Make next of new Node as next of prev_node
# 5. make next of prev_node as new_node
# Inserts a new node after the given prev_node.
# =============================================================================

def insertAfter(self, prevNode, newData):
    if prevNode is None:
        print("There is no prevNode. Please try again later.")
        return
    
    # create a new node:
    new_node = Node(newData)
    # 4
    new_node.next = prevNode.next
    # 5
    prevNode.next = new_node
    
























