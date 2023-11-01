from post_eval import evaluation
 
def test_single_operand():
  assert evaluation("5") == 5
  
def test_add_two_operand():
  assert evaluation("23+") == 5
  
def test_sub_two_operand():
  assert evaluation("23-") == -1
  
def test_mul_two_operand():
  assert evaluation("54*") == 20
   
