# **台大月老(NTU Yue Lao)**
An event to help students at National Taiwan University find a match before Christmas.

## **Member**
We are students in National Taiwan University. Our members include:

曹灝翰

何宇紘

于宸胤

江筠喬

曾映捷
## **Content**
We will first design a Google Form to survey the love and value perspectives of people in the NTU Exchange Forum. The data will be processed using Python algorithms, and the pairs will be randomly matched based on similarity. Finally, an automatic email with a greeting will be sent to the email addresses of the paired individuals. The entire project includes data processing and algorithms in Python.

## **Matching Mechanism**
Each question has a scale of 1 to 7, with 1 being "strongly disagree" and 7 being "strongly agree". The maximum difference between the scales is 6, and there are a total of 25 questions, so the maximum total difference is 150.

First, pairs with a total difference of 0 are matched, and the data for these pairs are removed until there are no more pairs with a total difference of 0. If there are two heterosexual men and one heterosexual woman with a total difference of 0, the man who appears earlier in the randomized order is paired with the woman, and the same rule applies for pairing individuals of the same gender.

Next, pairs with a total difference of 1 are matched, and this process is repeated up to a maximum total difference of 150.

## **Participation**
Heterosexual group with 2,304 individuals, consisting of 1,403 men and 901 women. Pairing will begin with male-female pairs, and male-male pairing will be done for any remaining individuals within the group.

Gay group with 193 individuals.

Lesbian group with 77 individuals.

## **Data source**
We collected data from the suvey. The data include private information. Hence, we can not provide the data.

## **Algorithm and Code**
Please check the Algorithm in Algorithm.pdf file and code in main.py.
 
