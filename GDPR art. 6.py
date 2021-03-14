#!/usr/bin/env python
# coding: utf-8

# In[ ]:


complianttext = "The processing of data seems to be compliant with GDPR art. 6. Be aware that this is not a definite answer, and that individual dissimilarities between students may occur. Please note that processing for a purpose other than that for which the personal data have been collected requires compatability with the purpose for which the personal data are initially collected. To decide if there is such compability the university should take into account any link between the purposes for which the personal data have been collected and the purposes of the intended further processing; the context in which the personal data have been collected, in particular regarding the relationship between data subjects and the controller; the nature of the personal data, in particular whether special categories of personal data are processed, pursuant to Article 9, or whether personal data related to criminal convictions and offences are processed, pursuant to Article 10; the possible consequences of the intended further processing for data subjects; and the existence of appropriate safeguards, which may include encryption or pseudonymisation."
noncomplianttext = "Unfortunately, the processing of data does not seem to be compliant with GDPR art. 6. Be aware that this is not a definite answer, and that individual dissimilarities between students may occur. Please note that processing for a purpose other than that for which the personal data have been collected requires compatability with the purpose for which the personal data are initially collected. To decide if there is such compability the university should take into account any link between the purposes for which the personal data have been collected and the purposes of the intended further processing; the context in which the personal data have been collected, in particular regarding the relationship between data subjects and the controller; the nature of the personal data, in particular whether special categories of personal data are processed, pursuant to Article 9, or whether personal data related to criminal convictions and offences are processed, pursuant to Article 10; the possible consequences of the intended further processing for data subjects; and the existence of appropriate safeguards, which may include encryption or pseudonymisation."

answer_user = input("Has the students given consent to the processing of their personal data for the purpose of monitoring of dropout risk? ")
if answer_user == "yes" or "Yes":
    print(complianttext)
elif answer_user == "no" or "No":
    answer_user2 = input("Is the processing of data necessary for the performance of a contract to which the students is party? ")
    if answer_user2 == "yes" or "Yes":
        print(complianttext)
    elif answer_user2 == "no" or "No":
        answer_user3 = input("Is the processing of data necessary for compliance with a legal obligation to which the university is subject? ")
        if answer_user3 == "yes" or "Yes":
            answer_user8 = input("Is the basis for the processing of data referred laid down by either Union law or Member State law to which the university is subject? ")
            if answer_user8 == "yes" or "Yes":
                answer_user9 = input("Is the purpose of the processing of data determined in that legal basis, and does the Union or the Member State law meet an objective of public interest and be proportionate to the legitimate aim pursued? ")
                if answer_user9 == "yes" or "Yes":
                    print(complianttext)
        elif answer_user3 or answer_user8 or answer_user9  == "no" or "No":
            answer_user4 = input("Is the processing of data necessary in order to protect the vital interests of the students or of another natural person? ")
            if answer_user4 == "yes" or "Yes":
                print(complianttext)
            elif answer_user4  == "no" or "No":
                answer_user5 = input("Is the processing of data necessary for the performance of a task carried out in the public interest or in the exercise of official authority the university has an obligation to perform? ")
                if answer_user5 == "yes" or "Yes":
                    answer_user10 = input("Is the basis for the processing of data referred laid down by either Union law or Member State law to which the university is subject? ")
                    if answer_user10 == "yes" or "Yes":
                        answer_user11 = input("Is the purpose of the processing of data determined in that legal basis or necessary for the performance of a task carried out in the public interest or in the exercise of official authority the university has an obligation to perform? ")
                        if answer_user11 == "yes" or "Yes":
                            answer_user12 = input("Does the Union or the Member State law meet an objective of public interest and be proportionate to the legitimate aim pursued? ")
                            if answer_user12 == "yes" or "Yes":
                                print(complianttext)
                    elif answer_user10 or answer_user11 or answer_user12 == "no" or "No":
                        answer_user7 = input("Is the processing of data necessary for the purposes of the legitimate interests pursued by the university or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the students which require protection of personal data? ")
                elif answer_user5 == "no" or "No":
                    answer_user6 = input("Is the university a public authority, and is the data processing carried out in the performance of the university's tasks? ")
                    if answer_user6 == "no" or "No":
                        print(complianttext)
                    elif answer_user6 == "yes" or "Yes":
                        answer_user7 = input("Is the processing of data necessary for the purposes of the legitimate interests pursued by the university or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the students which require protection of personal data? ")
                        if answer_user7 == "yes" or "Yes":
                            print(complianttext)
                        elif answer_user7 == "no" or "No":
                            print(noncomplianttext)
else:
    print("I do not understand. Please type 'yes' or 'no', please.")


# In[ ]:




