# Table of Contents
1. [Introduction](README.md#introduction)
2. [Explanation](README.md#Explanation)
2. [Instructions to run code](README.md#instructions-to-run-code)


# Introduction

This  repository contains the python solution for Insight Data Engineering Fellows program Coding Challenge.

The challenge can be summarised as follows:

For this challenge, we're asking you to take an input file that lists campaign contributions by individual donors and distill it into two output files:

1.medianvals_by_zip.txt: contains a calculated running median, total dollar amount and total number of contributions by recipient and zip code

2.medianvals_by_date.txt: has the calculated median, total dollar amount and total number of contributions by recipient and date.

The complete coding challenge statement is at  this link : https://github.com/InsightDataScience/find-political-donors



# Explanation

1. medianvals_by_zip.txt :

For every unique combination of valid CMTE_ID and ZIP_CODE, the contributions are stored in RunningMedian object.

This makes use of RunningMedian.py which calculates the running median of contributions by using two heaps, i.e, Min Heap and Max Heap, the current sum of contributions , the number of contributions for the data streamed so far.

The output file has the format : CMTE_ID|ZIP_CODE|Median|Number of contributions|Sum of Contributions

2. medianvals_by_date.txt :

For every unique combination of valid CMTE_ID and date, the contributions are stored in a list. The final output data is then sorted first by alphabetical order and then by chronological order.

The output file has the format : CMTE_ID|Date|Median|Number of contributions|Sum of Contributions

# Instructions to run code

The python code makes use of the libraries - numpy , collections , sys and math.
Use ./run.sh command to run the code. The input is at ./input/itcont.txt and the produced output is at ./output/medianvals_by_zip.txt and  ./output/medianvals_by_date.txt
