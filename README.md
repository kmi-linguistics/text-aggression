# Detection of Aggressive Behavior on Social Media
This is the repository of the aggression project carried out as part of the The Aggression Project at the Microsoft Research India Summer Workshop on Artificial Social Intelligence in June 2017. The repository contains all codes and datasets generated during the school.

The code helps detect types of aggression in Hindi, English and Hindi-English code-mixed data.
The analysis is done at 4 levels :



Aggressive--------------Non Aggressive (2 class) ----- END

|

Covert/Overt/Non Aggressive (3 class)	

|

Curse Abuse/Not Curse Abuse (2 class)

|

Types of threat- Non threatening/ 
Physical threat/Sexual threat/ 
Identity threat  (5 class)

|

END



## Training and Dataset

Data from Twitter and Facebook was used for training the 4 stage classifier. Tagged Data sets can be found in the 'Dataset' folder. Both the data files consist of 4 columns - id, text, aggression level and aggression sub-type.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.



## Prerequisites

python 2.7
NLTK Toolkit 3.2.x
SKlearn 0.18 



## Installing

1) Download the model files and put it inside the 'Codes' directory -
a. [Model File 1](https://drive.google.com/file/d/1Pzve4wHWtBaepUco-oroohEeiW6tha_E/view?usp=sharing)
b. [Model File 2](https://drive.google.com/file/d/10YHvH59GtQjkKMvhZb4o8u9SNFfzf0Sw/view?usp=sharing)
c. [Model File 3](https://drive.google.com/file/d/1RJVggvxhI7dI5u_pozyB4OrfI6g2rhD6/view?usp=sharing)

2) Type command ‘python all_features_test.py’ 					#takes about 4-5 minutes to run
3) A prompt saying- 'Enter your Sentence' shows up.
4) Type your sentence to obtain the 4 level aggression analysis.
5) Type 'exit' to finish.



## Citation
If you are using the dataset or the code in your research, please cite the following -

```@InProceedings{KUMAR18.861,
author = {Ritesh Kumar and Aishwarya N. Reganti and Akshit Bhatia and Tushar Maheshwari},
title = {Aggression-annotated Corpus of Hindi-English Code-mixed Data},
booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
year = {2018},
month = {May 7-12, 2018},
address = {Miyazaki, Japan},
editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
publisher = {European Language Resources Association (ELRA)},
isbn = {979-10-95546-00-9},
language = {english}
}```

For any queries / suggestions / offer for collaboration, you may contact ```ritesh78_llh@jnu.ac.in```

