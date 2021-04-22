def fight_norman():
  global firsttime
  if firsttime == 0:
    firsttime += 1
    your_hp = 15
    norm_health = 20
  while True:
    read_letters(f"What would you like to do?:\n(A)ttack Norman with {held_item}\n(D)istract Norman\n(R)eturn to reception\n")
    answer = input("")
    if answer == "a":
      norm_health -= held_item_val
      if your_hp == 0:
        read_letters("""Norman triumphs over you, resulting in the end of your life.
Unfortunately Norman Bates was the last face you ever saw
And his reign of terror will proceed to rage on.""")
        again()
      if norm_health <= 16 and norm_health > 12:
        read_letters(f"You hit Norman for {held_item_val} damage\n'You really think this is hurting me?' Norman exclaims\n")
        norm_atk = random.randint(1,5)
        your_hp -= norm_atk
        read_letters(f"Norman hits you for {norm_atk} hp,\nWatch out, you only have {your_hp} hp left\n")
        continue
      elif norm_health <= 12 and norm_health > 6:
        read_letters(f"You hit Norman for {held_item_val} damage\n'You're not doing a great job!' Norman stumbles as he proclaims\n")
        norm_atk = random.randint(1,4)
        your_hp -= norm_atk
        read_letters(f"Norman hits you for {norm_atk} hp,\nWatch out, you only have {your_hp} hp left\n")
        continue
      elif norm_health <= 6 and norm_health >= 1:
        read_letters(f"You hit Norman for {held_item_val} damage\n'I told you I'm not letting you leave here alive!' Norman shouts with murderous intent\n")
        norm_atk = random.randint(1,3)
        your_hp -= norm_atk
        read_letters(f"Norman hits you for {norm_atk} hp,\nWatch out, you only have {your_hp} hp left\n")
        continue
      elif norm_health <1:
        death_text("Impossible, you...    Can't...       L e a v e......")
        read_letters("""\n\nNorman falls to his knees, a shiny key with a skull on the end
falls out of his pocket as he hits the ground, this is your chance to leave!
You rush to grab the key as fast as you put it in the door.
You turn the lock to here a click. You open the door and leave.
Goodbye Bates Hotel, you're free from this nightmare that once was.....
                
                """)
        death_text("         Right?...   \n")
        again()
    elif answer == "d":
          read_letters("Norman doesn't fall for your pitiful attempt to point and distract him,\nhe proceeds to launch you back into the reception.")
          reception()
    elif answer == "r":
          read_letters("You decide to return to the reception. Probably for the better...")
          reception()
    else:
          read_letters("That isn't possible.")
          continue