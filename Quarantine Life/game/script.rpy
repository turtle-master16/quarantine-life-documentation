# The Characters
define pl = Character("[player_name]")
define pr = Character("Prince", color="#bc42f5")
define c = Character("Carla (Mom)", color="#f5d442")

# Transitions
define wipeleft = CropMove(0.2, "wipeleft")
define wiperight = CropMove(0.2, "wiperight")

# Transforms
transform moveright:
    linear 0.5 xpos 0.85
# The game starts here.
label start:
    scene black
    # Ask name
    python:
        player_name = renpy.input("What is your name?", "Coby")
        player_name = player_name.strip()
        if not player_name:
             player_name = "Coby"

    scene bg living room
    with fade

    pl "A normal and peaceful afternoon."

    pl "Such a wonderful day to spend my day off just lying and relaxing around the house. Or maybe I could go out with some friends later on. Either way, it’s still a beautiful day."

    show prince smile
    with dissolve

    pl "Ack!"

    pl "What the heck?! Why did you hit me with a pillow?"

    pr "Mom said to get up and take out the trash. Just because it’s your day off doesn’t mean you can laze around and ignore all your chores."

    pl "I work hard on a day to day basis in the office. I deserve this much."

    show prince point

    pr "Mom’s orders, if you have a problem with it go complain to her. Now get to it."

    pl "So much for a relaxing afternoon."

    pl "*Sigh*. Whatever. Let’s just get this over with."

    hide prince point
    with dissolve

    "*phone buzz*"

    pl "Huh? A new notification?"

    menu:
        "Ignore your phone":
            pl "I’ll check it out after finishing my chores. I wouldn’t want to face mom’s wrath."

            jump news

        "Check your phone":
            pl "I’m sure checking my phone for a bit wouldn’t hurt. I can always do my chores later."

            scene black
            with wipeleft

            centered "Two hours later..."

            scene bg living room
            with wiperight
            pl "Pfft! Hahaha! This meme is so relatable. I wonder what time it is."

            pl "Oh god! It’s already been two hours?! I just looked at my phone for a moment."

            show carla angry
            with dissolve

            c "Didn’t I tell you to throw away the trash? And yet here you are playing with your phone."

            pl "Eep! Mom! I’ll go do my chores right now."

label news:
    scene black
    with wipeleft

    centered "An hour later..."

    scene bg living room
    with wiperight

    pl "Finally done with chores. I wanna go on a vacation so bad."

    show prince lazy
    with dissolve

    pl "Hey Prince, what are you doing, slacking off? I thought you’re busy with school work."

    show prince smile

    pr "I need a break too, you know."

    pl " I don’t think it’s considered as studying if you take a break every five minutes upon opening your lectures."

    show prince point

    pr "Don’t question my study methods. As long as I maintain my scores I’m good. Besides, I’m in high school, I know what I’m doing."

    pl "This kid. If he fails another test he’ll get another butt whooping from mom."

    pl "Okay, okay. If that’s what you want to do I’m not gonna stop you. Let’s just watch some TV."

    hide prince
    with dissolve

    "Reporter" "Breaking news, the Philippines has been suspending all flights from Wuhan City that is considered to be ground zero for the new coronavirus..."

    "Reporter" "...that has been causing respiratory illness, called COVID-19. Flights from other parts of China will also be strictly monitored… In other news…"

    pl "Man, what’s with this new coronavirus? I’ve been hearing about them a lot lately."

    show carla worried
    with dissolve

    c "Oh dear. Is it about that new virus going around? I hope your father is doing well abroad. He’s all alone out there and I hope it doesn’t affect him."

    menu:
        "Dad will be fine":
            pl "I’m sure dad will be fine. People are already aware of this new virus, people will start taking precautions on whatever this is."

            c "But still, I can’t help but worry for your father. I hope he’s doing ok. I’ll call him later after his work."

            jump emersion
        "The government will handle it":
            pl "I’m sure the government will do something about it."

            show carla handstop

            c "We can’t always depend on the government to do everything for us. We still have to do our part."

            jump emersion
        "We should be careful":
            pl "If that’s the case, the best thing we could do right now is to remain cautious and wait for further reports on this coronavirus."

            show carla worried

            c "I’ll contact your father. Oh, I hope he is doing alright."
    label emersion:
        hide carla
        with moveoutleft
        show prince confused
        with dissolve

        pr "Why is it that every time I watch the news there’s always something big like this is happening?"

        pl "Maybe you should stop watching celebrity gossip and watch the actual news instead?"

        show prince angry

        pr "They’re interesting. Leave me alone."

        pl "This is still alarming to hear. I hope this doesn’t turn out for the worse."

    label lockdown:
        scene black
        with wipeleft

        centered "Three months later..."

        scene bg living room
        with wiperight

        pl "It’s been three months since the COVID-19 was first announced. There have been a lot of reports going around the world related to this virus. This is so scary."

        "Reporter" "This just in, the president has declared a state of public health emergency."

        "Reporter" "Classes have been suspended and work-from-home is sought among local coronavirus cases. Citizens must remain in their homes until further notice."

        "Reporter" "Residents who refuse to follow the mandatory quarantine may be arrested under a state of public emergency with six months imprisonment and penalty fine."

        show prince happy at left
        with dissolve

        pr "No classes? Let's go!"

        show carla worried at right
        with dissolve

        c "It seems like we’ll be staying home for the next couple of months. The only time we’ll be able to go outside is when we need to buy basic necessities."

        show carla thinking

        c "I have to say, this is a smart strategy to contain the virus from spreading."

        menu:
            "I'm not staying home":
                pl "There is no way I’m staying home for that long."

                show prince curious

                pr "I don’t really mind. No school work means I can play video games all day every day."

                show carla handstop at right

                c "[player_name], the government just said that everyone must remain inside. It’s the safest thing to do to avoid the virus."

                pl "I can make decisions for myself. I don’t need the government to tell me what I can and cannot do."

                show carla please

                c "Please, you must think this through."

                menu:
                    "You're right.":
                        pl "I’m sorry, I wasn’t thinking clearly. You’re right, if I want to remain safe I must follow what the government says. I can always message them online."

                        show carla happy

                        c "Thank you for understanding."

                        jump proceed
                    "No, I do what I want.":
                        pl "Like I said, I’m a grown up, I can make decisions I know are best for me. I’m going to die of boredom if I stay home for that long."

                        jump getcaught
            "No work!":
                pl "Alright! I can sleep whenever I want now that I don’t have to wake up early to go to work."

                pr "And I can stay up all night playing video games!"

                show carla confused

                c "*Sigh* Why are two being so childish?"

                jump proceed
            "We should remain positive":
                pl "We just have to keep calm and stay positive. Everything will pass."

                c "If we’ll be staying here for more than a month, we need to find ways to save money."

                show prince smile

                pr "I know what I’m going to do for an entire month."

                show carla confused

                c "Are video games the only thing in your mind right now?"

                show prince happy

                pr "Yes..."

    label proceed:
        "TO BE CONTINUED"

        "Dialogue under Construction"

    return

    # Endings
    label getcaught:
        scene black
        with wipeleft

        centered "After a couple of days..."

        scene bg living room
        with wiperight

        show prince serious

        pr "Wow, you’re serious about going out? You’re even trying to sneak out at night so mom wouldn’t know."

        pr "Just to remind you, there is a curfew, all shops are closed and officials go on patrols to make sure people stay indoors."

        show prince point

        pr "And if ever you get caught, no one will be able to bail you out."

        pl "Mom is just overexaggerating about the whole pandemic thing and I am not going to get caught. I’ll be back later."

        show prince angry

        pr "Hey! Wait!"

        scene bg outside
        with dissolve

        pl "Wow. I’ve never seen the neighborhood so quiet before."

        "Police" "Hey you! Stop right there."

        pl "What are you doing?! Let go of me!"

        "Police" "You are under arrest for quarantine violation."

        scene black
        with dissolve

        centered "{color=#f00}{b}Bad End: Quarantine Violator{/b}{/color}"

    return
