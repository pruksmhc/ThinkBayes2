{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "#Title#\n",
    "\n",
    "NOTE: One should not participate in such activity and the author has not participated in such activity. \n",
    "This is based on that one movie about friends who cheat on the SAT. \n",
    "A group of four friends are about to take a major international math competition exam similar to the IMO but which is made up of one multiple choice question in mathematics. They pass by a room and see the Head of Examination for their school discuss the answer. Simon says he overheard the Head saying the answer is A and thinks it is the answer. The friends, since they love math, decided to do an analysis. The distribution of answers in the past are as below:\n",
    "A: 35% \n",
    "B: 19% \n",
    "C: 20% \n",
    "D: 26% \n",
    "Given that Simon was telling the truth (in that he indeed heard A), and human hearing at age 18 (Simon’s age) is inaccurate 0.24 of the time, what is the probability that the answer is indeed A? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from __future__ import print_function, division\n",
    "\n",
    "from thinkbayes2 import Hist, Pmf\n",
    "\n",
    "% matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The prior is stated as above. The original question is : given Simon heard A, what is the probaiblity that the answer is indeed A? Here, the set of hypothesis is binary, whether or not A is indeed the answer. P(H1) = 0.35, where H1 is the answer is indeed A. P(H2) = 0.65, where H2 is that the answer is not A. The likelihood, or P(D|H1) = (0.35)(0.76), and P(D|H2) = (0.65)(0.24). This is because if the answer is indeed A, then Simon's hearing must have been correct (0.76 chance). If the answer is not A, then Simon's hearing was faulty (0.24 chance)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Pmf' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-b56f12534f2d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mpmf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mPmf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;31m#uput in a doc string of what this is with teh funciton.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m#Comments: -- Go over, and what if you change the cosntants? generalize, creating a fuunction for code quality.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mpmf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSet\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'The answer to the exam is indeed A'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0.35\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mpmf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSet\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'The answer is not A'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0.65\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'Pmf' is not defined"
     ]
    }
   ],
   "source": [
    "pmf = Pmf()\n",
    "#uput in a doc string of what this is with teh funciton.\n",
    "#Comments: -- Go over, and what if you change the cosntants? generalize, creating a fuunction for code quality. \n",
    "pmf.Set('The answer to the exam is indeed A', 0.35)\n",
    "pmf.Set('The answer is not A', 0.65)\n",
    "pmf.Mult('The answer to the exam is indeed A', 0.76)\n",
    "pmf.Mult('The answer is not A', 0.24)\n",
    "pmf.Normalize()\n",
    "pmf.Print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "Thus, by adding the two likelihoods to get the normalizing factor and normalizing the two probabilities, we can see that the probability of the answer to the exam being indeed A is 0.63. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "The below are - solve some problems. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "<img src=\"bayes_problems.jpg\">"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
