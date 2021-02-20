import re, sys

crust = r'(thin|thick|gluten[ -]free|deep dish)'
delivery = r'(take[ -]out|deliver(y|ed)|pick[ -]up)'
location = r'(maple leaf|redmond town center|bellevue square)'
modification = r'((no |without )?(( and |, (and )?)?(pineapple|(red )?onions|(swiss|provolone|cheddar|mozzarella|extra)( cheese)?|black olives|green peppers|mushrooms|bacon|ham))+( (on|to) the (right|left|first|second) half)?)'
name = r'(eva|michael|logan)'
phone = r'(([0-9]{3}-?)?[0-9]{3}-?[0-9]{4})'
pizza_number = r'(\b(first|second|third|fourth|fifth|sixth|last|all)\b( one)?(?! half))'
quantity = r'(\bone(?!<)\b|two|three|four|five|six)'
size = r'(1[024] inch|small|medium|large)'
specialty_pizza = r'(hawaiian|4 cheese|vegetarian|vegan|meat lovers|pepperoni)'

def label_slots(utterance):
  utterance = re.sub(crust, r'<crust>\1</crust>', utterance)
  utterance = re.sub(delivery, r'<delivery>\1</delivery>', utterance)
  utterance = re.sub(location, r'<location>\1</location>', utterance)
  utterance = re.sub(modification, r'<modification>\1</modification>', utterance)
  utterance = re.sub(name, r'<name>\1</name>', utterance)
  utterance = re.sub(phone, r'<phone>\1</phone>', utterance)
  utterance = re.sub(pizza_number, r'<pizza_number>\1</pizza_number>', utterance)
  utterance = re.sub(quantity, r'<quantity>\1</quantity>', utterance)
  utterance = re.sub(size, r'<size>\1</size>', utterance)
  utterance = re.sub(specialty_pizza, r'<specialty_pizza>\1</specialty_pizza>', utterance)
  return utterance

def label_intent(utterance):
  if "start over" in utterance or "restart" in utterance:
    return "start_over"
  if re.search(r'(?<!i )(?<!me )(say (that )again|repeat)', utterance) != None:
    return "repeat"
  if "reorder" in utterance or "another order" in utterance:
    return "reorder"
  if re.search(r"status|check on|order ready|where('s| is) (\w+ )?(pizza|order)|^when.*(pizza|order)", utterance) != None:
    return "query_status"
  if "cancel" in utterance:
    return "cancel"
  if re.search(r'switch|actually|instead|change|no, (that was|i said)', utterance) != None:
    return "revise"
  if re.search(r'nope|not right|(?<!>)no\b', utterance) != None: # don't catch "<modification>no ...""
    return "deny"
  if re.match(r'do you|how (much|many)|what|when', utterance) != None:
    return "request_info"
  if "</" in utterance: # isn't anything that outweighs it and has a slot
    return "inform"
  if re.search(r'\b(hi|hello|hey)\b', utterance) != None:
    return "greet"
  if re.search(r'yes|yeah|yep|right|you bet', utterance) != None:
    return "confirm"
  if "thank" in utterance:
    return "thank"
  return "0"

for line in sys.stdin:
  utterance = label_slots(line)
  intent = label_intent(utterance)
  print(intent, utterance, sep="\t")