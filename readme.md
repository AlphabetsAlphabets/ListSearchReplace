# Purpose of algorithm
The purpose of this algorithm is to allow the user, to change elements within a list. Search if an element exists within a list, and a list within a list. Furthermore, having the ability to replace the value with something of use.  
  
Currently the __readme.md__ file has documentation(this term is relative) on the only algorithm I wrote, which is LSR(List search replace). Therefore, this readme will only contain documentation for the aforementioned algorithms.    
  
Once I have written more algorithms. Each individual algorithm will be contained in it's on folder. With it's own readme file, outlining its use, and limitations.
  
# Features, and limitations
Link to [documentation](https://github.com/YJH16120/ListSearchReplace/blob/master/docs.md)

### Features
1. Able to search, and replace elements within a list. Even if the list is two layers deep. Meaning it has a list inside a list. While searching there will be return values. If you have a two layered list, it will return the indexs of the value. Which will get you to that element, for you to replace it or change it.

2. If the values inside a list are the same, such as binary options. It will be able to change the state of the binaries, with the replace method.  
  
3. Able to typecast values within a list or a layered list, to a single uniformed data type, across the list. So now you are able to change and edit elements within them as you see fit. Previously, if you had a nested list, and wished to convert a list of mixed data types it would be unable to do so. Now with this feature, changing everything to the same data type. You can use the replace function, to change anything as you see fit.  
  
### Limitations
Currently there are __no known__ limitations  

# Features to be added
There are no features to be added, as of now.
  
# Contributing guidlines
If you wish to contribute to this repository, feel free to do so under the __add ons__ branch. But first, go to the __review__ branch. So that you can see what features are being implemented. Then read the contribution giudline, for each of the features. Then move to the __add ons__ branch, name the file in the following format:
```
<featurename><V#>.py 
"""
Where # in <V#> is the file number, if there is a file made before you, increment the # by one. Using the TypeCasting feature as an example. 
If your commit is the first one of that feature name is TypeCastingV1.py If there is a filed before such as TypeCastingV1.py name yours TypeCastringV2.py
"""
```
If you would like to make a new feature of your own, name the file with your feature, along with a new markdown file, with the same name as your feature. Outlining what you are trying to do. And the problems/issues, you are currently facing while trying to implement the feature.
  
Even if there is no **Problems I am facing** section or anything similar in fashion, I encourage anyone to check the code, and see if you can improve it. Even if it's the code of the original file. The file without the V1 or V2's as a suffix. Is the file I made. You can improve, or change it in anyway.
