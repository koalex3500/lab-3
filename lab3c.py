#!/usr/bin/env python3

#will be using the single  function operate for three arguments
def operate(a, b, operation):
 if operation == "add":
  return a + b
 elif operation == "subtract":
  return a - b
 elif operation == "multiply":
  return a * b
 else:
  return 'Error: function operator can be "add", "subtract", or "multiply"'
