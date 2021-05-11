from prac_06.guitar import Guitar

# vintage guitar - 98 years
gibson_l5_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
# non vintage guitar - 11 years
michael_mc_dne = Guitar("Michael MC DNE", 2010, 20100.50)

print("{} get_age() - Expected 99. Got {}"
      .format(gibson_l5_ces.name, gibson_l5_ces.get_age()))
print("{} get_age() - Expected 11. Got {}"
      .format(michael_mc_dne.name, michael_mc_dne.get_age()))
print("{} is_vintage() - Expected True. Got {}"
      .format(gibson_l5_ces.name, gibson_l5_ces.is_vintage()))
print("{} is_vintage() - Expected False. Got {}"
      .format(michael_mc_dne.name, michael_mc_dne.is_vintage()))