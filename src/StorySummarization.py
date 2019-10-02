from rake_nltk import Rake
import nltk.data
i

def summarizeText(text):
    r = Rake()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = []
    sentence_order = 0

    # extract phrases from sentence, then give sentence a value based on the phrases in the sentence and their values
    # keep track of original sentence order with sentenceOrder
    for sentence in tokenizer.tokenize(text):
        r.extract_keywords_from_text(sentence)
        sentence_score = 0
        for phrase in r.get_ranked_phrases_with_scores():
            sentence_score += phrase[0]

        sentences.append((sentence, sentence_score, sentence_order))
        sentence_order += 1

    sentences_ordered_by_highest_value = sorted(sentences, key=lambda unordered_sentence: unordered_sentence[1],
                                                reverse=True)

    # Summaries should be between 15-20% of their original content
    # Optimal score is a threshold. Any sentence with a score below this threshold will be cut from the summary
    optimal_summary_length = round(sentences.__len__() * 0.17)
    optimal_score = sentences_ordered_by_highest_value[optimal_summary_length + 1][1]

    summary_sentence_count = 0
    summary = ""
    for sentence in sentences:
        if sentence[1] >= optimal_score:
            summary_sentence_count += 1
            summary += sentence[0] + " "
            # print(sentence[0])
    print("original sentence count: ", sentences.__len__())
    print("summary sentence count: ", summary_sentence_count)
    print("summary as a percentage of the original: ", summary_sentence_count / sentences.__len__())
    return summary


story = '''Mr. Nebbia:  It was a good read wasn't it?  Okay.  So we're going to move on to my presentation on where we would like to go at this point.  And in considering how we might be able to bring government and industry together, it was important for us to provide a framework where people could work on technical issues, where they could dialogue back and forth, where they could breakout the parts of the work into more workable pieces, bite-size pieces, and then to come to some result that we could ultimately use in our ongoing dialogue with the commission regarding the re-purposing of the spectrum.
    
    So what we're looking to do here is to create a number of working groups, five, at this point, total, and all this is captured in the framework document that you have before you.  So we'd like to create five working groups to consider ways to facilitate the implementation of commercial wireless broadband in the 1695-1710, that's one of the working groups, and then four separate working groups in 1755-1850.
    
    We would then take the outcomes of the working groups that would be then submitted through the CSMAC for your review and ultimately, for recommendation on to NTIA in our ongoing work with the commission to re-purpose the spectrum.
    
    So we're planning to break it out in those working groups.  The structure for the working groups is such that we actually need a CSMAC participant in each group.  Our preference, at this point, is for that designated person to act as a liaison with the main body so that the main body and the co-chairs can be kept informed of what's taking place.
    
    In doing that, one of the things that we've seen in setting up this structure, we've seen that the 500 MHZ existing subcommittee and the sharing subcommittee, essentially, have a lot of work in common with this activity.
    
    And therefore, at this point, our choice is to stand those down for a period of time while this work is directly going on so that we can focus on this specific activity and come out with our results as quickly as possible.
    
    So we would then, in addition to having the liaison from the CSMAC, certainly like to invite all of you to participate in the working groups if you so choose.  Now, we understand that some of the backgrounds of CSMAC members don't link directly to some of the technical discussions that will have to go on, but we certainly want you to be assured that you're invited to participate.
    
    We would love to have you participate in the group, but we recognize that you may not have the specific technical background to work in some of the discussions.  So we would have this liaison, we would have other CSMAC participants who would like to join each of the working groups.
    
    NTIA will provide a representative, or more representatives, in each of the working groups.  The FCC has already committed a name, or more than one name, to each of the working groups, and then we will setup the groups to be co-chaired by an industry representative and a government representative.
    
    We've begun getting the names of the government representatives thus far.  We will -- in providing our invitations to people to participate in the groups, we will then be soliciting people to take on the industry co-chair role.
    
    So in the very near future -- well, let me go back to what we would like from you today so you can even be thinking about it as I continue to talk a little longer.  And that is, we would like to know whether you would be willing to be one of the CSMAC liaisons in any of these particular groups.
    
    So we'll look for as many answers as we can get today, but obviously, this may be a new idea, and therefore, we'd be happy to give you a few days to consider that.  Yes, Mr. Rush.
    
    Member Rush:  Charlie Rush here.  One very obvious question in my mind is, if we're to undertake a detailed analysis of the potential for sharing, it would make sense that we're going to have to do some sharing analyses.  Who, in your mind, is going to be responsible for doing that?
    
    Is NTIA going to do it?  Is the Federal Government going to do it based on recommendations or concepts put forward by the CSMAC and other representatives or is it something that you're going to expect the, I say you should do this, then you're going to turn around and we'll try to go ahead and do it; we'll reach a result?  Thank you.
    
    Mr. Nebbia:  We're certainly looking for a cooperative effort between all of the participants in the group.  We will be using, as the beginning point, the reports that we've drafted, or written.  So, for instance, the fast track report captures information about the weather satellite uses in the 1695-1710.
    
    There is an analysis associated with that report.  The 1755-1850 report, obviously, have different components and each one of them may have to be analyzed.  So as we break these out, we have, in fact, broken them into these separate groups, and I think the analysis required of each will be different, depending on the application that we have.
    
    Now, the framework document that we have written shows the breakout of what we are going to look at.  For instance, in Working Group 1, we're talking about the weather satellite receivers.  The fast track report recommended that a number of them be protected using exclusion areas.
    
    Those exclusion areas were determined based on an analysis using an understood commercial environment.  One of the questions that we have that this group will need to look at is whether we accurately reflected the commercial environment in that analysis, and that if we're able to improve upon that, we might actually be able to draw in exclusion areas or come up with other approaches.
    
    Each of them will have to have that type of, kind of, direct discussion on the issues related to each one.  But let me just finish a little bit on the work processes and then we can talk about the specific groups.
    
    So we're looking to have co-chairs from government and industry.  We will be soliciting the participants over the next week or so.  We have been provided recommended lists from various industry organizations to help us in trying to identify the right kind of people.
    
    Once again, we're looking for people who can work with us performing interference analysis; talk about the technical capabilities of the systems that they operate.  We recognize that, for instance, in the case of industry, we're probably talking about many of the same people across all of the working groups, since the uses will be the same across the working groups.
    
    On the other hand, from the government side, the uses differ greatly, depending on the working group.  So we would foresee there being different government people, probably, involved in each of those activities.
    
    So the work, as we get people together, is going to require a significant amount of cooperation.  We feel like, as an example, that we've had the 5 GHz Wi-Fi work that was done in the past where industry and government, the commission, and others, got together and worked through technical issues.
    
    They worked through how they were going to analyze problems, model problems, and so on, and came out with solutions that were workable.
    
    We see that as a model for groups being able to come together, provide a specific outcome that meets the need of the particular application they have, and then provide a recommendation that, ultimately, worked into the international community in that case, but ultimately, NTIA and the FCC were able then to use outcomes of that work in our own interaction and dialogue.
    
    So we think that's been a good example in the past of government and industry, on a working basis, pulling together.
    
    But in that cooperative effort, we're looking for the co-chairs, basically, to schedule the meetings, determine where they're going to be.  We will help them put together the contact list of people we ultimately invite.
    
    We, at the same time, will put out Bruce Washington's name on our Web site so that if someone else would like to volunteer to participate representing an industry group or a company, we would certainly be interested in their participation.
    
    So we're going to make an avenue for that to occur.  Yes, Kevin.  Sorry.
    
    Member Kahn:  So if we want to suggest other people from our own company into this process, is it best to simply go to that external process or should we route it internally, somehow, through you?
    
    Mr. Nebbia:  Your way would work fine for us, but if you want, Bruce is pulling in, certainly, other names, but, you know, if you called me one day and said, I got a person to suggest, I certainly would be happy to take the suggestion.  Yes, ma'am.
    
    Member Warren:  Sorry.  Jennifer Warren.
    
    Mr. Nebbia:  Can we pull the microphone over closer to her?
    
    Member Warren:  If also, we have members who have different technology that fall into different groups, would you be interested in people covering those different areas?  So if we have engineers that develop different systems that might be in the five different working groups --
    
    Mr. Nebbia:  Right.
    
    Member Warren:   -- you're interested in that kind of expertise spread out?  Okay.
    
    Mr. Nebbia:  And in fact, numerically, the groups we're looking to be represented is we certainly believe that the service providers need to be involved.  Some of them may have, you know, major interest, some of them may have rural interest, so we want to get a mix of service providers.
    
    On the other hand, the technical expertise that the technology builders have is absolutely critical to the discussion, so we're going to be looking for participants from the community that's building the devices, because they often, you know, understand the immediate impact of certain types of signals with the devices that they've built.
    
    We're also interested in people representing companies that build the government systems so that when we have the discussion, sometimes on the government side, we're managing programs in our direct familiarity with all the details and so on, we'll still need people that represent those technologies.
    
    So we're going to put our net fairly wide here to try to draw in as broad a range of people as possible.  Nonetheless, we are looking for the discussions to move forward at a fairly rapid pace, so we'll be making those initial invitations, in addition to names that may come in to Bruce, within the next week or so.
    
    As part of that process, we will be firming up who would be willing to act as a co-chair of the group, and in that same time, if we could conclude on who from CSMAC wants to participate directly in the groups.  But then as the groups begin their work, they're going to have to identify what the critical issues are within each of the application areas.
    
    This will be somewhat similar to our trying to identify specific questions within the CSMAC and that approach that we've taken.  For instance, within the weather satellite band, we know one of the critical aspects here is the issue of the exclusion areas, the size of the exclusion areas, maybe even the location of some of those exclusion areas, and we will need to pursue that further in the dialogue.
    
    Ed Drocella, from our office, will be participating in that.  Ed's got a long history in this work and I'm sure will be able to propel the discussion forward.
    
    The next working group we're going to form will deal with the law enforcement surveillance, electronic ordinance disposal, and some other short-distance links.
    
    And this, we'll be looking for a co-chair on the government side, and I should have mentioned in the last case, we'll be looking for a co-chair on the government side from commerce, NOAA, and Yvonne Navarro has been recommended for that.
    
    On the law enforcement surveillance side, DHS and Justice, we're looking for a name from them, and have received one thus far.  We just need to work that out.  On NTIA's side, we've got Rich Orsulak and Scott Jackson, both come from a long history in public safety-type operations.
    
    But the focus of the work here is going to be quite different.  In this case, based on our past experience with 1710-1755, we recognize that low-power law enforcement surveillance systems sharing with ubiquitous newly-implemented commercial wireless is an issue.
    
    And therefore, that represented the biggest hurdle I think we had in the relocation of the 1710-1755 band.  It will represent a similar hurdle in this band.  They operate across the entire band.  The systems that they have, for the most part, are very wide bandwidth receivers, and therefore, you know, one signal might impact several operations.
    
    Also, they have a nationwide authorization to go where they need to go and when they need to go, so this is really a challenging issue.  We know that they're not compatible.
    
    So in this case, what we're essentially asking the group to begin to look at is, what is the nature of the transition that the government might plan to pull out of the band?  Now, the federal law enforcement-type agencies have actually laid out, in our report, a three-step process for them, and that's one of the reasons why their costs are predicted to be fairly high.
    
    The first move is to get out of the 1755-1780 band within the five-year period and to go to a digital technology; continue operating in the rest of the band.  The possibility exists that at a later date, they could squeeze to a smaller number of megahertz by improving their digital capability at that point.
    
    And ultimately, potentially, move out of the band altogether, if, in fact, they can find another band that they can move to.
    
    So in this case, the essential question, I believe, is going to be, what's the transition plan for them moving out?  Now, what that means to them is they move out, basically, cities at a time, at least that's how it occurred the last time, so they may want to move out of New York on a set date, San Francisco another date, and so on.
    
    The critical thing is for us to be able to align, as much as possible, the interests of industry in moving in with the interest of the government in moving out.  And the government showed, in the past, that they were willing to reorder their plans if they knew what the requirements were.
    
    But, of course, getting into the process and then finding somebody needed San Francisco today and San Francisco was, like, 25th on the list, and we've talked about the NFL cities, I guess that's a common term in industry.
    
    They are where the major bands are, so we need to go beyond recognizing which are the major NFL cities and what the actual order of desire might be.  So we're going to have to talk about what industry's willing to discuss, what government's willing, and try to match up that order.  So that's, in that particular case, what we're looking at.
    
    As we move on to the satellite control and electronic warfare, the critical aspects here are, obviously, the satellites are not moving within a near time frame.  So the satellite control links and those locations around the country have got to be protected through some sort of mechanism.
    
    Interestingly enough, the interference problem, however, is into industry in this case.  So we've got to come up with a construct that will allow us to use as much as that space as possible with the assurances that it's not going to bite the government when and if the signal gets some sort of interference.
    
    So that's going to be the critical portion in this case is, the regulatory construct that we come up with that makes everybody feel that this is workable.
    
    On the electronic warfare side, some of you don't know, you know, too much about why is this important, but obviously, if you read the papers it's clear every day that the bad guys set off systems, devices, using current technology; cell phones.
    
    So it's important that DoD have the ability to test, to train, and this is a band that offers them commercial technology and a band, right now, that they have access to.  So if we're going to provide the access to the commercial community, DoD has got to have guarantees that they can train as they need to train.
    
    And that's going to be, once again, a regulatory construct that provides them what they need.  Tactical Radio Relay and Fixed Microwave, okay, we're already very familiar with the Fixed Microwave.  Gary Patrick, who shepherded our 1710-1755 relocation, will be involved in this.
    
    So we have lots of experience with the Fixed Microwave.  The Tactical Radio Relay has some different issues to it, but also, in that case, we do have some experience in industry and government coming together and working out arrangements that allow for the exclusion areas around the three permanent sites to be narrowed, in reality, on the ground, and so on.
    
    So we see some hope there in the protection areas not being as great as we might have defined in the past.  We're also excited about the possibility that the government, military particularly, may be moving toward more commercial-type technologies.
    
    And any way we can provide DoD with training opportunities where the connection between the wireless industry and their operations begins to become somewhat seamless, giving opportunities for both, then maybe we should pursue those.
    
    The biggest challenge, of course, is going to be the airborne operations, and therefore, we stole John Hunter from DoD after they stole him from T-Mobile, and we're glad to have John onboard to work in this area.
    
    We also want to note that there has been an STA request put in by T-Mobile, working together with CTIA, to do some measurements and testing in the band that might help them identify what the implications are of these airborne operations.
    
    So that work is going to depend a great deal, I think, on what they see when they do those measurements.  Some of that may be pure monitoring, some of it may be actual testing with the government operations.
    
    Ultimately, we are shooting for trying to wrap these issues up, primarily, for most of them, in January of next year.  The reason for that is, if we're going to be ready to have a portion of this spectrum available for the commission to work together with the 2155-2180, we've got to have that ready at that point.
    
    So in these discussions, we see them talking about the entire band, but also considering how the lower band may be able to be made available earlier.  If you look in our report, you will note a number of agencies saying that they could vacate the lower portion earlier, but only as a part of a longer term plan.
    
    So we think there may be some great potential there, but nonetheless, as we make the spectrum available, in these transitions and in these sharing modes, the distinctions of when certain portions get auctioned and others, you know, happen later, that may become a little less distinct, and certainly may not require different actions from the government.
    
    If we can come out with a way of sharing across the band, then maybe we can auction 1755, 1710, right away, but the next access in the other bands is essentially the same type of shared access.  That's a possibility.
    
    Okay.  We know it's your fault now.  Yes.  It's just my booming voice.  So on the other hand, we believe that the weather satellite band, 1695-1710, we would hope, can be done in a much shorter period of time.
    
    We think that the issues there are much more limited in terms of seeing if we can improve those coordination areas, or exclusion areas, excuse me, so in that case, we're hoping for an earlier date in September to complete that work.
    
    So that's kind of the order of march.  In fact, that band is likely to be the one we try to kick off as quickly as possible.  Sorry.  We're getting more.  And any mics that are still pointing at me or something.  Okay.
    
    Anyway, that's the time frame we're looking for.  We would envision each of the working groups coming back with a report, or reports, possibly more, if there are pieces that they can identify along the way.  Each of those reports would come back through the CSMAC for your consideration.
    
    And ultimately, you would then recommend what gets sent on to NTIA.  Now, I should say, in doing that, because we're looking for a cooperative environment and outcomes that meet both the commercial needs and the government needs, we are looking for outputs that represent a consensus outcome.
    
    So as people are working together, we need to continue to keep ourselves in the same room until we work through whatever hurdles and difficulties we find.  So our goal is that these groups would submit, up to CSMAC, agreed outcomes, not ones that have lots of loose ends and things we couldn't resolve.
    
    We need to work toward agreed outcomes so that, ultimately, we can work with a commission to put forward a clear path for re-purposing the band.  So thank you.  Any questions?  The questions today and the interaction is limited to the actual members of the CSMAC, so we've got to stick with that.  That's the agenda today.  So, yes, sir?
    
    Member Tramont:  Bryan Tramont, so we have a July meeting already slated, and probably another, like, a September and then a January, and have, sort of, iterative presentations from each of the working groups at those three meetings, with potential, some final reports in September and others in January?  Is that the lineup?
    
    Mr. Nebbia:  That's certainly my hope, yes.
    
    Member Gibson:  Mark Gibson.  You mentioned that two of the existing working groups will go into stasis, but what about the others?  Are you expecting reports from the, what is my working group, Spectrum Management Improvements on License?
    
    Chair Fontes:  At the end of this there are, I believe, a couple of additional products that are going to be produced.
    
    Member Gibson:  Okay.  One other question related to the work plan, in the framework, you mentioned issues with classified data, would those be surfaced in the ongoing discussions or do you want to service them at some point beforehand?
    
    Mr. Nebbia:  Yes.  I think they are going to get surfaced as the discussions go on.  My experience thus far is that classified information, generally, does not have to be brought into the mix here.  We may find that that's not the case, but generally, I think that that is the case.
    
    So I'm hopeful that we will not have to have that kind of direct classified discussion, however, if we do, then we'll have to resolve among the participants there, issues regarding clearances, and where we have those discussions, and what the nature of them be.
    
    I mean, we foresee there being some interest and concerns on the commercial side about some of their plans and so on, and, you know, we recognize that, and we will have to work with the information that people can provide to us.
    
    I think on the government's side, your bigger challenge will be in information that the government agencies consider to be sensitive in some way.  And, once again, I think in that case, we're going to have to look closely at what that is.
    
    A great example right now is information regarding the law enforcement surveillance bandwidth was not made available before the 1710-1755 auction.  It's now based on the fun that we've had the first year or so after the auction.  It's, you know, certainly well-known at this point.
    
    So there's some aspects like that, we would not expect some of the same sensitivity that we might have had before, but we'll have to look at those things.  We also recognize that, at least with some of the system characteristics, it doesn't take that much for someone to go out and, you know, do spectrum monitoring and pick up the characteristics of the system.
    
    So, you know, that's something we'll have to work through, but I think we can probably avoid classified discussions, more sensitive, we may have to have that conversation and decide what both the agencies and the commercial side are comfortable with.
    
    And, once again, I think, for me, a critical component here is just the cooperative environment where people are able to discuss these things and to say, well, I'm not free to talk about that, but let's go back and see how we might be able to approach that; that sort of thing.
    
    I think the discussions from the groups really need to stay in those groups; working through the issues.  We can't, once again, start fighting each other out in public when we're actually trying to carry out these conversations.
    
    Yes, there's no lawyers rule.  Okay.
    
    Chair Fontes:  Karl?
    
    Member Povelties:  I'm glad to see this work effort start and really happy to see that we're looking at relocation in addition to sharing.  I was wondering if, as part of the review, you were also going to look at some of the cost estimates that were provided and determine how accurate or inaccurate those may be?
    
    Mr. Nebbia:  Ultimately, the firming up of cost estimates is part of a formal process under the CSEA that we went through in the last go around.  And you can look back on the history there and you'll find, for instance, that in about 2001, we gave estimates, somewhere, about $900 million, and that actually, the outcome today is closer to $1-1/2 billion.
    
    So the numbers have actually come up since that point, but nonetheless, coming up with initial estimates is just that and we will be working through that process as we get closer to the decision point and as we get into the CSEA process.
    
    But I don't foresee these working groups working on a changing of the numbers.  We're working on, how can we work through the transition?  How can we live in environments where we're both there?
    
    I mean, ultimately, and this gets back to this question of relocation versus sharing, if you have to share with somebody for ten years, and that process works, then we have to ask why would we spend the money then to move them?
    
    So I think all those things fit in to the discussion.  We realize, as Tom said, we'd all rather have our own tents, but the military issued me a shelter half many years ago and told me that I was going to have to bunk with a really mean looking Sergeant and I, somehow, managed to do that.
    
    Chair Fontes:  Charles.
    
    Member Rush:  Thank you.  Charles Rush.  I have a couple questions that are probably getting into the details and you may not want to, you know, address them here, but I think they may be worthwhile, at least, giving some thought to.
    
    We have five different groups and four of them are working in the same frequency range, how do we assure that we're looking at uniform characteristics of the commercial deployment?
    
    You know, I think it's necessary that that not become an issue, that we all agree, somewhere, early in the process, if we can today, what it is that we envision in terms of the future deployment of whatever you want to call the mobile environment at this point in time, that would be applicable for these bands.
    
    And I think that, you know, that might not be something that is just simple, so we need to get some mechanism established to get that going, I think, sooner than later.
    
    Mr. Nebbia:  That's an excellent question, Charlie, and as we indicated at 1695, we did an estimate working with the commission on what the environment might look like, but we think that estimate can probably be improved.
    
    And also, we'll certainly be expecting that as we meet together with people from the equipment manufacturers, from the service providers, my expectation is that they would be, you know, going back and huddling themselves as to how to best present that environment.
    
    So we would certainly hope that they can come together and provide us with a good sense of what that will be.
    
    Chair Fontes:  Janice.
    
    Member Obuchowski:  I'd like to associate myself and partner with Charlie's observation and tie it to, I think, a somewhat thorny question.  So we all operate in good faith, we have an assumed set of parameters for the commercial partners in the band, we come up with some reasonable sharing approaches, what is the guarantee that when the FCC takes up its commercial band param we're sharing, that it's implying the same architecture?
    
    Because you don't have to be an engineer, I am not, to notice that there's a really substantial difference of opinion between the PCAST study and a carrier perspective, upon which typical auction revenues, historically, have been based.
    
    So you have two different world views and I don't think the FCC has signaled yet which path it intends to go down and I don't think Congress has either.  It raises a tough question for this process.
    
    Mr. Nebbia:  Well, I mean, we're certainly looking in these two particular bands for how they might be made available for commercial wireless, and that's our focus here.
    
    We do understand that one of the hidden recommendations from PCAST is moving the commission over on to NTIA's responsibility, but nobody's read that far into the report yet.  But we see the commission working actively and participating actively in these groups.
    
    And I think we have at least the history of cooperating over the 5 GHz Wi-Fi issue to come out with agreed upon outcomes, and that's certainly our goal.  Mike.
    
    Member Calabrese:  Something to add to Charlie's question is under the, you know, increasingly we see, even among, I think, some of the carriers, you know, very recently, much more of a move towards microcells, small cells, lower power.
    
    So is that scenario, is there room to address that in the alternative?  Because it could well be that, if you look at sharing, that that's a much more efficient way to accommodate the continued operation of the federal primaries.
    
    And if we only look at this at a very high power, like the original fast track report, I think, only looked at high power, you know, you might miss a lot of important policy insight into, you know, what sort of use of the band is most efficient.
    
    Mr. Nebbia:  Well, I think we certainly see lots of possibilities here.  We'll be looking for industry to represent those possibilities as opposed to us trying to put a construct over it.  So we'll be looking for them to come in, they have a sense of what their financial base is, and so on.
    
    And so they may find that solutions for specific operations are smaller cells and they'll have to consider that, but we're not looking to put that kind of, you know, direction into it.  We're looking for their input and feedback.  Yes, ma'am.
    
    Member Warren:  Jennifer Warren.  I just want to continue the thread that's begun here because I appreciate what you're saying about you won't be directing it, NTIA won't be directing it, but it does seem to go back to the original question that there needs to be a common input to all the different working groups, and that that is the, you know, precursor to, then, those discussions in each of the working groups, so that they're all working on the same, almost the same, band, so the same approach.
    
    So where is the working groups that's going to have the industry all come together and what they want the working groups to look at?  I mean, how does that get formulated and do you have a time frame by which you want that input to be ready for these working groups to get started?
    
    Because I don't think you can have -- it could be somewhat inefficient to have it being done, you know, in all four working groups and then the product might not be the same.
    
    So perhaps there could be a starting point where that product is put in for distribution to the co-chairs and those individual working groups.
    
    Chair Fontes:  A whole series of questions.
    
    Member Warren:  Sorry.
    
    Mr. Nebbia:  You know, let me just --
    
    Member Povelties:  It's all a slice as part of this search for 500, that group, working group, there was some technical characteristics put into that.  The suggestion may be that that would be a baseline and then the working groups could then look at that and see if it needs to be modified based on other things, such as what Mike was saying with the small cells.
    
    Mr. Nebbia:  Yes, sir.
    
    Member Tramont:  You're probably going to say what I'm going -- this is Brian Tramont, I would just say that, obviously it's important when you're naming the people to each of the groups that we have representative samples across all different commercial models so that each can calibrate.
    
    I agree with you, Jennifer, I think it'll be important that the commercial entities across all five working groups talk to each other.  I'm just not sure that adding another layer of having a common set of agreements from the commercial side before you go into the five working groups is achievable.
    
    So I think it's more important that you just have consistent representation across all five with good communication across the industry sectors in all five so that the commercial folks bring to the table the same set of assumptions, because the problem is, you're not going to have it, right?
    
    The individual CMRS providers are going to have different models.  Individual unlicensed providers will have different models than manufacturers.  You're not going to have a completely uniform approach.
    
    Member Kahn:  Kevin Kahn.  Realistically, there's not a whole lot of different standards being pushed right now.  I mean, there's been enough coalescence around standards directions that I think, you know, while we can hypothesize anything, there's really, you know, only a couple, and they're not much different from one another, the ones that are actually in development.
    
    And the standards roadmaps go out, you know, easily, into the ten-year time frame.  So while, you know, I'm sensitive to the theoretical question here, in a practical sense, the systems that are going to be built, for commercial use at least, are going to conform to wherever those standards are headed.
    
    And I think, you know, we ought to just assume, and maybe explicitly state that, what we're looking at our systems that appear to be, you know, in the general conformance with where those standards bodies seem to be head, because it's not a big guess.
    
    I mean, you know, there's drafts, there's everything for those things.  And, yes, you can argue around the corners and they'll be, like any standards group, you know, tons of arguments around the corners of those standards, but the dominant thrust of those standards are not going to, you know, suddenly take a hard-right turn somewhere.
    
    So, you know, I think this may be a little less of an issue than it could be.
    
    Member Rush:  I tend to agree with what Michael said and with what Jennifer said, and I'm sorry Brian, I have to disagree with you because I think that if everybody comes in with their own little nuance, what we're going to have is a very, very dissected viewpoint of, you know, what the shared environment is going to be.
    
    And, you know, I think we need to avoid that.  I'm going to do something that I said 15 years ago that if I did I would know it's time to leave, so I'm just probably going to leave.  I remember when I was working for the FCC in the year 2000 and I sat down with Diane Cornell and I said, we need to come up with a set of parameters to do some studies for this thing called INT2000, and how can we get that?
    
    And what the FCC at that point in time did was, they asked all the industry people to come in, and to provide their list of parameters, and the values associated with that parameter that would be needed for sharing studies.
    
    And we put the caveat to them that, if you can't do it, we will do it for you, and we will do the studies for you, and you probably don't want that.  And that led to a major effort on the part of the industry to then CTIA, or whatever it was called at that time, and that's what gave birth to the documentation that's in the ITU-R now for the parameters for INT2000.
    
    The ITU-R is going to go through the same process for INT Advance, but we can't wait for them to get that done.  I really think that we do need to have an agreement on the kinds of parameters that are needed and the concept, how these systems are going to be deployed, because Michael was absolutely correct, you've moved away from the notion of you have macrocells, you have microcells, and picocells, all separating.
    
    You now have picocells embedded within the macrocells, and you have relay modes, and you have femtocells, all of that means that the concept of having maximum power, and that's what you do your worst-case simulations on, has become those are worst-case, impossible, totally unrealistic simulations.
    
    We have to make the effort to take the step to be able to, as best we can, simulate what it is that the actual deployment is going to be, at least on the commercial side, and the gentleman from Intel is exactly correct, there's only so many standards that are out there, that we're talking about, form the commercial side.
    
    And it's, basically, the LTE family.  And that's not all that difficult to be able to come to some sort of coalescence on that and, you know, that particular approach.  And I would be glad to work on that particular issue, but not by myself.
    
    Mr. Nebbia:  Well, once again, I think, obviously, there does need to be a coming together on the industry side as to what represents that.  We would certainly have to have, I think, another discussion here whether we would intentionally setup a group to specifically do that.
    
    In a couple of the cases that we're dealing with, for instance, the satellite operations and the electronic warfare, we're, you know, coming up with -- I mean, we've got government operations that we know about.  I don't think it's a matter of the construct of the commercial operation, so very potentially, they could start working on their regulatory construct without spending the time.
    
    On the airborne stuff, a big part of the starting will be performing measurements and identifying how often the devices operate, what they look like, because, once again, there's concerns into industry, but as we start approaching how we would protect government operations, we'll need to understand that information better than we do today.
    
    And it should be as consistent as possible across the various discussions.  At the same time, I'm aware that, for instance, in industry's coordination with the tactical radio relay on the government side, those types of initial calculations produced fairly large areas.
    
    And it's not till you get past that that you actually get to where the solutions are.  So those things tend to provide an initial baseline for the discussions, but ultimately, companies have tailored their operation to be compatible around those bases to the point where, in some cases, you can get a cell phone signal almost immediately outside the base that was a protected area.
    
    So there's lots of things that industry can do and some of those things need to come out and, ultimately, find their way into the coordination procedures that come out of this.  So I think there's a lot that can be started without necessarily waiting for that.
    
    We do have the data that was provided through CSMAC before.  On the other hand, if that's as far as we can go with the characterization, once again, we're going to end up with fairly large areas.  Okay.
    
    In some cases, for instance, on the airborne side, one of the biggest issues is going to be looking at the mismatch between the bandwidth you're looking at, the bandwidth that's being emitted, the timing of it, the distance away, and so on.
    
    We may find that you're able to reach conclusions on the potential impact in the industry through these measurements, and so on, to get a good idea of whether that's something that you can tolerate.
    
    And a lot of what we're looking at here on the industry side, we believe and hope, is that the current technologies are much more tolerant than past technologies, and that's part of what we're going to be looking to see.
    
    Member Gibson:  Yes, it's Mark Gibson again.  I've been listening to what Kevin, and Charlie, and others have said, it reminds me, going back to, you know, the '80s or '90s when we did work at sharing between PCS and microwave, we only really had one paradigm, that being microwave systems and a class of mobile systems.
    
    As we moved into the next paradigm, which is AWS, sharing with federal systems, and we had a guidance document which was Bulletin 10, TSB 10F.  I think what we're going to find out of this effort is more guidance documents.
    
    And so it will be worthwhile to ensure, and I think you've done this, that the agencies or industry associations that hold those guidance documents, like TIA and others, are part of this process.
    
    So as those documents need to be updated to entrench this and parameterize these discussions going forward can be done, because that's really what made it possible to affect sharing in a commercial process through sharing tools, and analyses, and whatnot, you know, to make it work.
    
    You know, because a lot of the discussion we had up front was heuristic and theoretical.  It really was when we put that stuff into sharing tools and software that it became workable.  So I suspect you do have TIA and whatnot involved in that.
    
    So I think that a separate effort will need to be to identify the standards as it relates to the interplay between these systems and get that, you know, memorialized.
    
    Chair Fontes:  Are there other questions?  Karl?
    
    Mr. Nebbia:  Are you asking if I have another question?
    
    Chair Fontes:  Yes.  Any questions of Karl, then I want to find out if you have any last-minute comments.  Great.  I think the questions that Charlie raised and Michael raised are important questions to at least consider to begin this process.
    
    I think by addressing those types of questions, we will eliminate a lot of the possibilities of conflicts coming out of the report based on differing assumptions going in to the development of report.
    
    So we will, I'm sure, have an opportunity to follow up in trying to address the questions that were raised today.  I appreciate the discussion that followed Karl's presentation, because I think it actually raised some very valid helpful constructive points, so hats off.
    
    As Karl had this deja vu moment of sharing a tent with a Sergeant, I had a deja vu moment of WRC-95 when the United States is getting a little bit of slack from just about every country in the world with the exception of one.
    
    And we had a special meeting, kind of, in the sidebar of the conference center and everybody spent two hours just, basically, criticizing the United States and the positions that it's taken, and so forth, and so forth.
    
    And so when it came to my turn as the United States' representative at the meeting, I just said, well, thank you very much for identifying the issues, but, you know, I don't know of any group in the world that's gathered at one time that's better capable of addressing the issues that have been raised.
    
    So why don't we roll up our sleeves and work to resolve and address the issues?  You remember these discussions very well.  And I think that this is a great opportunity that we have, for many years we've been talking about the opportunities to better share government spectrum, re-allocation of spectrum, and so forth.
    
    I think the report that was presented was a very comprehensive report that is so inclusive of potential solutions for sharing, re-allocation, and so forth, and it doesn't deal just with a particular slice of a band.
    
    And I think this is a great opportunity that all of us, and those who will be participating in the working groups, have to roll up their sleeves and to do something that we really haven't achieved in a long time, and that is, trying to find solutions that will benefit both government and commercial entities.
    
    And I think this is a step in the right direction.  I appreciate Karl working over the weekend to, kind of, pull together this, just kidding, proposal.  We'd been having conversations about this earlier.
    
    And so I encourage folks to actively engage in these working groups, thank those who are already stepping up to do some of the work and their responsibilities.  And so, again, thank you, and thank you, Karl, for that presentation.
    
    Mr. Nebbia:  Can I just --
    
    Chair Fontes:  Sure.
    
    Mr. Nebbia:  So in closing, what I would appreciate is if you are interested in being the liaison for one of these groups, and once again, it's critical that we have a CSMAC member on each of the groups, if you could, please, either see me after the meetings here, I'll be around for a little while, or send an email to Bruce Washington and say, you know, you would like to do that, and which group you would like to do that for.
    
    And if you would generally like to participate so we can start building the contact list for the groups, if you could provide Bruce, once again, that you are interested in these specific working groups, then we'll begin to build that contact group and, you know, start setting them up.
    
    Chair Fontes:  Great.  I'd just like to go over a couple of other things.  First off, since we last met, the search for 500 MHZ committee, the co-chairs, Karl and Gary, Gary has resigned, as we all know.  He's taken the position at the FCC.  All of us appreciate the work that Gary has done.  I know Karl appreciates the opportunity to have worked with him.
    
    And so, you know, we wish Gary the best of luck at the FCC, and it's a great addition to the commission that Gary's rejoined them.
    
    Next, there was a question raised earlier about the other committees that are not on hiatus, so to speak, and I'd just like to turn it over to the committee chairs for a second to see what additional work and what plans are, and we're going to do it in a, kind of, reverse order.  So, Brian, do you want to chat a little bit?
    
    Mark, do you want to chat a little bit?
    
    Member Gibson:  Well, what we did from the last working group discussion, the one in Stanford, is, we began to look at the comments you had on the recommendations we made, because I think the only ones that were on the table at the time were the ones we made before that meeting, which I think were the ones in November.
    
    So we put together a document that, for the most part, the working group, I think, has approved, that addresses the working group's comments to your comments.  You know, so we're ready to let that go, but, you know, I think what we want to do is wait until, you know, we have a meeting.
    
    So we'll go through the process, but we have that.  Then there is the work plan we had.  We were working on the next question, which eludes me right now, but we have begun working on that.  And I think it was dealing with how you, you know, work with systems you don't have data on, or something like that.
    
    And we've gotten some traction on that and, you know, if we need to, we can present at the next meeting as well.  But I think if many of us are going to want to participate in these working groups, and so, I guess the question I had before was, you know, do you want both in July or, you know, how shall we proceed?
    
    Chair Fontes:  Well, clearly, I think the report that's nearly done --
    
    Member Gibson:  Yes.
    
    Chair Fontes:  -- we can present that in July.  And in terms of the time schedules that Karl has presented, and I know that they're coming upon us already, we may want to also take a look at the functions of these groups and see how many of those working group members are actively engaged in the others, and then, at that point, judge whether or not all of these are put on hiatus.
    
    Member Tramont:  Might I propose that -- Bryan Tramont, sorry.  Might I propose that the committee co-chairs come back to you within the next ten days or something with a proposal about what they think they should wrap up come July and then what they think is still viable to keep going on or not, because it may be very distinct to each committee that certain things are in different parts of the work plan.
    
    And then Karl and his team can give us feedback on whether there's something that we're working on that should really get done that needs to get done by September.
    
    Chair Fontes:  Right.  And some of the work is in progress already.
    
    Member Tramont:  Yes, exactly.
    
    Chair Fontes:  So we may be able to just wrap that up.
    
    Member Gibson:  And one point I had to what Bryan was saying is that, we might that, through the work we're doing with the new work plan, we may circle some of, at least, the late issues back into the, you know, various systems and services where we can have them.  Implicit in some of that is going to be the availability of data.
    
    I don't know that it's going to be a grand scale, but I think we can at least tee some of that up.  I don't think it, you know, meshes exactly, but if we can kill two birds with one allocation.
    
    Chair Fontes:  I also appreciate the process where we worked on specific questions.  I think it allowed responses to those questions to move forward in a timely fashion rather than waiting to an end report.  So I think that has been a very productive model for us to follow.
    
    Are there any questions on the remaining committees?  Mike, do you have any comments on what you're going to be talking about with respect to being licensed?
    
    Member Calabrese:  I don't know about comments, but, you know, I think what Bryan suggested would be good, that we need to huddle.  You know, at the Stanford meeting, we were complete on the initial interference questions that we had gone through.  We had some things in mind to move on to, but we also had wanted to consult, I think again, with Karl about what would be most productive in the current context.
    
    So I think Janice and I, at a minimum, need to huddle about that and probably consult with Karl.'''
print(summarizeText(story))

f = open("")
