from google.cloud import bigquery
import os
from pypdf import PdfReader

# Construct a BigQuery client object.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/prakou/Downloads/translation-llm-86e95fb15e10.json'
client = bigquery.Client()

table_id = "translation-llm.engati_test.test_table"

reader = PdfReader('/Users/prakou/Downloads/Courses in Firki (1).pdf')

row = """{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "abcdefghi"
        }
      ]
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "Translate the text into english if the text is not english and if the text is english then keep it same."
      }
    ]
  }
}"""

rows_to_insert = []

for page in reader.pages:
    rows_to_insert.append({"request": row.replace("abcdefghi", page.extract_text().replace('"', '').replace("\\n", " ").replace("\n", " ").replace("  ", " "))})

reader = PdfReader('/Users/prakou/Downloads/hindi.pdf')
for page in reader.pages:
    rows_to_insert.append({"request": row.replace("abcdefghi", page.extract_text().replace('"', '').replace("\\n", " ").replace("\n", " ").replace("  ", " "))})



# # rows.append(row)
# rows_to_insert = [
#     {"request": """{
#   "contents": [
#     {
#       "role": "user",
#       "parts": [
#         {
#           "text": "CourseName:5EMethodsofInstructionandPlanningCourseLink:5EMethodsofInstructionandPlanning-https://firki.co/course/view.php?id=24 CourseOverview: Delveintoacreative,hands-onapproachtoteachingwiththe5EMethodsofInstructionandPlanningcourse.Thiscourseinviteseducatorsandplannerstoexplorearefreshingmethodoflessonplanningbasedontheconstructivistphilosophy,wherelearnersareactiveparticipantsintheireducationaljourney.You’llbeintroducedtoastructured,step-by-stepinstructionalframeworkthatplacesemphasisonengagement,exploration,andevaluation,allowingstudentstogaindeeperinsightsthroughactivelearning. WhyTakeThisCourse? Educationisconstantlyevolving,andthiscourseprovidesanopportunitytorethinkhowyouapproachteaching.You’llbeginbyexaminingtheconstructivistapproachtolearning,whichencouragesstudentstobuildknowledgethroughexperienceandinquiry.Fromthere,you’lldiscoverthe5Emethod—asystematicmodeldesignedtomakelessonsmoreinteractive,student-centered,andeffective.Bytheend,you’llhavetheskillstocreateyourownlessonplanusingthispowerfulmethod. WhatYouWillLearn: ● Gainafoundationalunderstandingoftheconstructivistlearningapproach.● Explorethefivephasesofthe5Einstructionalmodelandhoweachphasecanelevatestudentlearning.● Developapersonalized5Elessonplan,enablingyoutoapplythisinnovativemethodinyourclassroomorlearningenvironment. WhoIsThisCourseFor? Whetheryou’reaneducatorlookingfornewstrategies,acurriculumplannerseekingamoreinteractiveapproach,orsomeonepassionateabouteducationalmethods,thiscourseisperfectforyou.The5Emethodisadaptableacrossdifferentsubjectsandteachingstyles,makingitaversatiletoolforanyoneeagertoenrichtheirinstructionaltechniques. Joinusandtransformthewayyouteachwiththe5EMethodsofInstructionandPlanningcourse!"
#         }
#       ]
#     }
#   ],
#   "system_instruction": {
#     "parts": [
#       {
#         "text": "Translate the text into english if the text is not english and if the text is english then keep it same."
#       }
#     ]
#   }
# }"""
#      }
# ]


errors = client.insert_rows_json(
    table_id, rows_to_insert, row_ids=[None] * len(rows_to_insert)
)
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))
