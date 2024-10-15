# Poker Hand Evaluation with Machine Learning

## Table of Contents
- [Objectives](#objectives)
- [Texas Hold'em Rules](#texas-holdem-rules)
- [Data Representation](#data-representation)
- [Data Creation](#data-creation)
- [Classification of Hands](#classification-of-hands)
- [Rating of Hands](#rating-of-hands)

---

## Objectives
The primary goal of this project is to develop a machine learning model capable of evaluating and comparing poker hands in Texas Hold'em on two criteria : a note and a confiance value.

### Steps to achieve this:
1. **Data Representation**: Define an efficient encoding for poker hands (cards' rank and suit).
2. **Data Creation**: Generate labeled datasets for training the model.
3. **Hand Classification**: Train a model to classify poker hands statistics.
4. **Hand Rating**: Implement a system to compare and rate the relative strength of two hands.
   
## Texas Hold'em Rules
In Texas Hold'em, each player is dealt two private cards (known as "hole cards"), and five community cards are dealt face-up on the table in three stages (the flop, turn, and river). Players aim to form the best possible five-card hand using any combination of their two hole cards and the five community cards. Hands may be composed of a mix of private and community cards, and sometimes a player's hand may not be complete until all community cards are revealed.

### Possible Hands (ranked from strongest to weakest):
<table>
<tr>
<td width="50%" valign="top">

### Straight Flush
![Straight Flush](images/straight_flush.png)  
Five consecutive cards of the same suit.

### Four of a Kind
![Four of a Kind](images/four_of_a_kind.png)  
Four cards of the same rank.

### Full House
![Full House](images/full_house.png)  
Three of a kind plus a pair.

### Flush
![Flush](images/flush.png)  
Five cards of the same suit, not in sequence.

### Straight
![Straight](images/straight.png)  
Five consecutive cards, different suits.

</td>
<td style="border-left: 1px solid black;" width="50%" valign="top">

### Three of a Kind
![Three of a Kind](images/three_of_a_kind.png)  
Three cards of the same rank.

### Two Pair
![Two Pair](images/two_pair.png)  
Two cards of one rank and two cards of another rank.

### One Pair
![One Pair](images/pair.png)  
Two cards of the same rank.

### High Card
![High Card](images/high_card.png)  
When no other hand is made, the highest card plays.

</td>
</tr>
</table>

Expl

## Data Representation

The first step is to describe a card with a vector. I choosed to use a combinaison on two one-hot encoding, one for the card value (2 to ace) and one for the card color.
<p align="center">
  <img src="images/fig_1.png" alt="Fig_1">
  <br>
  <i>Figure 1: Representation of a single card</i>
</p>
As we can see on figure 1, each card is represented with 17 bits. 
This way to encode a card is efficient because value and color don't tend to be both relevant in a hand. (the only case it is is in a straight flush with 0.0279% chance of occuring. for a given player)
A binary representation of a card could take only 6 bits but for such a low dimention vector, simplicity is better than dencity.

We will then concatenate multiple cards to make a hand. Each hand is composed of 7 cards, but some of them can be null. We want to train the network on non-full hands. The firts two cards are always here (and will always be on the first 34 bits) to represent the two cards in hand. The five following cards can be present or absent (leaving 17 zeroes) representing communities cards. The order of the five cards is random and any of them can be null. 

<p align="center">
  <img src="images/fig_2.png" alt="Fig_2">
  <br>
  <i>Figure 1: Representation of a hand</i>
</p>





![Fig_1](images/fig_1.png)  
## Data Creation

## Classification of Hands

## Rating of Hands
