# --------------------------------------------------------
# (c) Copyright 2014, 2020 by Jason DeLaat.
# Licensed under BSD 3-clause licence.
# --------------------------------------------------------
""" Adds operators to the Maybe monad. """
import pymonad.monad
import pymonad.maybe
import pymonad.operators.operators

class Maybe(pymonad.operators.operators.MonadOperators, pymonad.maybe.Maybe):
    """ See pymonad.operators.operators and pymonad.maybe. """

def Just(value): # pylint: disable=invalid-name
    """ A Maybe object representing the presence of an optional value. """
    return Maybe(value, True)

# A Maybe object representing the absence of an optional value.
Nothing = Maybe(None, False) # pylint: disable=invalid-name





class Option(Maybe): # MonadAlias already in MRO from MonadOperators
    """ An alias for the Maybe monad class. """
    def __repr__(self):
        return f'Some {self.value}' if self.monoid else 'Nothing'

def Some(value): # pylint: disable=invalid-name
    """ An Option object representing the presence of an optional value. """
    return Option(value, True)