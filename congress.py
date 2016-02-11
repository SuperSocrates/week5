# Thanks to the NY Times API: http://developer.nytimes.com/docs

import json

# This class will (eventually) represent one member of Congress.
class ElectedOfficial:
  parties = ["D", "R", "I"]

  def get_all_from_state(state):
      with open("congress.json", encoding='utf-8') as f:
        data = json.load(f)

      rep_data = data["results"][0]["members"]

      member_list = []

      for person in rep_data:
          new_member = ElectedOfficial()
          new_member.name = "{0}, {1}".format(person["last_name"], person["first_name"])
          new_member.party = person["party"]
          new_member.state = person["state"]

          member_list.append(new_member)

      illinois_members = []

      for rep in member_list:
          if rep.state == state:
              illinois_members.append(rep.name)

      return illinois_members


  #Class-Level method
  def get_all():
      with open("congress.json", encoding='utf-8') as f:
        data = json.load(f)

      rep_data = data["results"][0]["members"]

      member_list = []

      for person in rep_data:
          new_member = ElectedOfficial()
          new_member.name = "{0}, {1}".format(person["last_name"], person["first_name"])
          new_member.party = person["party"]
          new_member.state = person["state"]

          if "votes_with_party_pct" in person:
            new_member.loyalty_factor = float(person["votes_with_party_pct"])
          else:
            new_member.loyalty_factor = 0.0

          member_list.append(new_member)
      ElectedOfficial.members = member_list
      return member_list


# This function reads from congress.json
# and returns a list of members of congress
# who have been in office long enough to
# # have voted on a bill at least once.
# # Also, can you spot two design patterns?
# def read_from_file():
#   with open("congress.json", encoding='utf-8') as f:
#     data = json.load(f)
#
#   rep_data = data["results"][0]["members"]
#
#   member_list = []
#
#   for person in rep_data:
#       new_member = ElectedOfficial()
#       new_member.name = "{0}, {1}".format(person["last_name"], person["first_name"])
#       new_member.party = person["party"]
#       new_member.state = person["state"]
#
#       if "votes_with_party_pct" in person:
#         new_member.loyalty_factor = float(person["votes_with_party_pct"])
#       else:
#         new_member.loyalty_factor = 0.0
#
#       member_list.append(new_member)
#
#   return member_list
