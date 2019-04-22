#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Sivakrishna Uppalamethi
# DATE CREATED: April 22, 2019                                 
# REVISED DATE: April 22, 2019
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """  
    # Get the dictionary of dog names from the filename
    dognames_dic = get_dog_name_dict(dogfile)

    # print(dognames_dic)

    for key in results_dic:
      # Fetch the value (list) of each key into variable - value_list
      value_list = results_dic.get(key)

      # Read the elements from the list from index 0 - Pet label
      pet_label = value_list[0]

      # Read the elements from the list from index 1 - classified label
      classified_label = value_list[1]
     
     # print("PET_LABEL : {}, CLASS_LABEL : {}".format(pet_label, classified_label))
     # print(dognames_dic.get(pet_label))
     
      # Check if the pet label is present in the dog names dictionary (file)
      # if present append 1 to index position - 3 in the list - value_list
      value_list.append(get_label_from_dict(dognames_dic, pet_label))

      # Check if the classified label is present in the dog names dictionary (file)
      # if present append 1 to index position - 4 in the list - value_list      
      value_list.append(get_label_from_dict(dognames_dic, classified_label))
    

"""
  Find the label in the dictionary and return 1 and 0
  Parameters:
    dognames_dic - Dictionary of dognames with Key: dogname and value : 1
    label - the label to check in the dictionary
  Return:
    1 - if label found
    0 - if label not found
"""
def get_label_from_dict(dognames_dic, label):
  # if the key is foound in the dictionary - 1 is returned
  # else - 0 (default value)
  return dognames_dic.get(label, 0)



"""
  Read the input file using the filename and convert the lines in the file to a dictionary
  Parameters:
    filename - Input filename to convert to dictionary
  Return:
    Dictionary of dognames with Key: dogname and value : 1
"""
def get_dog_name_dict(filename):
  
  dognames_dic = dict()
  linecount = 0;
  # Reads in dognames from file, 1 name per line & automatically closes file
  with open(filename, "r") as infile:
      # Reads in dognames from first line in file
      line = infile.readline()     

      # Processes each line in file until reaching EOF (end-of-file) by 
      # processing line and adding dognames to dognames_dic with while loop
      while line != "":
          linecount += 1
          # Remove the newline character from the variable - line  
          #
          # Process line by striping newline from line
          line = line.strip().strip("/n")
          
          # check if the dogname(line) exists within dognames_dic, then if the dogname(line) 
          # doesn't exist within dognames_dic then add the dogname(line) 
          # to dognames_dic as the 'key' with the 'value' of 1. 
          if (dognames_dic.get(line,0) == 0):            
            dognames_dic[line] = 1

          # Reads in next line in file to be processed with while loop
          # if this line isn't empty (EOF)
          line = infile.readline()

  return dognames_dic


if __name__ == '__main__':
  dognames_dic = get_dog_name_dict("dognames.txt")
  # print(dognames_dic)



