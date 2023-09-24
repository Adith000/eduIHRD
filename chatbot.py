import pandas as pd
import random

data = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi there", "How are you", "Is anyone there?", "Hey", "Hola", "Hello", "Hi","Good day","How r u"],
            "responses": ["Hello", "Good to see you again", "Hi there, how can I help?"],
            "context": [""]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"],
            "responses": ["See you!", "Have a nice day", "Bye! Come back again soon."],
            "context": [""]
        },
        {
            "tag": "thanks",
            "patterns": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"],
            "responses": ["My pleasure", "You're Welcome"],
            "context": [""]
        },
        {
            "tag": "ihrd_info",
            "patterns": ["What is IHRD?", "Tell me about IHRD", "IHRD information", "About IHRD","IHRD info", "Give me an overview of IHRD",
                         "I'd like to learn about IHRD",
                         "Could you provide some insights on IHRD?",
                         "Share some details regarding IHRD",
                         "What can you tell me about IHRD?",
                         "Tell me more about IHRD's mission",
                         "IHRD's purpose?",
                         "Educate me about IHRD",
                         "What's the primary focus of IHRD?",
                         "Can you describe IHRD's goals?",
                         "Tell me what IHRD offers"],
            "responses": [
                "IHRD, or Institute of Human Resources Development, is an organization dedicated to providing quality education and training programs.",
                "IHRD stands for Institute of Human Resources Development, which offers various educational and skill development programs.",
                "IHRD is an institution focused on human resource development through education and training initiatives."
            ],
            "context": [""]
        },
         {
            "tag": "Adoor Faculty",
            "patterns": ["Tell me about the professors at College Of Engineering Adoor.",
                        "Can you provide information about the teaching staff of College Of Engineering Adoor?",
                        "Who are the faculty members here at College Of Engineering Adoor?",
                        "Give me details about the academic staff of College Of Engineering Adoor.",
                        "I'd like to learn more about the professors of College Of Engineering Adoor.",
                        "What can you tell me about the teachers at College Of Engineering Adoor?",
                        "Who makes up the faculty at College Of Engineering Adoor?",
                        "Tell me about the instructors of College Of Engineering Adoor.",
                        "Share some insights into the faculty members of College Of Engineering Adoor.",
                        "Can you list the names of the professors of College Of Engineering Adoor?"],
            "responses": [" Mechanical Department\n\n"
                            "HOD : Dr. Suresh Kumar.N\n"
                            "Associate Professor\n"
                            "Mechanical Engineering\n\n"

                            "Faculty\n\n"

                            "Dr. K Sunil Kumar\n"
                            "Designation:- Professor (Principal incharge)\n"
                            "Qualification:-M. Tech, Ph. D\n"
                            "Experience:-32 Yrs\n\n"

                            "Dr. Suresh Kumar N\n"
                            "Designation :- Associate Professor\n"
                            "Qualification:- M. Tech, Ph.D\n"
                            "Experience:- 26 Yrs\n\n"

                            "Dr. Jose Mathew\n"
                            "Designation:-Associate Professor\n"
                            "Qualification:- M. Tech, Ph. D\n"
                            "Experience:-23 Yrs\n\n"

                            "Dr. Binulal B R\n"
                            "Designation:-Associate Professor\n"
                            "Qualification:-M. Tech, Ph. D\n"
                            "Experience:- 22 Yrs\n\n"

                            "Dr. Venkitaraj K P\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M. Tech, Ph. D\n"
                            "Experience:- 23 Yrs\n\n"

                            "Sri. Revikumar Thampi V R\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:-M. Tech\n"
                            "Experience:-22 Yrs\n\n"

                            "Sri. Baiju V\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:-M. Tech\n"
                            "Experience:- 21 Yrs\n\n"

                            "Sri. John Seprian Fernandez S\n"
                            "Designation:-Assistant Professor\n"
                            "Qualification:-B. Tech\n"
                            "Experience:-16 Yrs\n\n"

                            "Sri. Madhu A K\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:-M. Tech\n"
                            "Experience:-16 Yrs\n\n"

                            "Sri. Sanjay Raj\n"
                            "Designation:-Assistant Professor\n"
                            "Qualification:-M. Tech\n"
                            "Experience:-15 Yrs\n\n"

                            "Staff\n\n"

                            "Girish G\n"
                            "Designation:- Demonstrator\n\n"

                            "Manoj Kumar V\n"
                            "Designation:- Workshop Instructor\n\n"

                            "Arya Aravind\n"
                            "Designation:- Workshop Instructor\n\n"

                            "S Gopalan\n"
                            "Designation:- Tradesman\n\n"

                            "Retheesh R\n"
                            "Designation:- Tradesman\n\n"

                            "Electronics and Communication Engineering\n\n"

                            "HOD : Dr. Jayachandran E S\n"
                            "Designation Professor and Head\n\n"

                            "Faculty\n\n"

                            "Rajesh M S\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Preethymol Silastin\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Reji Thankachan\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Deebu U S\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Shan N\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Girija M G\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Harikumar T\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Jaferkhan P\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Sobhi Raj N\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Deepa T R\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M Tech\n\n"

                            "Staff\n\n"

                            "Ashna Abu\n"
                            "Designation:- Workshop instructor\n"
                            "Qualification:- Diploma\n\n"

                            "Thushara U S\n"
                            "Designation:- Workshop Instructor\n"
                            "Qualification:- Diploma\n\n"

                            "Ramjith P B\n"
                            "Designation:- Tradesman\n"
                            "Qualification:- ITI\n\n"

                            "Electrical and Electronics Engineering\n\n"

                            "HOD : Dr. John George\n"
                            "Designation: Professor\n\n"

                            "Faculty\n\n"

                            "Dr. John George\n"
                            "Designation:- Professor\n"
                            "Qualification:- M.tech, Ph.D\n"
                            "Experience:- 24\n\n"

                            "Dr. Sreeja P\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M.tech, Ph.D\n"
                            "Experience:- 24\n\n"

                            "Sri. Renjith Kumar D\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M.tech\n"
                            "Experience:- 23\n\n"

                            "Sri. Jain George\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M.tech\n"
                            "Experience:- 12\n\n"

                            "Smt. Anu P\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M.tech\n"
                            "Experience:- 8\n\n"

                            "Smt. Reeja Thankachan\n"
                            "Designation:- 	Assistant Professor\n"
                            "Qualification:- M.tech\n"
                            "Experience:- 4\n\n"

                            "Smt. Anjali S\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M.tech\n"
                            "Experience:- 10\n\n"

                            "Smt. Sumi Soman\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M.tech\n"
                            "Experience:- 4.5\n\n"

                            "Smt. Sujitha Surendran\n"
                            "Designation:- Assistant Professor\n"
                            "Qualification:- M.tech\n"
                            "Experience:- 4\n\n"

                            "Staff\n\n"

                            "Biju K G\n"
                            "Designation:- Trade Instructor Gr.II\n\n"

                            "Vinod Joy\n"
                            "Designation:- Trade Instructor Gr.II\n\n"

                            "Chinchu P.R\n"
                            "Designation:- Workshop Instructor\n\n"

                            "Lijo Daniel\n"
                            "Designation:- Tradesman\n\n"

                            "Computer Science and Engineering\n\n"

                            "HOD : Shibu J\n"
                            "Designation Associate Professor\n\n"

                            "Faculty\n\n"

                            "Mr Shibu J\n"
                            "Designation:- Associate Professor\n\n"

                            "Mr Vinod P R\n"
                            "Designation:- Assistant Professor\n\n"

                            "Ms Girija V R\n"
                            "Designation:- Assistant Professor\n\n"

                            "Mr Jayaram K\n"
                            "Designation:- Assistant Professor\n\n"

                            "Mrs Sreedeepa H S\n"
                            "Designation:- Assistant Professor\n\n"

                            "Mrs Manju J\n"
                            "Designation:- Assistant Professor\n\n"

                            "Ms Honey M\n"
                            "Designation:- Assistant Professor\n\n"

                            "Ms Keerthana R\n"
                            "Designation:- Assistant Professor\n\n"

                            "Mrs Jyothi Vijayan\n"
                            "Designation:- Assistant Professor\n\n"

                            "Staff\n\n"

                            "Sreeja Krishnan\n"
                            "Designation:-Computer Programmer\n\n"

                            "Arya A\n"
                            "Designation:-Computer Programmer\n\n"

                            "Samzeena S\n"
                            "Designation:-Workshop Instructor\n\n"

                            "Nisha Chandran\n"
                            "Designation:-	Workshop Instructor\n\n"

                            "Department of Applied Sciences\n\n"
                            "HOD : MONI P JOHN\n"
                            "Designation:- Associate Professor in Chemistry\n\n"

                            "FACULTY\n\n"

                            "Dr Ajitha P S\n"
                            "Designation:- Associate Professor\n\n"

                            "Mr Rubon L\n"
                            "Designation:-  Associate Professor\n\n"

                            "Mrs Sheeba Joseph\n"
                            "Designation:- Associate Professor\n\n"

                            "Mrs Shiji KV\n"
                            "Designation:- Associate Professor\n\n"

                            "Mrs Rethee Kumari S\n"
                            "Designation:- Assistant Professor\n\n"

                            "Mrs Thazneem Ansari\n"
                            "Designation:- Assistant Professor\n\n"

                            "Mrs Nikhitha Muhammad\n"
                            "Designation:- Assistant Professor\n\n"],
            "context": [""]
        },
         {
            "tag": "Adoor mech",
            "patterns": ["Tell me about the professors in the mechanical department of College Of Engineering Adoor.",
                        "Who are the faculty members in the mechanical engineering department of College Of Engineering Adoor?",
                        "Can you provide information on the teaching staff in mechanical engineering at College Of Engineering Adoor?",
                        "Give me details about the mechanical department instructors of College Of Engineering Adoor.",
                        "I'd like to learn more about the professors teaching mechanical engineering at College Of Engineering Adoor.",
                        "What can you tell me about the mechanical engineering faculty of College Of Engineering Adoor?",
                        "Who makes up the staff in the mechanical department of College Of Engineering Adoor?",
                        "Tell me about the mechanical engineering instructors of College Of Engineering Adoor.",
                        "Share some insights into the mechanical department staff of College Of Engineering Adoor.",
                        "Can you list the names of the professors in mechanical engineering at College Of Engineering Adoor?"],
            "responses": [" Mechanical Department\n\n"
                        "HOD : Dr. Suresh Kumar.N\n"
                        "Associate Professor\n"
                        "Mechanical Engineering\n\n"

                        "Faculty\n\n"

                        "Dr. K Sunil Kumar\n"
                        "Designation:- Professor (Principal incharge)\n"
                        "Qualification:-M. Tech, Ph. D\n"
                        "Experience:-32 Yrs\n\n"

                        "Dr. Suresh Kumar N\n"
                        "Designation :- Associate Professor\n"
                        "Qualification:- M. Tech, Ph.\n"
                        "Experience:- 26 Yrs\n\n"

                        "Dr. Jose Mathew\n"
                        "Designation:-Associate Professor\n"
                        "Qualification:- M. Tech, Ph. D\n"
                        "Experience:-23 Yrs\n\n"

                        "Dr. Binulal B R\n"
                        "Designation:-Associate Professor\n"
                        "Qualification:-M. Tech, Ph. D\n"
                        "Experience:- 22 Yrs\n\n"

                        "Dr. Venkitaraj K P\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M. Tech, Ph. D\n"
                        "Experience:- 23 Yrs\n\n"

                        "Sri. Revikumar Thampi V R\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:-M. Tech\n"
                        "Experience:-22 Yrs\n\n"

                        "Sri. Baiju V\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:-M. Tech\n"
                        "Experience:- 21 Yrs\n\n"

                        "Sri. John Seprian Fernandez S\n"
                        "Designation:-Assistant Professor\n"
                        "Qualification:-B. Tech\n"
                        "Experience:-16 Yrs\n\n"

                        "Sri. Madhu A K\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:-M. Tech\n"
                        "Experience:-16 Yrs\n\n"

                        "Sri. Sanjay Raj\n"
                        "Designation:-Assistant Professor\n"
                        "Qualification:-M. Tech\n"
                        "Experience:-15 Yrs\n\n"

                        "Staff\n\n"

                        "Girish G\n"
                        "Designation:- Demonstrator\n\n"

                        "Manoj Kumar V\n"
                        "Designation:- Workshop Instructor\n\n"

                        "Arya Aravind\n"
                        "Designation:- Workshop Instructor\n\n"

                        "S Gopalan\n"
                        "Designation:- Tradesman\n\n"

                        "Retheesh R\n"
                        "Designation:- Tradesman\n\n"],
            "context": [""]
         },
         {
            "tag": "Adoor ec",
            "patterns": ["Tell me about the professors in the Electronics and Communication Engineering department of College Of Engineering Adoor.",
                        "Who are the faculty members in the Electronics and Communication Engineering department of College Of Engineering Adoor?",
                        "Can you provide information on the teaching staff in Electronics and Communication Engineering at College Of Engineering Adoor?",
                        "Give me details about the Electronics and Communication Engineering department instructors of College Of Engineering Adoor.",
                        "I'd like to learn more about the professors teaching Electronics and Communication Engineering at College Of Engineering Adoor.",
                        "What can you tell me about the Electronics and Communication Engineering faculty of College Of Engineering Adoor?",
                        "Who makes up the staff in the Electronics and Communication Engineering of College Of Engineering Adoor?",
                        "Tell me about the Electronics and Communication Engineering instructors of College Of Engineering Adoor.",
                        "Share some insights into the Electronics and Communication Engineering staff of College Of Engineering Adoor.",
                        "Can you list the names of the professors in Electronics and Communication Engineering at College Of Engineering Adoor?"],
            "responses": ["Electronics and Communication Engineering\n\n"

                        "HOD : Dr. Jayachandran E S\n"
                        "Designation Professor and Head\n\n"

                        "Faculty\n\n"

                        "Rajesh M S\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Preethymol Silastin\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Reji Thankachan\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Deebu U S\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Shan N\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Girija M G\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Harikumar T\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Jaferkhan P\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Sobhi Raj N\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Deepa T R\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M Tech\n\n"

                        "Staff\n\n"

                        "Ashna Abu\n"
                        "Designation:- Workshop instructor\n"
                        "Qualification:- Diploma\n\n"

                        "Thushara U S\n"
                        "Designation:- Workshop Instructor\n"
                        "Qualification:- Diploma\n\n"

                        "Ramjith P B\n"
                        "Designation:- Tradesman\n"
                        "Qualification:- ITI\n\n"],
            "context": [""]
         },
         {
            "tag": "Adoor eee ",
            "patterns": ["Tell me about the professors in the Electrical and Electronics Engineering department of College Of Engineering Adoor.",
                        "Who are the faculty members in the Electrical and Electronics Engineering department of College Of Engineering Adoor?",
                        "Can you provide information on the teaching staff in Electrical and Electronics Engineering at College Of Engineering Adoor?",
                        "Give me details about the Electrical and Electronics Engineering department instructors of College Of Engineering Adoor.",
                        "I'd like to learn more about the professors teaching Electrical and Electronics Engineering at College Of Engineering Adoor.",
                        "What can you tell me about the Electrical and Electronics Engineering faculty of College Of Engineering Adoor?",
                        "Who makes up the staff in the Electrical and Electronics Engineering of College Of Engineering Adoor?",
                        "Tell me about the Electrical and Electronics Engineering instructors of College Of Engineering Adoor.",
                        "Share some insights into the Electrical and Electronics Engineering staff of College Of Engineering Adoor.",
                        "Can you list the names of the professors in Electrical and Electronics Engineering at College Of Engineering Adoor?"],
            "responses": ["Electrical and Electronics Engineering\n\n"

                        "HOD : Dr. John George\n"
                        "Designation: Professor\n\n"

                        "Faculty\n\n"

                        "Dr. John George\n"
                        "Designation:- Professor\n"
                        "Qualification:- M.tech, Ph.D\n"
                        "Experience:- 24\n\n"

                        "Dr. Sreeja P\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech, Ph.D\n"
                        "Experience:- 24\n\n"

                        "Sri. Renjith Kumar D\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 23\n\n"

                        "Sri. Jain George\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 12\n\n"

                        "Smt. Anu P\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 8\n\n"

                        "Smt. Reeja Thankachan\n"
                        "Designation:- 	Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 4\n\n"

                        "Smt. Anjali S\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 10\n\n"

                        "Smt. Sumi Soman\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 4.5\n\n"

                        "Smt. Sujitha Surendran\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 4\n\n"

                        "Staff\n\n"

                        "Biju K G\n"
                        "Designation:- Trade Instructor Gr.II\n\n"

                        "Vinod Joy\n"
                        "Designation:- Trade Instructor Gr.II\n\n"

                        "Chinchu P.R\n"
                        "Designation:- Workshop Instructor\n\n"

                        "Lijo Daniel\n"
                        "Designation:- Tradesman\n\n""Electrical and Electronics Engineering\n\n"

                        "HOD : Dr. John George\n"
                        "Designation: Professor\n\n"

                        "Faculty\n\n"

                        "Dr. John George\n"
                        "Designation:- Professor\n"
                        "Qualification:- M.tech, Ph.D\n"
                        "Experience:- 24\n\n"

                        "Dr. Sreeja P\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech, Ph.D\n"
                        "Experience:- 24\n\n"

                        "Sri. Renjith Kumar D\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 23\n\n"

                        "Sri. Jain George\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 12\n\n"

                        "Smt. Anu P\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 8\n\n"

                        "Smt. Reeja Thankachan\n"
                        "Designation:- 	Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 4\n\n"

                        "Smt. Anjali S\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 10\n\n"

                        "Smt. Sumi Soman\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 4.5\n\n"

                        "Smt. Sujitha Surendran\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.tech\n"
                        "Experience:- 4\n\n"

                        "Staff\n\n"

                        "Biju K G\n"
                        "Designation:- Trade Instructor Gr.II\n\n"

                        "Vinod Joy\n"
                        "Designation:- Trade Instructor Gr.II\n\n"

                        "Chinchu P.R\n"
                        "Designation:- Workshop Instructor\n\n"

                        "Lijo Daniel\n"
                        "Designation:- Tradesman\n\n"],
            "context": [""]
         },
         {
            "tag": "Adoor cse ",
            "patterns": ["Tell me about the professors in the Computer Science and Engineering department of Adoor.",
                        "Who are the faculty members in the Computer Science and Engineering department of College Of Engineering Adoor?",
                        "Can you provide information on the teaching staff in Computer Science and Engineering at College Of Engineering Adoor?",
                        "Give me details about the Computer Science and Engineering department instructors of College Of Engineering Adoor.",
                        "I'd like to learn more about the professors teaching Computer Science and Engineering at College Of Engineering Adoor.",
                        "What can you tell me about the Computer Science and Engineering faculty of College Of Engineering Adoor?",
                        "Who makes up the staff in the Computer Science and Engineering of College Of Engineering Adoor?",
                        "Tell me about the Computer Science and Engineering instructors of College Of Engineering Adoor.",
                        "Share some insights into the Computer Science and Engineering staff of College Of Engineering Adoor.",
                        "Can you list the names of the professors in Computer Science and Engineering at College Of Engineering Adoor?"],
            "responses": ["Computer Science and Engineering\n\n"

                        "HOD : Shibu J\n"
                        "Designation Associate Professor\n\n"

                        "Faculty\n\n"

                        "Mr Shibu J\n"
                        "Designation:- Associate Professor\n\n"

                        "Mr Vinod P R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Ms Girija V R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mr Jayaram K\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs Sreedeepa H S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs Manju J\n"
                        "Designation:- Assistant Professor\n\n"

                        "Ms Honey M\n"
                        "Designation:- Assistant Professor\n\n"

                        "Ms Keerthana R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs Jyothi Vijayan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Staff\n\n"

                        "Sreeja Krishnan\n"
                        "Designation:-Computer Programmer\n\n"

                        "Arya A\n"
                        "Designation:-Computer Programmer\n\n"

                        "Samzeena S\n"
                        "Designation:-Workshop Instructor\n\n"

                        "Nisha Chandran\n"
                        "Designation:-	Workshop Instructor\n\n"

                        "Department of Applied Sciences\n\n"
                        "HOD : MONI P JOHN\n"
                        "Designation:- Associate Professor in Chemistry\n\n"

                        "FACULTY\n\n"

                        "Dr AJITHA P S\n"
                        "Designation:- Associate Professor\n\n"

                        "Mr RUBON L\n"
                        "Designation:-  Associate Professor\n\n"

                        "Mrs SHEEBA JOSEPH\n"
                        "Designation:- Associate Professor\n\n"

                        "Mrs SHIJI KV\n"
                        "Designation:- Associate Professor\n\n"

                        "Mrs RETHEE KUMARY S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs THAZNEEM ANSARI\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs NIKHITHA MUHAMMAD\n"
                        "Designation:- Assistant Professor\n\n"],
            "context": [""]
         },
         {
            "tag": "Adoor hod ",
            "patterns": ["I'd like to know who the HODs of the College Of Engineering Adoor.",
                        "Can you share the HODs' names for the departments of College Of Engineering Adoor ?",
                        "Can you tell me about the  department heads of College Of Engineering Adoor?",
                        "Could you give me an overview of the department heads of College Of Engineering Adoor?",
                        "Tell me about the leadership in the departments of College Of Engineering Adoor.",
                        "Provide information about the Heads of Departments in theCollege Of Engineering Adoor."],
            "responses": [" Mechanical Department\n\n"
                            "HOD : Dr. Suresh Kumar.N\n"
                            "Associate Professor\n"
                            "Mechanical Engineering\n\n"


                            "Electronics and Communication Engineering Department\n\n"
                            "HOD : Dr. Jayachandran E S\n"
                            "Designation Professor and Head\n\n"


                            "Electrical and Electronics Engineering\n\n"
                            "HOD : Dr. John George\n"
                            "Designation: Professor\n\n"


                            "Computer Science and Engineering\n\n"
                            "HOD : Shibu J\n"
                            "Designation Associate Professor\n\n"],
            "context": [""]
         },
         {
            "tag": "Adoor Courses",
            "patterns": ["What courses are offered at College Of Engineering Adoor?" ,
                         "Tell me about the programs available at College Of Engineering Adoor" ,
                         "Can you list the available courses at College Of Engineering Adoor?" ,
                         "What are the academic programs at College Of Engineering Adoor?",
                         "Which degrees can I pursue at College Of Engineering Adoor?",
                         "Give me information on the available majors at College Of Engineering Adoor",
                         "What fields of study are available at College Of Engineering Adoor?",
                         "Tell me about the curriculum options provided by College Of Engineering Adoor"],
            "responses": ["M.Tech Courses =\n\n "
                          "Mechanical Enginnering ( Thermal Engineering) : 18 seats per year\n\n"
                          "B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 60 seats per year \n"
                          "Electrical & Electronics Engineering : 60 seats per year \n"
                          "Electronics & Communication Engineering : 60 per year \n"
                          "Mechanical Engineering : 120 per year" ],
            "context": [""]
        },
        {
            "tag": "Contact Adoor",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Adoor?",
                        "I need the contact information of the College Of Engineering Adoor, please.",
                        "How can I get in touch with the College Of Engineering Adoor?","What is the College Of Engineering Adoor phone number?",
                        "Please share the College Of Engineering Adoor email address.",
                        "I'm looking for the address of the College Of Engineering Adoor.","How can I contact the admissions department of the College Of Engineering Adoor?",
                        "I need to reach the financial aid office of College Of Engineering Adoor. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Adoor?","Do College Of Engineering Adoor have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Adoor official website for contact details?","How do I get in touch with the College Of Engineering Adoor for general queries?"],
            "responses":
                ["College of Engineering, Manakala. P.O. Adoor, Pathanamthitta District Kerala State. \nPin : 691 551\n Phone: +91-4734-230640(P) \nPhone: +91-4734-231995(O)\n Mobile : 8547005100 \nE-mail : ceadoor@ihrd.ac.in\n web : www.ceadoor.ihrd.ac.in"],
            "context": [""]
        },
        {
            "tag": "Adoor",
            "patterns": ["Tell me about College Of Engineering Adoor", "College Of Engineering Adoor", "Adoor",
                          "Details about College Of Engineering Adoor"],
            "responses": [
                "Run by IHRD, College of Engineering, Adoor has been the leading technical institution in Kerala since it's venture in 1995. Affiliated to KTU, CEA offers B.Tech in Computer Science & Engineering, Electronics & Communication Engineering, Mechanical Engineering and Electrical & Electronics Engineering Departments, reflecting the modern technological advancements through its updated syllabi. Experienced staff, excellent research facilities and some of the brightest students in the state contribute to the studying environment in the college. Adoor Engineering college seeks to bring out the all-round abilities in the students and instills in them a vision for a better tomorrow"],
            "context": [""]
        },
        {
            "tag": "Attingal Faculty",
            "patterns": ["Tell me about the professors at College Of Engineering Attingal.",
                        "Can you provide information about the teaching staff of College Of Engineering Attingal?",
                        "Who are the faculty members here at College Of Engineering Attingal?",
                        "Give me details about the academic staff of College Of Engineering Attingal.",
                        "I'd like to learn more about the professors of College Of Engineering Attingal.",
                        "What can you tell me about the teachers at College Of Engineering Attingal?",
                        "Who makes up the faculty at College Of Engineering Attingal?",
                        "Tell me about the instructors of College Of Engineering Attingal.",
                        "Share some insights into the faculty members of College Of Engineering Attingal.",
                        "Can you list the names of the professors of College Of Engineering Attingal?"],
            "responses":  [
                              "Computer Science and Engineering\n\n"
                             "Faculty\n\n"
                             "Dr. Suma L S\n"
                             "Designation: ASSISTANT PROFESSOR\n"
                              "Qualification: Ph D\n"
                             "Specialization: N/A\n\n"

                             "Dancy Kurian\n"
                              "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: MTech\n"
                                 "Specialization: N/A\n\n"

                                "Dr. Leena Silvoster M\n"
                                   "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: Ph D\n"
                             "Specialization: N/A\n\n"

                              "Remya R S\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                               "Qualification: M. Tech. PHD thesis submitted\n"
                                 "Specialization: Computer Science and Information Technology (M Tech)\n\n"

                                "Syama S R\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Computer Science and Engineering\n\n"

                                "SHIJINA J SALIM\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.TECH\n"
                                "Specialization: COMPUTER SCIENCE AND ENGINEERING\n\n"

                                "MEENU MOHAN\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech in Computer Science\n"
                                "Specialization: Image Processing\n\n"

                                "ARYA MURALI\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.TECH IN COMPUTER SCIENCE AND ENGINEERING\n"
                                "Specialization: COMPUTER NETWORKS & PROGRAMMING LANGUAGES\n\n"

                                "Shaima Rahim\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: Mtech in Computer Science\n"
                                "Specialization: Digital Image Computing\n\n"

                                "Electrical and Electronics Engineering\n\n"
                                "Faculty\n\n"
                                "Salins S S\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Power Systems\n\n"

                                "Sreejith S\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Power Systems\n\n"

                                "Anjana P\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Power and Energy\n\n"

                                "Vani R\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: VLSI and Embedded System\n\n"

                                "Sneha V L\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Control Systems\n\n"

                                "Aleena B S\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Industrial Drives and Control\n\n"

                                "Neethu R Nair\n"
                                "Designation: ASSISTANT PROFESSOR\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Control and Instrumentation\n\n"

                                "Electronics & Communication Engineering\n\n"
                                "Faculty\n\n"
                                "Dr. Sunil T.T.\n"
                                "Designation: Professor\n"
                                "Qualification: Ph.D.\n"
                                "Specialization: N/A\n\n"

                                "Sudheer Babu P.P\n"
                                "Designation: Assistant Professor\n"
                                "Qualification: M.Tech.\n"
                                "Specialization: Opto Electronics & Laser Technology\n\n"

                                "Sabeena M\n"
                                "Designation: Assistant Professor\n"
                                "Qualification: M.Tech.\n"
                                "Specialization: Optoelectronics & Optical Communication\n\n"

                                "Minikumari G.\n"
                                "Designation: Assistant Professor\n"
                                "Qualification: M.Tech.\n"
                                "Specialization: Microwave and TV Engineering\n\n"

                                "Shanu N.\n"
                                "Designation: Assistant Professor\n"
                                "Qualification: M.E.\n"
                                "Specialization: Communication Systems\n\n"

                                "Sajitha V. Raj\n"
                                "Designation: Assistant Professor\n"
                                "Qualification: M.Tech.\n"
                                "Specialization: Microwave & TV Engineering\n\n"

                                "Mili Rosline Mathews\n"
                                "Designation: Assistant Professor\n"
                                "Qualification: M.Tech.\n"
                                "Specialization: Signal Processing\n\n"

                                "Department of Applied Science\n\n"
                                "Mechanical and Engineering\n\n"
                                "Ganesh R\n"
                                "Designation: Assistant Professor in Mechanical Engineering\n"
                                "Qualification: M.Tech\n"
                                "Specialization: Propulsion Engineering\n\n"

                                "LAXMIKANTH K S\n"
                                "Designation: ASSISTANT PROFESSOR IN MECHANICAL ENGINEERING\n"
                                "Qualification: M.Tech\n"
                                "Specialization: THERMAL SCIENCE\n\n"

                                "Chemistry\n\n"
                                "ArunNath R\n"
                                "Designation: Assistant Professor in Chemistry\n"
                                "Qualification: Msc, BEd Physical Science\n"
                                "Specialization: Msc Analytical Chemistry\n\n"

                                "Maths\n\n"
                                "AJITHA KUMARI. R\n"
                                "Designation: Assoc. Professor in Mathematics\n"
                                "Qualification: MSc, M.Phil\n"
                                "Specialization: Graph Theory\n\n"

                                "MANOJ.S\n"
                                "Designation: Assistant professor\n"
                                "Qualification: MSc, M.Phil\n"
                                "Specialization: Semigroup Theory\n\n"

                                "Physics\n\n"
                                "MURALI V S\n"
                                "Designation: Associate Professor In Physics (Non Cadre)\n"
                                "Qualification: MSc, MPhil\n"
                                "Specialization: PHYSICS\n\n"],
                                "context": [""]

         },
           {
        "tag": "Attingal cse ",
        "patterns": ["Tell me about the professors in the Computer Science and Engineering department of College Of Engineering Attingal.",
                    "Who are the faculty members in the Computer Science and Engineering department of College Of Engineering Attingal?",
                    "Can you provide information on the teaching staff in Computer Science and Engineering at College Of Engineering Attingal?",
                    "Give me details about the Computer Science and Engineering department instructors of College Of Engineering Attingal.",
                    "I'd like to learn more about the professors teaching Computer Science and Engineering at College Of Engineering Attingal.",
                    "What can you tell me about the Computer Science and Engineering faculty of College Of Engineering Attingal?",
                    "Who makes up the staff in the Computer Science and Engineering of College Of Engineering Attingal?",
                    "Tell me about the Computer Science and Engineering instructors of College Of Engineering Attingal.",
                    "Share some insights into the Computer Science and Engineering staff of College Of Engineering Attingal.",
                    "Can you list the names of the professors in Computer Science and Engineering at College Of Engineering Attingal?"],
        "responses": [
                         "Computer Science and Engineering\n\n"
                            "Faculty\n\n"
                            "Dr. Suma L S\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- Ph D\n\n"

                            "Dancy Kurian\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- MTech\n\n"

                            "Dr. Leena Silvoster M\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- Ph D\n\n"

                            "Remya R S\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- M. Tech. PHD thesis submitted\n"
                            "Specialization:- Computer Science and Information Technology (M Tech)\n\n"

                            "Syama S R\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- M.Tech\n"
                            "Specialization:- Computer Science and Engineering\n\n"

                            "SHIJINA J SALIM\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- M.TECH\n"
                            "Specialization:- COMPUTER SCIENCE AND ENGINEERING\n\n"

                            "MEENU MOHAN\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- M.Tech in Computer Science\n"
                            "Specialization:- Image Processing\n\n"

                            "ARYA MURALI\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- M.TECH IN COMPUTER SCIENCE AND ENGINEERING\n"
                            "Specialization:- COMPUTER NETWORKS &PROGRAMMING LANGUAGES\n\n"

                            "Shaima Rahim\n"
                            "Designation:- ASSISTANT PROFESSOR\n"
                            "Qualification:- Mtech in Computer Science\n"
                            "Specialization:- Digital Image Computing\n\n"],
            "context": [""]
         },
        {
        "tag": "Attingal eee ",
        "patterns": ["Tell me about the professors in the Electrical Engineering department of College Of Engineering Attingal.",
                    "Who are the faculty members in the Electrical Engineering department of College Of Engineering Attingal?",
                    "Can you provide information on the teaching staff in Electrical Engineering at College Of Engineering Attingal?",
                    "Give me details about the Electrical Engineering instructors of College Of Engineering Attingal.",
                    "I'd like to learn more about the professors teaching Electrical Engineering at College Of Engineering Attingal.",
                    "What can you tell me about the Electrical Engineering faculty of College Of Engineering Attingal?",
                    "Who makes up the staff in the Electrical Engineering of College Of Engineering Attingal?",
                    "Tell me about the Electrical Engineering instructors of College Of Engineering Attingal.",
                    "Share some insights into the Electrical Engineering staff of College Of Engineering Attingal.",
                    "Can you list the names of the professors in Electrical Engineering at College Of Engineering Attingal?"],
        "responses": ["Electrical Engineering\n\n"
                      "Salins S S\n"
                        "Designation:- ASSISTANT PROFESSOR\n"
                        "Qualification:- M.Tech\n"
                        "Specialization:- Power Systems\n\n"

                        "Sreejith S\n"
                        "Designation:- ASSISTANT PROFESSOR\n"
                        "Qualification:- M.Tech\n"
                        "Specialization:- Power Systems\n\n"

                        "Anjana P\n"
                        "Designation:- ASSISTANT PROFESSOR\n"
                        "Qualification:- M.Tech\n"
                        "Specialization:- Power and Energy\n\n"

                        "Vani R\n"
                        "Designation:- ASSISTANT PROFESSOR\n"
                        "Qualification:- M.Tech\n"
                        "Specialization:- VLSI and Embedded System\n\n"

                        "Sneha V L\n"
                        "Designation:- ASSISTANT PROFESSOR\n"
                        "Qualification:- M.Tech\n"
                        "Specialization:- Control Systems\n\n"

                        "Aleena B S\n"
                        "Designation:- ASSISTANT PROFESSOR\n"
                        "Qualification:- M.Tech\n"
                        "Specialization:- Industrial Drives and Control\n\n"

                        "Neethu R Nair\n"
                        "Designation:- ASSISTANT PROFESSOR\n"
                        "Qualification:- M.Tech\n"
                        "Specialization:- Control and Instrumentation\n\n"],
             "context": [""]
         },
          {
        "tag": "Attingal ece ",
        "patterns": ["Tell me about the professors in the Electronics Engineering department of College Of Engineering Attingal.",
                    "Who are the faculty members in the Electronics Engineering department of College Of Engineering Attingal?",
                    "Can you provide information on the teaching staff in Electronics Engineering at College Of Engineering Attingal?",
                    "Give me details about the Electronics Engineering instructors of College Of Engineering Attingal.",
                    "I'd like to learn more about the professors teaching Electronics Engineering at College Of Engineering Attingal.",
                    "What can you tell me about the Electronics Engineering faculty of College Of Engineering Attingal?",
                    "Who makes up the staff in the Electronics Engineering of College Of Engineering Attingal?",
                    "Tell me about the Electronics Engineering instructors of College Of Engineering Attingal.",
                    "Share some insights into the Electronics Engineering staff of College Of Engineering Attingal.",
                    "Can you list the names of the professors in Electronics Engineering at College Of Engineering Attingal?"],
        "responses": ["Electronics Engineering\n\n"
                        "Dr. Sunil T.T.\n"
                        "Designation:- Professor\n"
                        "Qualification:- Ph.D.\n\n"

                        "Sudheer Babu P.P\n"
                        "Designation:- Assistant Professor\n"
                        "Qualification:- M.Tech.\n\n"],
                     "context": [""]

         },
        {
            "tag": "Attingal Courses",
            "patterns": ["What courses are offered at College Of Engineering Attingal?" ,
                         "Tell me about the programs available at College Of Engineering Attingal" ,
                         "Can you list the available courses at College Of Engineering Attingal?" ,
                         "What are the academic programs at College Of Engineering Attingal?",
                         "Which degrees can I pursue at College Of Engineering Attingal?",
                         "Give me information on the available majors at College Of Engineering Attingal",
                         "What fields of study are available at College Of Engineering Attingal?",
                         "Tell me about the curriculum options provided by College Of Engineering Attingal"],
            "responses": ["B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 60 seats per year \n"
                          "Computer Science & Engineering (Artificial Intelligence and Machine Learning) : 60 seats per year \n"
                          "Electrical & Electronics Engineering : 60 seats per year \n"
                          "Electronics & Communication Engineering : 60 per year \n"],
            "context": [""]
        },
        {
            "tag": "Contact Attingal",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Attingal?",
                        "I need the contact information of the College Of Engineering Attingal, please.",
                        "How can I get in touch with the College Of Engineering Attingal?","What is the College Of Engineering Attingal phone number?",
                        "Please share the College Of Engineering Attingal email address.",
                        "I'm looking for the address of the College Of Engineering Attingal.","How can I contact the admissions department of the College Of Engineering Attingal?",
                        "I need to reach the financial aid office of College Of Engineering Attingal. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Attingal?","Do College Of Engineering Attingal have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Attingal official website for contact details?","How do I get in touch with the College Of Engineering Attingal for general queries?"],
            "responses":
                ["College of Engineering Attingal , Near KSRTC Bus stand, Attingal P.O, Trivandurm, \nPin - 695 101. \nPhone No :0470-2627400 (O)\n Fax   No   :0470-2627400 \nMobile : 8547005037\n E-mail : ceattingal@ihrd.ac.in\n web : www.ceattingal.ac.in"],
            "context": [""]
        },
        {
            "tag": "Attingal",
            "patterns": ["Tell me about College Of Engineering Attingal", "College Of Engineering Attingal", "Attingal",
                          "Details about College Of Engineering Attingal"],
            "responses": [
                "College of Engineering Attingal, established by the Institute of Human Resources Development (IHRD), a Government of Kerala undertaking, is a premier technical institute having well-flourished environment for molding professionals. College of Engineering Attingal, started functioning in the academic year 2003-2004. The Institution has gained the approval of the All India Council for Technical Education and is an affiliated institution under KTU"],
            "context": [""]
        },
        {
            "tag": "Chengannur Faculty",
            "patterns": ["Tell me about the professors at College Of Engineering Chengannur.",
                        "Can you provide information about the teaching staff of College Of Engineering Chengannur?",
                        "Who are the faculty members here at College Of Engineering Chengannur?",
                        "Give me details about the academic staff of College Of Engineering Chengannur.",
                        "I'd like to learn more about the professors of College Of Engineering Chengannur.",
                        "What can you tell me about the teachers at College Of Engineering Chengannur?",
                        "Who makes up the faculty at College Of Engineering Chengannur?",
                        "Tell me about the instructors of College Of Engineering Chengannur.",
                        "Share some insights into the faculty members of College Of Engineering Chengannur.",
                        "Can you list the names of the professors of College Of Engineering Chengannur?"],
            "responses": ["Computer Engineering\n\n"
                        "HOD : Dr. Manju S Nair\n"
                        "Associate Professor & Head Of the Department\n"
                        "Department of Computer Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Dr. Shama Das\n"
                        "Designation:- Professor\n\n"

                        "Dr. Manju S Nair\n"
                        "Designation:- Associate Professor & HOD\n\n"
                        "Sri.Ahammed Siraj K K\n"
                        "Designation:- Associate Professor\n\n"

                        "Sri. Gopakumar G\n"
                        "Designation:- Associate Professor\n\n"

                        "Smt. C Jyothirmayi Devi\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Vinod P R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Manjusha Nair S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Ajoy Thomas\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Geetha S\n"
                        "Designation:- Assistant Professor (dptn to PhD)\n\n"

                        "Smt. Shiny B.\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Princy Sugathan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anjitha P\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Arathy U P\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Sreelekshmi K R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Syeatha Merlin Thampy\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Vishnu S Kumar\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Betty James\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Naseena N\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Angel Thankam Thomas\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. SHEMEEMA HASHIM\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Ameena A\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Shereena Thampi\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. ROSY K PHILIP\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. NEETHU TREESA JACOB\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. JITHY JOHN\n"
                        "Designation:- Assistant Professor\n\n"

                        "Staff\n"

                        "Sri. Susil Kumar M\n"
                        "Designation:- System Analyst\n\n"

                        "Smt. Sreelatha\n"
                        "Designation:- Junior System Analyst\n\n"

                        "Smt. Jalajakumari R\n"
                        "Designation:- Trade Instructor Grade II\n\n"

                        "Sri. Vinayak Harilal\n"
                        "Designation:- Demonstrator/Workshop Instructor\n\n"

                        "Smt. Darsana P Sam\n"
                        "Designation:- Computer Programmer\n\n"

                        "Smt. Thara Rajan\n"
                        "Designation:- Computer Programmer\n\n"

                        "Smt. Santhi krishna S\n"
                        "Designation:- Tradesman\n\n"

                        "Electrical Engineering\n\n"
                        "HOD : Dr. Rajeevan A K\n"
                        "Head of the Department\n"
                        "Department of Electrical Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Faculty\n\n"

                        "Dr. Rajeevan A K\n"
                        "Designation:- Assistant Professor & HOD\n\n"

                        "Dr. Raju M\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Savitha K P\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Sherin Joseph\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Bijukumar K\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Geethu Zacharia\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Veena Chandran S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Prasobh P\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Soumya S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Hridya S G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Arun K Vijayan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Geethu Zacharia\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anaswara Mohan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Shalu Priya S J\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Anandu M A\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Resmimol P R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Technical Staff\n\n"

                        "Sri. Benny Mathew V\n"
                        "Designation:- Foreman\n\n"

                        "Sri Suresh T K\n"
                        "Designation:- Demonstrator\n\n"

                        "Sri. Rajeev Rajan\n"
                        "Designation:- Demonstrator\n\n"

                        "Sri Anil C D\n"
                        "Designation:- Tradesman\n\n"

                        "Electronics Engineering\n\n"
                        "HOD : Dr. Laila D\n"
                        "Professor & Head Of the Department\n"
                        "Department of Electronics Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Faculty\n\n"

                        "Dr. Deepa J\n"
                        "Designation:- Professor\n\n"

                        "Dr. Shanavaz K T\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Rajesh Mohan R\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Sarah Jacob\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Shiji T P\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Hari V S\n"
                        "Designation:- Associate Professor\n\n"

                        "Smt. Deepa V S\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. M V Rajesh\n"
                        "Designation:- Associate Professor\n\n"

                        "Smt. Sheeja P George\n"
                        "Designation:- Associate Professor\n\n"

                        "Smt. Jisha Raj R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Dhivya Raj\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Darsana S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Varsha P S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Saji Kumar T V\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anupama A\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Rajesh M S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anuja V Nair\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Sylish S V\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Yasim Khan M\n"
                        "Designation:- Assistant Professor\n\n"

                        "Deepa Susan Jacob\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Raji A\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Nisha Rajan S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Sam K Sumesh\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Vibesh V Panicker\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Neethu Verjisen\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Sruthi B R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Rijimol Mathew\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anju V Sathyan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Rajalakshmy A K\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Sreechandanalal J\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Neethu Anilkumar\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Renjitha\n"
                        "Designation:- Assistant Professor\n\n"

                        "Technical Staff\n\n"

                        "Smt. Bindhu V\n"
                        "Designation:- Demonstrator/W.S Instructor Hg. Gr. I\n\n"

                        "Sri. P Prem\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Smt. Mini S\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Sri. M Suresh\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Sri. Binesh Joseph\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Smt. Chandralekha C\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Sri. Mohammed Mubarack P S\n"
                        "Designation:- Demonstrator/W.S Instructor (Electronics)\n\n"

                        "Sri. Chinthumon C G\n"
                        "Designation:- Demonstrator/W.S Instructor (Electronics)\n\n"

                        "General Engineering\n\n"
                        "HOD : Dr. Rajesh V G\n"
                        "Head Of the Department\n"
                        "Department of General Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Faculty\n\n"

                        "Sri. Jayadeep Kumar J\n"
                        "Assistant Professor\n\n"

                        "Smt. Athira Thulasidas\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Sarath Kumar S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Jamshak S H\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Justin G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Technical Staff\n\n"

                        "Sri. Radhakrishnan N S\n"
                        "Designation:- Foreman\n\n"

                        "Sri. Vinod G\n"
                        "Designation:- Tradesman (Carpentry)\n\n"

                        "Smt. Rakhy T R\n"
                        "Designation:- Tradesman (Civil)\n\n"

                        "Sri.Arun kumar S\n"
                        "Designation:- Tradesman\n\n"

                        "Sri.Preejith P K\n"
                        "Designation:- Tradesman\n\n"

                        "Applied Sciences\n\n"
                        "HOD : Dr. Madhusoodhanan Nair R\n"
                        "Head Of the Department\n"
                        "Department of Applied Sciences\n"
                        "College of Engineering, Chengannur\n\n"

                        "Faculty\n\n"

                        "Dr. C R Ajith Sen\n"
                        "Designation:- Professor (NC) (Physical Education)\n\n"

                        "Smt.Rani Vijaya G L\n"
                        "Designation:- Associate Professor(Mathematics)\n\n"

                        "Smt.Renu K K\n"
                        "Designation:- Associate Professor(Mathematics)\n\n"

                        "Sri. Suresh Kumar G\n"
                        "Designation:- Associate Professor (NC) (Mathematics)\n\n"

                        "Smt.Pushpa L\n"
                        "Designation:- Assistant Professor(Chemistry)\n\n"

                        "Smt. Jalaja M B\n"
                        "Designation:- Assistant Professor (Mathematics)\n\n"

                        "Smt. Amritha P Vijay\n"
                        "Designation:- Assistant Professor (Civil)\n\n"

                        "Smt. Jiji Anna Raju\n"
                        "Designation:- Assistant Professor(English)\n\n"

                        "Sri. Amal Suresh\n"
                        "Designation:- Assistant Professor(English)\n\n"

                        "Smt. Lincy Thomas\n"
                        "Designation:- Assistant Professor (Physics)\n\n"

                        "Smt. Malavika M Kurup\n"
                        "Designation:- Assistant Professor (Chemistry)\n\n"

                        "Smt. Smitha K\n"
                        "Designation:- Assistant Professor (Economics)\n\n"

                        "Smt. Reji S\n"
                        "Designation:- Professor (Mathematics)\n\n"],
            "context": [""]
        },
        {
            "tag": "Chengannur cse ",
            "patterns": ["Tell me about the professors in the Computer Science and Engineering department of College Of Engineering Chengannur.",
                        "Who are the faculty members in the Computer Science and Engineering department of College Of Engineering Chengannur?",
                        "Can you provide information on the teaching staff in Computer Science and Engineering at College Of Engineering Chengannur?",
                        "Give me details about the Computer Science and Engineering department instructors of College Of Engineering Chengannur.",
                        "I'd like to learn more about the professors teaching Computer Science and Engineering at College Of Engineering Chengannur.",
                        "What can you tell me about the Computer Science and Engineering faculty of College Of Engineering Chengannur?",
                        "Who makes up the staff in the Computer Science and Engineering of College Of Engineering Chengannur?",
                        "Tell me about the Computer Science and Engineering instructors of College Of Engineering Chengannur.",
                        "Share some insights into the Computer Science and Engineering staff of College Of Engineering Chengannur.",
                        "Can you list the names of the professors in Computer Science and Engineering at College Of Engineering Chengannur?"],
            "responses": ["Computer Science and Engineering\n\n"

                        "HOD : Shibu J\n"
                        "Designation Associate Professor\n\n"

                        "Faculty\n\n"

                        "Mr Shibu J\n"
                        "Designation:- Associate Professor\n\n"

                        "Mr Vinod P R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Ms Girija V R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mr Jayaram K\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs Sreedeepa H S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs Manju J\n"
                        "Designation:- Assistant Professor\n\n"

                        "Ms Honey M\n"
                        "Designation:- Assistant Professor\n\n"

                        "Ms Keerthana R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs Jyothi Vijayan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Staff\n\n"

                        "Sreeja Krishnan\n"
                        "Designation:-Computer Programmer\n\n"

                        "Arya A\n"
                        "Designation:-Computer Programmer\n\n"

                        "Samzeena S\n"
                        "Designation:-Workshop Instructor\n\n"

                        "Nisha Chandran\n"
                        "Designation:-	Workshop Instructor\n\n"

                        "Department of Applied Sciences\n\n"
                        "HOD : MONI P JOHN\n"
                        "Designation:- Associate Professor in Chemistry\n\n"

                        "FACULTY\n\n"

                        "Dr AJITHA P S\n"
                        "Designation:- Associate Professor\n\n"

                        "Mr RUBON L\n"
                        "Designation:-  Associate Professor\n\n"

                        "Mrs SHEEBA JOSEPH\n"
                        "Designation:- Associate Professor\n\n"

                        "Mrs SHIJI KV\n"
                        "Designation:- Associate Professor\n\n"

                        "Mrs RETHEE KUMARY S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs THAZNEEM ANSARI\n"
                        "Designation:- Assistant Professor\n\n"

                        "Mrs NIKHITHA MUHAMMAD\n"
                        "Designation:- Assistant Professor\n\n"],
            "context": [""]
         },
        {
            "tag": "Chengannur eee ",
            "patterns": ["Tell me about the professors in the Electrical Engineering department of College Of Engineering Chengannur.",
                        "Who are the faculty members in the Electrical Engineering department of College Of Engineering Chengannur?",
                        "Can you provide information on the teaching staff in Electrical Engineering at College Of Engineering Chengannur?",
                        "Give me details about the Electrical Engineering instructors of College Of Engineering Chengannur.",
                        "I'd like to learn more about the professors teaching Electrical Engineering at College Of Engineering Chengannur.",
                        "What can you tell me about the Electrical Engineering faculty of College Of Engineering Chengannur?",
                        "Who makes up the staff in the Electrical Engineering of College Of Engineering Chengannur?",
                        "Tell me about the Electrical Engineering instructors of College Of Engineering Chengannur.",
                        "Share some insights into the Electrical Engineering staff of College Of Engineering Chengannur.",
                        "Can you list the names of the professors in Electrical Engineering at College Of Engineering Chengannur?"],
            "responses": ["Electrical Engineering\n\n"
                        "HOD : Dr. Rajeevan A K\n"
                        "Head of the Department\n"
                        "Department of Electrical Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Faculty\n\n"

                        "Dr. Rajeevan A K\n"
                        "Designation:- Assistant Professor & HOD\n\n"

                        "Dr. Raju M\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Savitha K P\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Sherin Joseph\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Bijukumar K\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Geethu Zacharia\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Veena Chandran S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Prasobh P\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Soumya S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Hridya S G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Arun K Vijayan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Geethu Zacharia\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anaswara Mohan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Shalu Priya S J\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Anandu M A\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Resmimol P R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Technical Staff\n\n"

                        "Sri. Benny Mathew V\n"
                        "Designation:- Foreman\n\n"

                        "Sri Suresh T K\n"
                        "Designation:- Demonstrator\n\n"

                        "Sri. Rajeev Rajan\n"
                        "Designation:- Demonstrator\n\n"

                        "Sri Anil C D\n"
                        "Designation:- Tradesman\n\n"],
            "context": [""]
         },
        {
            "tag": "Chengannur ece ",
            "patterns": ["Tell me about the professors in the Electronics Engineering department of College Of Engineering Chengannur.",
                        "Who are the faculty members in the Electronics Engineering department of College Of Engineering Chengannur?",
                        "Can you provide information on the teaching staff in Electronics Engineering at College Of Engineering Chengannur?",
                        "Give me details about the Electronics Engineering instructors of College Of Engineering Chengannur.",
                        "I'd like to learn more about the professors teaching Electronics Engineering at College Of Engineering Chengannur.",
                        "What can you tell me about the Electronics Engineering faculty of College Of Engineering Chengannur?",
                        "Who makes up the staff in the Electronics Engineering of College Of Engineering Chengannur?",
                        "Tell me about the Electronics Engineering instructors of College Of Engineering Chengannur.",
                        "Share some insights into the Electronics Engineering staff of College Of Engineering Chengannur.",
                        "Can you list the names of the professors in Electronics Engineering at College Of Engineering Chengannur?"],
            "responses": ["Electronics Engineering\n\n"
                        "HOD : Dr. Laila D\n"
                        "Professor & Head Of the Department\n"
                        "Department of Electronics Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Faculty\n\n"

                        "Dr. Deepa J\n"
                        "Designation:- Professor\n\n"

                        "Dr. Shanavaz K T\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Rajesh Mohan R\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Sarah Jacob\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Shiji T P\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. Hari V S\n"
                        "Designation:- Associate Professor\n\n"

                        "Smt. Deepa V S\n"
                        "Designation:- Associate Professor\n\n"

                        "Dr. M V Rajesh\n"
                        "Designation:- Associate Professor\n\n"

                        "Smt. Sheeja P George\n"
                        "Designation:- Associate Professor\n\n"

                        "Smt. Jisha Raj R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Dhivya Raj\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Darsana S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Varsha P S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Saji Kumar T V\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anupama A\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Rajesh M S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anuja V Nair\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Sylish S V\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Yasim Khan M\n"
                        "Designation:- Assistant Professor\n\n"

                        "Deepa Susan Jacob\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Raji A\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Nisha Rajan S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Sam K Sumesh\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sri. Vibesh V Panicker\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Neethu Verjisen\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Sruthi B R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Rijimol Mathew\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Anju V Sathyan\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Rajalakshmy A K\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Sreechandanalal J\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Neethu Anilkumar\n"
                        "Designation:- Assistant Professor\n\n"

                        "Smt. Renjitha\n"
                        "Designation:- Assistant Professor\n\n"

                        "Technical Staff\n\n"

                        "Smt. Bindhu V\n"
                        "Designation:- Demonstrator/W.S Instructor Hg. Gr. I\n\n"

                        "Sri. P Prem\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Smt. Mini S\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Sri. M Suresh\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Sri. Binesh Joseph\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Smt. Chandralekha C\n"
                        "Designation:- Trade Instructor Gr. II (Electronics)\n\n"

                        "Sri. Mohammed Mubarack P S\n"
                        "Designation:- Demonstrator/W.S Instructor (Electronics)\n\n"

                        "Sri. Chinthumon C G\n"
                        "Designation:- Demonstrator/W.S Instructor (Electronics)\n\n"],
            "context": [""]
         },
        {
            "tag": "Chengannur hod ",
            "patterns": ["I'd like to know who the HODs of the College Of Engineering Chengannur.",
                        "Can you share the HODs' names for the departments of College Of Engineering Chengannur ?",
                        "Can you tell me about the other department heads of College Of Engineering Chengannur?",
                        "Could you give me an overview of the department heads of College Of Engineering Chengannur?",
                        "Tell me about the leadership in the departments of College Of Engineering Chengannur.",
                        "Provide information about the Heads of Departments in theCollege Of Engineering Chengannur."],
            "responses": ["Computer Engineering\n\n"
                        "HOD : Dr. Manju S Nair\n"
                        "Associate Professor & Head Of the Department\n"
                        "Department of Computer Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Electrical Engineering\n\n"
                        "HOD : Dr. Rajeevan A K\n"
                        "Head of the Department\n"
                        "Department of Electrical Engineering\n"
                        "College of Engineering, Chengannur\n\n"

                        "Electronics Engineering\n\n"
                        "HOD : Dr. Laila D\n"
                        "Professor & Head Of the Department\n"
                        "Department of Electronics Engineering\n"
                        "College of Engineering, Chengannur\n\n"],
            "context": [""]
         },

        {
            "tag": "Chengannur Courses",
            "patterns": ["What courses are offered at College Of Engineering Chengannur?" ,
                         "Tell me about the programs available at College Of Engineering Chengannur" ,
                         "Can you list the available courses at College Of Engineering Chengannur?" ,
                         "What are the academic programs at College Of Engineering Chengannur?",
                         "Which degrees can I pursue at College Of Engineering Chengannur?",
                         "Give me information on the available majors at College Of Engineering Chengannur",
                         "What fields of study are available at College Of Engineering Chengannur?",
                         "Tell me about the curriculum options provided by College Of Engineering Chengannur"],
            "responses": ["M.Tech Courses =\n\n "
                          "Electronics with specialization in  VLSI & Embedded Systems : 18 seats per year\n"
                          "Computer Science with specialization in  Digital Image Processing : 18 seats per year\n\n"
                          "B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 120 seats per year \n"
                          "Electrical & Electronics Engineering : 120 seats per year \n"
                          "Electronics & Communication Engineering : 120 per year \n"
                          "Electronics and Instrumentation Engineering : 60 per year \n\n"
                          "MCA Courses =\n\n"
                          "Master of Computer Applications : 60 seats per year\n"],
            "context": [""]
        },
        {
            "tag": "Contact Chengannur",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Chengannur?",
                        "I need the contact information of the College Of Engineering Chengannur, please.",
                        "How can I get in touch with the College Of Engineering Chengannur?","What is the College Of Engineering Chengannur phone number?",
                        "Please share the College Of Engineering Chengannur email address.",
                        "I'm looking for the address of the College Of Engineering Chengannur.","How can I contact the admissions department of the College Of Engineering Chengannur?",
                        "I need to reach the financial aid office of College Of Engineering Chengannur. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Chengannur?","Do College Of Engineering Chengannur have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Chengannur official website for contact details?","How do I get in touch with the College Of Engineering Chengannur for general queries?"],
            "responses":
                ["College of Engineering, Chengannur, Alleppuzha District. Kerala state.\n Pin - 689 121 \nPhone : 0479-2456046 (P)\n Phone : 0479-2454125 (O),\n Phone : 0479-2451424(AO)\n Phone : 0479-2455125(Rec.) \nMobile: 8547005032\n E-mail : cechengannur@ihrd.ac.in \nweb : www.ceconline.edu"],
            "context": [""]
        },
        {
            "tag": "Chengannur",
            "patterns": ["Tell me about College Of Engineering Chengannur", "College Of Engineering Chengannur", "Chengannur",
                          "Details about College Of Engineering Chengannur"],
            "responses": [
                "The College of Engineering Chengannur, was established in the year 1993, with a vision to create engineers having the drive, skill, and confidence to become the pioneers of tomorrow. The college was set up under the auspices of the Institute of Human Resources and Development (IHRD) and is recognized by the All India Council for Technical Education (AICTE), New Delhi. It is affiliated to the Cochin University of Science and Technology (CUSAT) which is known internationally for its academic excellence. The courses offered are designed to cater to the industry’s urgent demand for skilled professionals in the field of Computers and Electronics"],
            "context": [""]
        },
           {
    "tag": "Cherthala Faculty",
            "patterns": ["Tell me about the professors at College Of Engineering Cherthala.",
                        "Can you provide information about the teaching staff of College of Engineering, Cherthala?",
                        "Who are the faculty members here at College of Engineering, Cherthala?",
                        "Give me details about the academic staff of College of Engineering, Cherthala.",
                        "I'd like to learn more about the professors of College of Engineering, Cherthala.",
                        "What can you tell me about the teachers at College of Engineering, Cherthala?",
                        "Who makes up the faculty at College of Engineering, Cherthala?",
                        "Tell me about the instructors of College of Engineering, Cherthala.",
                        "Share some insights into the faculty members of College of Engineering, Cherthala.",
                        "Can you list the names of the professors of College of Engineering, Cherthala?"],
         "responses": ["COMPUTER ENGINEERING\n\n"

                        "HOD : Dr.Priya S\n"
                        "Designation :-Professor \n"
                        "Qualification:- Ph.D\n"
                        "Experience : 24 Years\n\n"

                        "Faculty\n\n"

                        "Manilal D L\n"
                        "Designation :-Associate Professor\n\n"

                        "Muhammed Ilyas H\n"
                        "Designation :-Associate Professor\n\n"

                        "Anitha M A\n"
                        "Designation :-Associate Professor\n\n"

                        "Janu R. Panicker\n"
                        "Designation :-Associate Professor\n\n"

                        "Greeshma N.Gopal\n"
                        "Designation :-Associate Professor\n\n"

                        "Jayakrishnan R\n"
                        "Designation :-Associate Professor\n\n"

                        "Jasmine Joseph\n"
                        "Designation :-Associate Professor(C)\n\n"

                        "Rohitha R\n"
                        "Designation :-Associate Professor\n\n"

                        "Lekshmi R Nair\n"
                        "Designation :-Associate Professor\n\n"

                        "Judy Ann Joy\n"
                        "Designation :-Associate Professor(C)\n\n"

                        "Jincy Showri\n"
                        "Designation :-Associate Professor\n\n"

                        "Vimal Vinod\n"
                        "Designation :-Associate Professor\n\n"

                        "SIKHA SASIDHARAN\n"
                        "Designation :-Associate Professor\n\n"

                        "Fathima Aneez\n"
                        "Designation :-Associate Professor\n\n"

                        "Vishnupriya G S\n"
                        "Designation :-Associate Professor\n\n"

                        "Shabana H\n"
                        "Designation :-Associate Professor\n\n"

                        "Arun Betty A S\n"
                        "Designation :-Associate Professor\n\n"

                        "Rakhi . R\n"
                        "Designation :-Associate Professor\n\n"

                        "Shemeema Hashim\n"
                        "Designation :-Associate Professor\n\n"

                        "Technical Staff\n\n"

                        "Ajit Kumar S\n"
                        "Designation :-Junior System Analyst\n\n"

                        "Madhusudana Kurup S.P\n"
                        "Designation :-Computer Programmer\n\n"

                        "Satheesh Mohan\n"
                        "Designation :-Computer Programmer\n\n"

                        "Liji Jose\n"
                        "Designation :- System Analyst\n\n"

                        "Shoma S Rajan\n"
                        "Designation :- Trade Instructor\n\n"

                        "Shahina H\n"
                        "Designation :- Demonstrator\n\n"

                        "ELECTRONICS ENGINEERING\n\n"

                        "HOD : Dr. Ashok Kumar T\n"
                        "Designation :-Associate Professor\n"

                        "Experience	:  27 Years \n"
                        "Teaching	:  Embedded System Design, Soft Computing\n"
                        "Research	: Digital Image processing, Embedded System, Wireless Networks, Machine Learning\n\n"

                        "Faculty\n\n"

                        "Anisha Mohammed\n"
                        "Designation :-Associate Professor\n\n"

                        "Laghima PM\n"
                        "Designation :-Associate Professor\n\n"

                        "Sreekumar K\n"
                        "Designation :-Associate Professor\n\n"

                        "Swapna\n"
                        "Designation :-Associate Professor\n\n"

                        "Jasleena C\n"
                        "Designation :-Associate Professor\n\n"

                        "Meera Thampy\n"
                        "Designation :-Associate Professor\n\n"

                        "Jisha mol L\n"
                        "Designation :-Associate Professor\n\n"

                        "Sunith C K\n"
                        "Designation :-Associate Professor\n\n"

                        "Visanthi V P\n"
                        "Designation :-Associate Professor\n\n"

                        "Technical Staff\n\n"

                        "Ajitha Kumari P\n"
                        "Designation :-Demonstrator\n\n"

                        "George C Karamel\n"
                        "Designation :-Demonstrator\n\n"

                        "Deepesh P\n"
                        "Designation :-Demonstrator\n\n"

                        "ELECTRICAL ENGINEERING\n\n"

                        "HOD : Elizwa Laiju\n"
                        "Designation :-Associate Professor\n\n"

                        "Riya Augustine\n"
                        "Designation :-Associate Professor\n\n"

                        "Dickson\n"
                        "Designation :-Associate Professor\n\n"

                        "Anjali T.H\n"
                        "Designation :-Associate Professor\n\n"

                        "Technical Staff\n\n"

                        "Jessy Abraham\n"
                        "Designation :-Trade Instructor Grade-ll\n\n"

                        "Amal Satheesan\n"
                        "Designation :-Tradesman\n\n"

                        "Wenstone E D\n"
                        "Designation :-Demonstrator\n\n"

                        "GENERAL ENGINEERING\n\n"

                        "HOD : Varghese M P\n"
                        "Designation :-Associate Professor\n\n"

                        "Shifana A N\n"
                        "Designation :-Assistant Professor (Civil)\n\n"

                        "Nikil Dev C K \n"
                        "Designation :-Assistant Professor (ME)\n\n"

                        "Sarath Prakash \n"
                        "Designation :-Assistant Professor (ME)\n\n"

                        "Technical Staff\n\n"

                        "Santhosh A.J.\n"
                        "Designation :-Tradesman in M.E\n\n"

                        "APPLIED SCIENCES\n\n"
                        "HOD : SARAKUTTY K.J.\n"
                        "Designation:- Associate Professor (Mathematics)\n\n"

                        "Faculty\n\n"

                        "PRIYAKUMAR T.N.\n"
                        "Designation:- Associate Professor (Mathematics)\n\n"

                        "Suja N Thomas\n"
                        "Designation:- Associate Professor (Mathematics)\n\n"

                        "Alphonsa K.A\n"
                        "Designation:- Assistant Professor (Physics)\n\n"

                        "Jithin George\n"
                        "Designation:- Assistant Professor (English)\n\n"],
                                        "context": [""]

    },
    {
            "tag": "Chengannur cse ",
            "patterns": ["Tell me about the professors in the Computer Science and Engineering department of College Of Engineering Chengannur.",
                        "Who are the faculty members in the Computer Science and Engineering department of College Of Engineering Chengannur?",
                        "Can you provide information on the teaching staff in Computer Science and Engineering at College Of Engineering Chengannur?",
                        "Give me details about the Computer Science and Engineering department instructors of College Of Engineering Chengannur.",
                        "I'd like to learn more about the professors teaching Computer Science and Engineering at College Of Engineering Chengannur.",
                        "What can you tell me about the Computer Science and Engineering faculty of College Of Engineering Chengannur?",
                        "Who makes up the staff in the Computer Science and Engineering of College Of Engineering Chengannur?",
                        "Tell me about the Computer Science and Engineering instructors of College Of Engineering Chengannur.",
                        "Share some insights into the Computer Science and Engineering staff of College Of Engineering Chengannur.",
                        "Can you list the names of the professors in Computer Science and Engineering at College Of Engineering Chengannur?"],
            "responses": ["Computer Science and Engineering\n\n"

                                "HOD : Dr.Priya S\n"
                                "Designation :-Professor \n"
                                "Qualification:- Ph.D\n"
                                "Experience : 24 Years\n\n"

                                "Faculty\n\n"

                                "Manilal D L\n"
                                "Designation :-Associate Professor\n\n"

                                "Muhammed Ilyas H\n"
                                "Designation :-Associate Professor\n\n"

                                "Anitha M A\n"
                                "Designation :-Associate Professor\n\n"

                                "Janu R. Panicker\n"
                                "Designation :-Associate Professor\n\n"

                                "Greeshma N.Gopal\n"
                                "Designation :-Associate Professor\n\n"

                                "Jayakrishnan R\n"
                                "Designation :-Associate Professor\n\n"

                                "Jasmine Joseph\n"
                                "Designation :-Associate Professor(C)\n\n"

                                "Rohitha R\n"
                                "Designation :-Associate Professor\n\n"

                                "Lekshmi R Nair\n"
                                "Designation :-Associate Professor\n\n"

                                "Judy Ann Joy\n"
                                "Designation :-Associate Professor(C)\n\n"

                                "Jincy Showri\n"
                                "Designation :-Associate Professor\n\n"

                                "Vimal Vinod\n"
                                "Designation :-Associate Professor\n\n"

                                "SIKHA SASIDHARAN\n"
                                "Designation :-Associate Professor\n\n"

                                "Fathima Aneez\n"
                                "Designation :-Associate Professor\n\n"

                                "Vishnupriya G S\n"
                                "Designation :-Associate Professor\n\n"

                                "Shabana H\n"
                                "Designation :-Associate Professor\n\n"

                                "Arun Betty A S\n"
                                "Designation :-Associate Professor\n\n"

                                "Rakhi . R\n"
                                "Designation :-Associate Professor\n\n"

                                "Shemeema Hashim\n"
                                "Designation :-Associate Professor\n\n"

                                "Technical Staff\n\n"

                                "Ajit Kumar S\n"
                                "Designation :-Junior System Analyst\n\n"

                                "Madhusudana Kurup S.P\n"
                                "Designation :-Computer Programmer\n\n"

                                "Satheesh Mohan\n"
                                "Designation :-Computer Programmer\n\n"

                                "Liji Jose\n"
                                "Designation :- System Analyst\n\n"

                                "Shoma S Rajan\n"
                                "Designation :- Trade Instructor\n\n"

                                "Shahina H\n"
                                "Designation :- Demonstrator\n\n"
                          ],
                         "context": [""]


    },
   {
        "tag": "Cherthala ece ",
        "patterns": ["Tell me about the professors in the Electronics Engineering department of College Of Engineering Cherthala.",
                    "Who are the faculty members in the Electronics Engineering department of College Of Engineering Cherthala?",
                    "Can you provide information on the teaching staff in Electronics Engineering at College Of Engineering Cherthala?",
                    "Give me details about the Electronics Engineering instructors of College Of Engineering Cherthala.",
                    "I'd like to learn more about the professors teaching Electronics Engineering at College Of Engineering Cherthala.",
                    "What can you tell me about the Electronics Engineering faculty of College Of Engineering Cherthala?",
                    "Who makes up the staff in the Electronics Engineering of College Of Engineering Cherthala?",
                    "Tell me about the Electronics Engineering instructors of College Of Engineering Cherthala.",
                    "Share some insights into the Electronics Engineering staff of College Of Engineering Cherthala.",
                    "Can you list the names of the professors in Electronics Engineering at College Of Engineering Cherthala?"],
        "responses": ["Electronics Engineering\n\n"
                      "HOD : Dr. Ashok Kumar T\n"
                            "Designation :-Associate Professor\n"

                            "Experience	:  27 Years \n"
                            "Teaching	:  Embedded System Design, Soft Computing\n"
                            "Research	: Digital Image processing, Embedded System, Wireless Networks, Machine Learning\n\n"

                            "Faculty\n\n"

                            "Anisha Mohammed\n"
                            "Designation :-Associate Professor\n\n"

                            "Laghima PM\n"
                            "Designation :-Associate Professor\n\n"

                            "Sreekumar K\n"
                            "Designation :-Associate Professor\n\n"

                            "Swapna\n"
                            "Designation :-Associate Professor\n\n"

                            "Jasleena C\n"
                            "Designation :-Associate Professor\n\n"

                            "Meera Thampy\n"
                            "Designation :-Associate Professor\n\n"

                            "Jisha mol L\n"
                            "Designation :-Associate Professor\n\n"

                            "Sunith C K\n"
                            "Designation :-Associate Professor\n\n"

                            "Visanthi V P\n"
                            "Designation :-Associate Professor\n\n"

                            "Technical Staff\n\n"

                            "Ajitha Kumari P\n"
                            "Designation :-Demonstrator\n\n"

                            "George C Karamel\n"
                            "Designation :-Demonstrator\n\n"

                            "Deepesh P\n"
                            "Designation :-Demonstrator\n\n"
                      ],
                                     "context": [""]

    },
    {
    "tag": "Cherthala eee ",
        "patterns": ["Tell me about the professors in the Electrical Engineering department of College Of Engineering Cherthala.",
                    "Who are the faculty members in the Electrical Engineering department of College Of Engineering Cherthala?",
                    "Can you provide information on the teaching staff in Electrical Engineering at College Of Engineering Cherthala?",
                    "Give me details about the Electrical Engineering instructors of College Of Engineering Cherthala.",
                    "I'd like to learn more about the professors teaching Electrical Engineering at College Of Engineering Cherthala.",
                    "What can you tell me about the Electrical Engineering faculty of College Of Engineering Cherthala?",
                    "Who makes up the staff in the Electrical Engineering of College Of Engineering Cherthala?",
                    "Tell me about the Electrical Engineering instructors of College Of Engineering Cherthala.",
                    "Share some insights into the Electrical Engineering staff of College Of Engineering Cherthala.",
                    "Can you list the names of the professors in Electrical Engineering at College Of Engineering Cherthala?"],
        "responses": ["Electrical Engineering\n\n"
                        "HOD : Elizwa Laiju\n"
                        "Designation :-Associate Professor\n\n"

                        "Riya Augustine\n"
                        "Designation :-Associate Professor\n\n"

                        "Dickson\n"
                        "Designation :-Associate Professor\n\n"

                        "Anjali T.H\n"
                        "Designation :-Associate Professor\n\n"

                        "Technical Staff\n\n"

                        "Jessy Abraham\n"
                        "Designation :-Trade Instructor Grade-ll\n\n"

                        "Amal Satheesan\n"
                        "Designation :-Tradesman\n\n"

                        "Wenstone E D\n"
                        "Designation :-Demonstrator\n\n"
                      ],
                    "context": [""]
    },
    {
            "tag": "Cherthala ge ",
            "patterns": ["Tell me about the professors in the General Engineering department of College Of Engineering Cherthala.",
                        "Who are the faculty members in the General Engineering department of College Of Engineering Cherthala?",
                        "Can you provide information on the teaching staff in General Engineering at College Of Engineering Cherthala?",
                        "Give me details about the General Engineering instructors of College Of Engineering Cherthala.",
                        "I'd like to learn more about the professors teaching General Engineering at College Of Engineering Cherthala.",
                        "What can you tell me about the General Engineering faculty of College Of Engineering Cherthala?",
                        "Who makes up the staff in the General Engineering of College Of Engineering Cherthala?",
                        "Tell me about the General Engineering instructors of College Of Engineering Cherthala.",
                        "Share some insights into the General Engineering staff of College Of Engineering Cherthala.",
                        "Can you list the names of the professors in General Engineering at College Of Engineering Cherthala?"],
            "responses": ["General Engineering\n\n"
                          "HOD : Varghese M P\n"
                            "Designation :-Associate Professor\n\n"

                            "Shifana A N\n"
                            "Designation :-Assistant Professor (Civil)\n\n"

                            "Nikil Dev C K \n"
                            "Designation :-Assistant Professor (ME)\n\n"

                            "Sarath Prakash \n"
                            "Designation :-Assistant Professor (ME)\n\n"

                            "Technical Staff\n\n"

                            "Santhosh A.J.\n"
                            "Designation :-Tradesman in M.E\n\n"

                          ],
                                "context": [""]
    },
    {
            "tag": "Cherthala applied ",
                 "patterns": ["Tell me about the professors in the Applied Engineering department of College Of Engineering Cherthala.",
                        "Who are the faculty members in the Applied Engineering department of College Of Engineering Cherthala?",
                        "Can you provide information on the teaching staff in Applied Engineering at College Of Engineering Cherthala?",
                        "Give me details about the Applied Engineering instructors of College Of Engineering Cherthala.",
                        "I'd like to learn more about the professors teaching Applied Engineering at College Of Engineering Cherthala.",
                        "What can you tell me about the Applied Engineering faculty of College Of Engineering Cherthala?",
                        "Who makes up the staff in the Applied Engineering of College Of Engineering Cherthala?",
                        "Tell me about the Applied Engineering instructors of College Of Engineering Cherthala.",
                        "Share some insights into the Applied Engineering staff of College Of Engineering Cherthala.",
                        "Can you list the names of the professors in Applied Engineering at College Of Engineering Cherthala?"],
                 "responses": [ "APPLIED SCIENCES\n\n"
                               "HOD : SARAKUTTY K.J.\n"
                                "Designation:- Associate Professor (Mathematics)\n\n"

                                "Faculty\n\n"

                                "PRIYAKUMAR T.N.\n"
                                "Designation:- Associate Professor (Mathematics)\n\n"

                                "Suja N Thomas\n"
                                "Designation:- Associate Professor (Mathematics)\n\n"

                                "Alphonsa K.A\n"
                                "Designation:- Assistant Professor (Physics)\n\n"

                                "Jithin George\n"
                                "Designation:- Assistant Professor (English)\n\n"
                               ],
                                                 "context": [""]

    },
     {
            "tag": "Chengannur hod ",
            "patterns": ["I'd like to know who the HODs of the College Of Engineering Chengannur.",
                        "Can you share the HODs' names for the departments of College Of Engineering Chengannur ?",
                        "Can you tell me about the other department heads of College Of Engineering Chengannur?",
                        "Could you give me an overview of the department heads of College Of Engineering Chengannur?",
                        "Tell me about the leadership in the departments of College Of Engineering Chengannur.",
                        "Provide information about the Heads of Departments in theCollege Of Engineering Chengannur."],
            "responses": ["COMPUTER ENGINEERING\n\n"
                            "HOD : Dr.Priya S\n"
                            "Designation :-Professor \n"
                            "Qualification:- Ph.D\n"
                            "Experience : 24 Years\n\n"

                            "ELECTRONICS ENGINEERING\n\n"
                            "HOD : Dr. Ashok Kumar T\n"
                            "Designation :-Associate Professor\n"


                            "ELECTRICAL ENGINEERING\n\n"
                            "HOD : Elizwa Laiju\n"
                            "Designation :-Associate Professor\n\n"

                            "GENERAL ENGINEERING\n\n"
                            "HOD : Varghese M P\n"
                            "Designation :-Associate Professor\n\n"


                            "APPLIED SCIENCES\n\n"
                            "HOD : SARAKUTTY K.J.\n"
                            "Designation:- Associate Professor (Mathematics)\n\n"


                          ],
                  "context": [""]

    },
         {
            "tag": "Cherthala Courses",
            "patterns": ["What courses are offered at College Of Engineering Cherthala?" ,
                         "Tell me about the programs available at College Of Engineering Cherthala" ,
                         "Can you list the available courses at College Of Engineering Cherthala?" ,
                         "What are the academic programs at College Of Engineering Cherthala?",
                         "Which degrees can I pursue at College Of Engineering Cherthala?",
                         "Give me information on the available majors at College Of Engineering Cherthala",
                         "What fields of study are available at College Of Engineering Cherthala?",
                         "Tell me about the curriculum options provided by College Of Engineering Cherthala"],
            "responses": ["M.Tech Courses =\n\n "
                          "Electronics Engineering ( Signal Processing) : 24 seats per year\n"
                          "Computer Science Engineering ( Computer and Information Science) : 24 seats per year\n\n"
                          "B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 90 seats per year \n"
                          "Electrical & Electronics Engineering : 60 seats per year \n"
                          "Electronics & Communication Engineering : 60 per year \n"],
            "context": [""]
        },

        {
            "tag": "Contact Cherthala",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Cherthala?",
                        "I need the contact information of the College Of Engineering Cherthala, please.",
                        "How can I get in touch with the College Of Engineering Cherthala?","What is the College Of Engineering Cherthala phone number?",
                        "Please share the College Of Engineering Cherthala email address.",
                        "I'm looking for the address of the College Of Engineering Cherthala.","How can I contact the admissions department of the College Of Engineering Cherthala?",
                        "I need to reach the financial aid office of College Of Engineering Cherthala. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Cherthala?","Do College Of Engineering Cherthala have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Cherthala official website for contact details?","How do I get in touch with the College Of Engineering Cherthala for general queries?"],
            "responses":
                ["College of Engineering, Cherthala Ottappunna, Pallippuram.P.O Cherthala-\n688541 \nPh : +91 478 2552714\n Ph : +91 478 2553416,\n E-mail :cecerthala@ihrd.ac.in\n web    : ceherthala.ihrd.ac.in"],
            "context": [""]
        },
        {
            "tag": "Cherthala",
            "patterns": ["Tell me about College Of Engineering Cherthala", "College Of Engineering Cherthala", "Cherthala",
                          "Details about College Of Engineering Cherthala"],
            "responses": [
                "Run by IHRD, College of Engineering, Cherthala has been the leading technical institution in Kerala since it’s venture in 2004. Affiliated to CUSAT, CE Cherthala offers M.Tech in Electronics Engineering (Signal Processing) and Computer Science Engineering (Computer and Information Science), B.Tech in Computer Science & Engineering, Electronics & Communication Engineering, reflecting the modern technological advancements through its updated syllabi. The institution is approved by AICTE, New Delhi and affiliated to CUSAT. It is under the management of IHRD (Institute of Human Resources Development) , a Kerala Government undertaking"],
            "context": [""]
        },
        {
            "tag": "Thrikkakkara Courses",
            "patterns": ["What courses are offered at Model Engineering College Thrikkakkara?" ,
                         "Tell me about the programs available at Model Engineering College Thrikkakkara" ,
                         "Can you list the available courses at Model Engineering College Thrikkakkara?" ,
                         "What are the academic programs at Model Engineering College Thrikkakkara?",
                         "Which degrees can I pursue at Model Engineering College Thrikkakkara?",
                         "Give me information on the available majors at Model Engineering College Thrikkakkara",
                         "What fields of study are available at Model Engineering College Thrikkakkara?",
                         "Tell me about the curriculum options provided by Model Engineering College Thrikkakkara"],
            "responses": ["M.Tech Courses =\n\n"
                          "Electronics Engineering (VLSI & Embedded Systems) : 24 seats per year\n"
                          "Electronics Engineering (Signal Processing) : 18 seats per year\n"
                          "Computer Science Engineering (Data Science ) : 18 seats per year\n"
                          "Mechanical Engineering( Energy Management) : 24 seats per year\n"
                          "B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 180 seats per year \n"
                          "Computer Science and Business Systems : 60 seats per year \n"
                          "Electrical & Electronics Engineering : 60 seats per year \n"
                          "Electronics & Communication Engineering : 60 seats per year \n"
                          "Electronics & Bio-Medical Engineering : 60 seats per year \n"
                          "Mechanical Engineering : 60 seats per year\n"],
            "context": [""]
        },
        {
            "tag": "Contact Thrikkakkara",
            "patterns": ["Can you provide me with the contact details for the Model Engineering College Thrikkakkara?",
                        "I need the contact information of the Model Engineering College Thrikkakkara, please.",
                        "How can I get in touch with the Model Engineering College Thrikkakkara?","What is the Model Engineering College Thrikkakkara phone number?",
                        "Please share the Model Engineering College Thrikkakkara email address.",
                        "I'm looking for the address of the Model Engineering College Thrikkakkara.","How can I contact the admissions department of the Model Engineering College Thrikkakkara?",
                        "I need to reach the financial aid office of Model Engineering College Thrikkakkara. What's their contact?",
                        "Is there a separate contact for the academic affairs department of Model Engineering College Thrikkakkara?","Do Model Engineering College Thrikkakkara have a website or social media where I can find contact information?",
                        "Can you direct me to the Model Engineering College Thrikkakkara official website for contact details?","How do I get in touch with the Model Engineering College Thrikkakkara for general queries?"],
            "responses":
                ["Model Engineering College, B.M.C. PO, Thrikkakkara, Kochi, Kerala State -\n Pin: 682021\n Phone:0484-2575370(O)\n Phone:0484-2577379(P) \nE-mail : mec@ihrd.ac.in \nweb : www.mec.ac.in"],
            "context": [""]
        },
        {
            "tag": "Thrikkakkara",
            "patterns": ["Tell me about Model Engineering College Thrikkakkara", "Model Engineering College Thrikkakkara", "Thrikkakkara",
                          "Details about Model Engineering College Thrikkakkara"],
            "responses": [
                "Model Engineering College was established in 1989 by the IHRD to provide quality engineering education in the industrial centre of Kerala. It was established as a self-financing college with a fair degree of autonomy. The college started functioning in August 1989 in the premises of High School, Edapally with Four degree courses in Biomedical , Computer Science, Electronics Engineering and Electrical engineering and Four Master degree  in Electronics Engineering (VLSI & Embedded Systems),Electronics Engineering (Signal Processing),Electronics Engineering (Opto Electronics),Computer Science & Engineering (Image Processing) . When it was started Model Engineering College was the first self-financing college under the Government of Kerala and was the first college affiliated to CUSAT. The college was shifted to the present campus at Thrikkakara in September 1994 and has grown into an institution of excellence"],
            "context": [""]
        },
        {
        "tag": "Kalloopara Faculty",
        "patterns": ["Tell me about the professors at College Of Engineering Kalloopara.",
                    "Can you provide information about the teaching staff of College Of Engineering Kalloopara?",
                    "Who are the faculty members here at College Of Engineering Kalloopara?",
                    "Give me details about the academic staff of College Of Engineering Kalloopara.",
                    "I'd like to learn more about the professors of College Of Engineering Kalloopara.",
                    "What can you tell me about the teachers at College Of Engineering Kalloopara?",
                    "Who makes up the faculty at College Of Engineering Kalloopara?",
                    "Tell me about the instructors of College Of Engineering Kalloopara.",
                    "Share some insights into the faculty members of College Of Engineering Kalloopara.",
                    "Can you list the names of the professors of College Of Engineering Kalloopara?"],
                     "responses": [
                         "Computer Science & Engineering\n\n"
                        "HOD: MANOJ RAY D\n"
                        "ASSOCIATE PROFESSOR\n\n"

                        "Facutly\n\n"

                        "Renjith S R\n"
                        "Designation :- Assistant Professor \n\n"

                        "Ajeesh S\n"
                        "Designation :- Assistant Professor\n\n"

                        "Indu P K\n"
                        "Designation :- Assistant Professor\n\n"

                        "Kala Karun\n"
                        "Designation :- Assistant Professor(on leave )\n\n"

                        "Sukanya M V\n"
                        "Designation :- Assistant Professor\n\n"

                        "Nivedya A R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Jinu L\n"
                        "Designation:- Assistant Professor\n\n"

                        "Marina G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Geethu Raju G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Revathy P\n"
                        "Designation:- Computer Programmer\n\n"

                        "Jisha R Chandran\n"
                        "Designation:- Computer Programmer\n\n"

                        "Swathy R S\n"
                        "Designation:- Demonstrator\n\n"

                        "Electronics & Communication Engineering\n\n"
                        "HOD\n"
                        "ANOOP S\n"
                        "ASSISTANT PROFESSOR\n\n"

                        "Faculty\n\n"

                        "Soumya G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Shahina S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Chithra Raveendran\n"
                        "Designation:- Assistant Professor\n\n"

                        "Chithra B R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sibu M. S.\n"
                        "Designation Tradesman\n\n"

                        "Athira Thampi\n"
                        "Designation:- Demonstrator\n\n"

                        "Raji R C\n"
                        "Designation:- Demonstrator\n\n"

                        "Applied Science\n\n"
                        "HOD\n"
                        "JAYALEKSHMI A\n"
                        "Assoc. Prof. in Mathematics\n\n"

                        "Manu Rajendran\n"
                        "Designation:- Assoc. Prof in Physical Education\n\n"

                        "Arya S\n"
                        "Designation:- Asst. Prof. in Physics\n\n"

                        "Anjali Vijay\n"
                        "Designation:- Asst. Prof. in English\n\n"

                        "General Engineering\n\n"
                        "HOD\n"
                        "Dr. ASIFSHA A\n"
                        "Asst Prof in Mechanical Engineering\n\n"

                        "ASHNA MARIA MARTIN\n"
                        "Designation:- Asst Prof in Civil Engineering\n\n"

                        "GEORGE PETER\n"
                        "Designation:- Tradesman in Mechanical\n\n"
                     ],
                      "context": [""]

        },
        {
        "tag": "Kalloopara ec",
        "patterns": ["Tell me about the professors in the Electronics and Communication Engineering department of V.",
                    "Who are the faculty members in the Electronics and Communication Engineering department of College Of Engineering Kalloopara?",
                    "Can you provide information on the teaching staff in Electronics and Communication Engineering at College Of Engineering Kalloopara?",
                    "Give me details about the Electronics and Communication Engineering department instructors of College Of Engineering Kalloopara.",
                    "I'd like to learn more about the professors teaching Electronics and Communication Engineering at College Of Engineering Kalloopara.",
                    "What can you tell me about the Electronics and Communication Engineering faculty of College Of Engineering Kalloopara?",
                    "Who makes up the staff in the Electronics and Communication Engineering of College Of Engineering Kalloopara?",
                    "Tell me about the Electronics and Communication Engineering instructors of College Of Engineering Kalloopara.",
                    "Share some insights into the Electronics and Communication Engineering staff of College Of Engineering Kalloopara.",
                    "Can you list the names of the professors in Electronics and Communication Engineering at College Of Engineering Kalloopara?"],
        "responses": ["Electronics & Communication Engineering\n\n"
                        "HOD: ANOOP S\n"
                        "ASSISTANT PROFESSOR\n\n"

                        "Faculty\n\n"

                        "Soumya G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Shahina S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Chithra Raveendran\n"
                        "Designation:- Assistant Professor\n\n"

                        "Chithra B R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sibu M. S.\n"
                        "Designation Tradesman\n\n"

                        "Athira Thampi\n"
                        "Designation:- Demonstrator\n\n"

                        "Raji R C\n"
                        "Designation:- Demonstrator\n\n"

                      ],
        "context": [""]

        },
       {
        "tag": "Kalloopara cse ",
        "patterns": ["Tell me about the professors in the Computer Science and Engineering department of Kalloopara.",
                    "Who are the faculty members in the Computer Science and Engineering department of College Of Engineering Kalloopara?",
                    "Can you provide information on the teaching staff in Computer Science and Engineering at College Of Engineering Kalloopara?",
                    "Give me details about the Computer Science and Engineering department instructors of College Of Engineering Kalloopara.",
                    "I'd like to learn more about the professors teaching Computer Science and Engineering at College Of Engineering Kalloopara.",
                    "What can you tell me about the Computer Science and Engineering faculty of College Of Engineering Kalloopara?",
                    "Who makes up the staff in the Computer Science and Engineering of College Of Engineering Kalloopara?",
                    "Tell me about the Computer Science and Engineering instructors of College Of Engineering Kalloopara.",
                    "Share some insights into the Computer Science and Engineering staff of College Of Engineering Kalloopara.",
                    "Can you list the names of the professors in Computer Science and Engineering at College Of Engineering Kalloopara?"],
        "responses": ["Computer Science and Engineering\n\n"
                      "HOD:MANOJ RAY D\n"
                        "ASSOCIATE PROFESSOR\n\n"

                        "Facutly\n\n"

                        "Renjith S R\n"
                        "Designation :- Assistant Professor \n\n"

                        "Ajeesh S\n"
                        "Designation :- Assistant Professor\n\n"

                        "Indu P K\n"
                        "Designation :- Assistant Professor\n\n"

                        "Kala Karun\n"
                        "Designation :- Assistant Professor(on leave )\n\n"

                        "Sukanya M V\n"
                        "Designation :- Assistant Professor\n\n"

                        "Nivedya A R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Jinu L\n"
                        "Designation:- Assistant Professor\n\n"

                        "Marina G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Geethu Raju G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Revathy P\n"
                        "Designation:- Computer Programmer\n\n"

                        "Jisha R Chandran\n"
                        "Designation:- Computer Programmer\n\n"

                        "Swathy R S\n"
                        "Designation:- Demonstrator\n\n"

                      ],
           "context": [""]

        },
        {
        "tag": "Kalloopara eee ",
        "patterns": ["Tell me about the professors in the Electrical and Electronics Engineering department of V.",
                    "Who are the faculty members in the Electrical and Electronics Engineering department of College Of Engineering Kalloopara?",
                    "Can you provide information on the teaching staff in Electrical and Electronics Engineering at College Of Engineering Kalloopara?",
                    "Give me details about the Electrical and Electronics Engineering department instructors of College Of Engineering Kalloopara.",
                    "I'd like to learn more about the professors teaching Electrical and Electronics Engineering at College Of Engineering Kalloopara.",
                    "What can you tell me about the Electrical and Electronics Engineering faculty of College Of Engineering Kalloopara?",
                    "Who makes up the staff in the Electrical and Electronics Engineering of College Of Engineering Kalloopara?",
                    "Tell me about the Electrical and Electronics Engineering instructors of College Of Engineering Kalloopara.",
                    "Share some insights into the Electrical and Electronics Engineering staff of College Of Engineering Kalloopara.",
                    "Can you list the names of the professors in Electrical and Electronics Engineering at College Of Engineering Kalloopara?"],
        "responses": ["Electrical and Electronics Engineering\n\n"
                      "HOD : Mr. JAISON JAMES\n"
                        "Designation :- Associate Professor\n\n"

                        "Mr. DEEPU V S\n"
                        "Designation :- Associate Professor\n\n"

                        "Ms. RESHMI RAVI K\n"
                        "Designation :- Associate Professor\n\n"

                        "Mr. JINCY J M\n"
                        "Designation :- Associate Professor\n\n"

                        "Ms. SINI S\n"
                        "Designation :- Associate Professor\n\n"

                        "Mr. BIJU P THOMAS\n"
                        "Designation:- Trade Instructor\n\n"

                        "Mr. RAHUL R BABU\n"
                        "Designation:- Demonstrator\n\n"

                        " Mr. JUBIN P ISSAC\n"
                        " Designation:- Tradesman\n\n"   ],
        },
        {
            "tag": "Kalloopara applied ",
                 "patterns": ["Tell me about the professors in the Applied Engineering department of College Of Engineering Kalloopara.",
                        "Who are the faculty members in the Applied Engineering department of College Of Engineering Kalloopara?",
                        "Can you provide information on the teaching staff in Applied Engineering at College Of Engineering Kalloopara?",
                        "Give me details about the Applied Engineering instructors of College Of Engineering Kalloopara.",
                        "I'd like to learn more about the professors teaching Applied Engineering at College Of Engineering Kalloopara.",
                        "What can you tell me about the Applied Engineering faculty of College Of Engineering Kalloopara?",
                        "Who makes up the staff in the Applied Engineering of College Of Engineering Kalloopara?",
                        "Tell me about the Applied Engineering instructors of College Of Engineering Kalloopara.",
                        "Share some insights into the Applied Engineering staff of College Of Engineering Kalloopara.",
                        "Can you list the names of the professors in Applied Engineering at College Of Engineering Kalloopara?"],
                 "responses": [ "APPLIED SCIENCES\n\n"
                               "HOD: JAYALEKSHMI A\n"
                                "Assoc. Prof. in Mathematics\n\n"

                                "Manu Rajendran\n"
                                "Designation:- Assoc. Prof in Physical Education\n\n"

                                "Arya S\n"
                                "Designation:- Asst. Prof. in Physics\n\n"

                                "Anjali Vijay\n"
                                "Designation:- Asst. Prof. in English\n\n"],
                                  "context": [""]

        },
        {
             "tag": "Kalloopara general ",
                 "patterns": ["Tell me about the professors in the General Engineering department of College Of Engineering Kalloopara.",
                        "Who are the faculty members in the General Engineering department of College Of Engineering Kalloopara?",
                        "Can you provide information on the teaching staff in General Engineering at College Of Engineering Kalloopara?",
                        "Give me details about the General Engineering instructors of College Of Engineering Kalloopara.",
                        "I'd like to learn more about the professors teaching General Engineering at College Of Engineering Kalloopara.",
                        "What can you tell me about the General Engineering faculty of College Of Engineering Kalloopara?",
                        "Who makes up the staff in the General Engineering of College Of Engineering Kalloopara?",
                        "Tell me about the General Engineering instructors of College Of Engineering Kalloopara.",
                        "Share some insights into the General Engineering staff of College Of Engineering Kalloopara.",
                        "Can you list the names of the professors in General Engineering at College Of Engineering Kalloopara?"],
                 "responses": ["GENERAL ENGINEERING\n\n"
                                "HOD:Dr. ASIFSHA A\n"
                                "Asst Prof in Mechanical Engineering\n\n"

                                "ASHNA MARIA MARTIN\n"
                                "Designation:- Asst Prof in Civil Engineering\n\n"

                                "GEORGE PETER\n"
                                "Designation:- Tradesman in Mechanical\n\n"

                               ],
                  "context": [""]

        },
        {
        "tag": "Kalloopara hod ",
            "patterns": ["I'd like to know who the HODs of the College Of Engineering Kalloopara.",
                        "Can you share the HODs' names for the departments of College Of Engineering Kalloopara ?",
                        "Can you tell me about the other department heads of College Of Engineering Kalloopara?",
                        "Could you give me an overview of the department heads of College Of Engineering Kalloopara?",
                        "Tell me about the leadership in the departments of College Of Engineering Kalloopara.",
                        "Provide information about the Heads of Departments in theCollege Of Engineering Kalloopara"],
            "responses": ["Computer Science & Engineering\n\n"
                            "HOD:MANOJ RAY D\n"
                            "ASSOCIATE PROFESSOR\n\n"

                            "Department of Electronics and Communication Engineering\n\n"
                            "HOD : Dr. SHANAVAZ K T\n"
                            "Designation :-Associate Professor\n\n"


                            "Electrical & Electronics Engineering\n\n"
                            "HOD : Mr. JAISON JAMES\n"
                            "Designation :- Associate Professor\n\n"


                            "Applied Science\n\n"
                            "HOD: JAYALEKSHMI A\n"
                            "Assoc. Prof. in Mathematics\n\n"


                            "General Engineering\n\n"
                            "HOD:Dr. ASIFSHA A\n"
                            "Asst Prof in Mechanical Engineering\n\n" ],
            "context": [""]
        },
         {
            "tag": "Kalloopara Courses",
            "patterns": ["What courses are offered at College Of Engineering Kalloopara?" ,
                         "Tell me about the programs available at College Of Engineering Kalloopara" ,
                         "Can you list the available courses at College Of Engineering Kalloopara?" ,
                         "What are the academic programs at College Of Engineering Kalloopara?",
                         "Which degrees can I pursue at College Of Engineering Kalloopara?",
                         "Give me information on the available majors at College Of Engineering Kalloopara",
                         "What fields of study are available at College Of Engineering Kalloopara?",
                         "Tell me about the curriculum options provided by College Of Engineering Kalloopara"],
            "responses": ["M.Tech Courses =\n\n"
                          "Computer Science with specialization in Cyber Forensics and Information Security : 18 seats per year\n\n"
                          "B.Tech Courses = \n"
                          "Computer Science & Engineering : 60 seats per year \n"
                          "Electrical & Electronics Engineering : 60 seats per year \n"
                          "Electronics & Communication Engineering : 60 seats per year \n\n"
                          "B.Voc/ D.Voc Courses =\n\n"
                          "B.Voc =\n"
                          "Electronics Manufacturing Services : 30 seats per year \n"
                          "Software Development : 30 seats per year\n\n"
                          "D.Voc\n"
                          "Electronics Manufacturing Services : 30 seats per year\n"
                          "Software Development : 30 seats per year\n"],
            "context": [""]
        },
        {
            "tag": "Contact Kalloopara",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Kalloopara?",
                        "I need the contact information of the College Of Engineering Kalloopara, please.",
                        "How can I get in touch with the College Of Engineering Kalloopara?","What is the College Of Engineering Kalloopara phone number?",
                        "Please share the College Of Engineering Kalloopara email address.",
                        "I'm looking for the address of the College Of Engineering Kalloopara.","How can I contact the admissions department of the College Of Engineering Kalloopara?",
                        "I need to reach the financial aid office of College Of Engineering Kalloopara. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Kalloopara?","Do College Of Engineering Kalloopara have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Kalloopara official website for contact details?","How do I get in touch with the College Of Engineering Kalloopara for general queries?"],
            "responses":
                ["College of Engineering, Kallooppara, Kadamankulam.P.O. Thiruvalla (Via) Pathanamthitta Dist. Kerala State\n Pin- 689 583 \nPhone: 0469-2677890(P) \nPhone: 0469-2678983(O) \nMobile : 8547005034 \nE-mail : principal@cek,ac.in\n web : cek.ac.in"],
            "context": [""]
        },
         {
            "tag": "Kalloopara",
           "patterns": ["Tell me about College Of Engineering Kalloopara", "College Of Engineering Kalloopara", "Kalloopara",
                          "Details about College Of Engineering Kalloopara"],
            "responses": [
                "College of Engineering Kallooppara located in the Sylvan hills of Pathanamthitta district, is one of the premier institutions among the new generation Engineering colleges of South India . Ever since its inception in 2004 under the aegis of the Institute of Human Resources Development (IHRD-a Govt. of Kerala undertaking) the college has already made its presence felt in the technical horizon of the State. The institution offers undergraduate courses in three of the modern streams in Engineering viz, Electronics & communications, Computer Science & Engineering and Information Technology and PG  Courses in Cyber Forensics and Information Security"],
            "context": [""]
        },
           {
            "tag": "KNP Faculty",
            "patterns": ["Tell me about the professors at College Of Engineering Karunagappaly.",
                        "Can you provide information about the teaching staff of College Of Engineering Karunagappaly?",
                        "Who are the faculty members here at College Of Engineering Karunagappaly?",
                        "Give me details about the academic staff of College Of Engineering Karunagappaly.",
                        "I'd like to learn more about the professors of College Of Engineering Karunagappaly.",
                        "What can you tell me about the teachers at College Of Engineering Karunagappaly?",
                        "Who makes up the faculty at College Of Engineering Karunagappaly?",
                        "Tell me about the instructors of College Of Engineering Karunagappaly.",
                        "Share some insights into the faculty members of College Of Engineering Karunagappaly.",
                        "Can you list the names of the professors of College Of Engineering Karunagappaly?"],
            "responses":  [
                            "Computer Science and Engineering\n\n"

                                "Faculty\n\n"

                                "HOD : Dr. Smitha P.\n"
                                "Associate Professor ( Cadre)\n\n"

                                "Dancy Kurian\n"
                                "Assistant Professor\n\n"

                                "SHEEJA Y.S.\n"
                                "Assistant Professor\n\n"

                                "SABEENA K.\n"
                                "Assistant Professor\n\n"

                                "VINOD R.\n"
                                "Assistant Professor\n\n"

                                "Dr. JYOTHI R.L.\n"
                                "Assistant Professor\n\n"

                                "Dr. SHANI RAJ\n"
                                "Assistant Professor\n\n"

                                "AJIMI AMEER\n"
                                "Assistant Professor\n\n"

                                "NEETHU SAJEEV\n"
                                "Assistant Professor\n\n"

                                "BUSHRA BEEVI A\n"
                                "Assistant Professor\n\n"

                                "RESMI M R\n"
                                "Assistant Professor (Adhoc)\n\n"

                                "SHEHSA A. SHUKKOOR\n"
                                "Assistant Professor (Adhoc)\n\n"

                                "Staffs\n\n"


                                "SHIBU V\n"
                                "Foreman\n\n"


                                "APARNA A.R\n"
                                "Computer Programmer\n\n"


                                "ATHIRA A\n"
                                "Computer Programmer\n\n"


                                "SAJIN PRASAD\n"
                                "Demonstrator\n\n"


                                "ELECTRONICS AND COMMUNICATION\n\n"
                                "Faculty\n\n"

                                "C V ANIL KUMAR\n"
                                "Principal\n\n"


                                "HOD : Dr. GOPAKUMAR C.\n"
                                "Associate Professor ( Cadre)\n\n"


                                "Dr. T E AYOOB KHAN\n"
                                "Associate Professor ( Cadre)\n\n"


                                "SALINI S.\n"
                                "Associate Professor ( Non Cadre)\n\n"


                                "SHINY C\n"
                                "Assistant Professor\n\n"


                                "REJU JOHN\n"
                                "Assistant Professor\n\n"


                                "JIBU J V\n"
                                "Assistant Professor\n\n"


                                "staff\n\n"

                                "RADHAKRISHNAPILLAI P B\n"
                                "Trade Instructor\n\n"


                                "JYOTHILEKSHMI.L\n"
                                "Demonstrator\n\n"


                                "Electrical Engineering\n\n"

                                "HOD : LIBI A.\n"
                                "Assistant Professor\n\n"


                                "HASEENA P .Y."
                                "Assistant Professor\n\n"


                                "ARATHI P D\n"
                                "Assistant Professor\n\n"

                                "SHEENA K\n"
                                "Assistant Professor\n\n"


                                "ARYA V KURUP\n"
                                "Assistant Professor\n\n"


                                "THARA MURALI\n"
                                "Assistant Professor\n\n"


                                "LULU JOSEPH\n"
                                "Assistant Professor\n\n"


                                "SUMAYYA N\n"
                                "Assistant Professor\n\n"


                                "RADHIKA R CHANDRAN\n"
                                "Assistant Professor\n\n"


                                "PREEMA R. CHANDRAN\n"
                                "Assistant Professor\n\n"


                                "Staff\n"
                                "ANILKUMAR V\n"
                                "Trade Instructor\n\n"


                                "Mechanical Enginereenig\n"

                                "Dr. AJILKUMAR A.\n"
                                "Associate Professor ( Cadre)\n\n"

                                "MANU M.JOHN\n"
                                "Assistant Professor\n\n"


                                "PREMNATH G\n"
                                "Assistant Professor\n\n"


                                "FATHIMA B NAZAR\n"
                                "Assistant Professor\n\n"


                                "AKASH R.S.\n"
                                "Assistant Professor\n\n"


                                "ASWIN R\n"
                                "Assistant Professor\n\n"


                                "GAUTHAM CHAND M\n"
                                "Assistant Professor\n\n"


                                "RAJESH KUMAR G\n"
                                "Demonstrator\n\n"


                                "APPLIED SCIENCE\n"

                                "SHEELA R.\n"
                                "Assistant Professor\n\n"


                                "Dr JOHNSY S PRASAD\n"
                                "Professor\n\n"


                                "PREMAKUMARI K. R.\n"
                                "Associate Professor ( Non Cadre)\n\n"

                                "LEKSHMI KRISHNAN\n"
                                "Assistant Professor\n\n"



                            ],
                                        "context": [""]


        },
       {
        "tag": "KNP cse ",
        "patterns": ["Tell me about the professors in the Computer Science and Engineering department of Karunagappally.",
                    "Who are the faculty members in the Computer Science and Engineering department of College Of Engineering Karunagappally?",
                    "Can you provide information on the teaching staff in Computer Science and Engineering at College Of Engineering Karunagappally?",
                    "Give me details about the Computer Science and Engineering department instructors of College Of Engineering Karunagappally.",
                    "I'd like to learn more about the professors teaching Computer Science and Engineering at College Of Engineering Karunagappally.",
                    "What can you tell me about the Computer Science and Engineering faculty of College Of Engineering Karunagappally?",
                    "Who makes up the staff in the Computer Science and Engineering of College Of Engineering Karunagappally?",
                    "Tell me about the Computer Science and Engineering instructors of College Of Engineering Karunagappally.",
                    "Share some insights into the Computer Science and Engineering staff of College Of Engineering Karunagappally.",
                    "Can you list the names of the professors in Computer Science and Engineering at College Of Engineering Karunagappally?"],
        "responses": [
                            "Computer Science and Engineering\n\n"

                            "Faculty\n\n"

                            "HOD : Dr. Smitha P.\n"
                            "Associate Professor ( Cadre)\n"

                            "Dancy Kurian\n"
                            "Assistant Professor\n\n"

                            "SHEEJA Y.S.\n"
                            "Assistant Professor\n\n"

                            "SABEENA K.\n"
                            "Assistant Professor\n\n"

                            "VINOD R.\n"
                            "Assistant Professor\n\n"

                            "Dr. JYOTHI R.L.\n"
                            "Assistant Professor\n\n"

                            "Dr. SHANI RAJ\n"
                            "Assistant Professor\n\n"

                            "AJIMI AMEER\n"
                            "Assistant Professor\n\n"

                            "NEETHU SAJEEV\n"
                            "Assistant Professor\n\n"

                            "BUSHRA BEEVI A\n"
                            "Assistant Professor\n\n"

                            "RESMI M R\n"
                            "Assistant Professor (Adhoc)\n\n"

                            "SHEHSA A. SHUKKOOR\n"
                            "Assistant Professor (Adhoc)\n\n"

                            "Staffs\n\n"


                            "SHIBU V\n"
                            "Foreman\n\n"


                            "APARNA A.R\n"
                            "Computer Programmer\n\n"


                            "ATHIRA A\n"
                            "Computer Programmer\n\n"


                            "SAJIN PRASAD\n"
                            "Demonstrator\n\n"          ],
                                                "context": [""]

        },
         {
            "tag": "KNP cse ",
            "patterns": ["Tell me about the professors in the Computer Science and Engineering department of College Of Engineering Karunagappally.",
                        "Who are the faculty members in the Computer Science and Engineering department of College Of Engineering Karunagappally?",
                        "Can you provide information on the teaching staff in Computer Science and Engineering at College Of Engineering Karunagappally?",
                        "Give me details about the Computer Science and Engineering department instructors of College Of Engineering Karunagappally.",
                        "I'd like to learn more about the professors teaching Computer Science and Engineering at College Of Engineering Karunagappally.",
                        "What can you tell me about the Computer Science and Engineering faculty of College Of Engineering Karunagappally?",
                        "Who makes up the staff in the Computer Science and Engineering of College Of Engineering Karunagappally?",
                        "Tell me about the Computer Science and Engineering instructors of College Of Engineering Karunagappally.",
                        "Share some insights into the Computer Science and Engineering staff of College Of Engineering Karunagappally.",
                        "Can you list the names of the professors in Computer Science and Engineering at College Of Engineering Karunagappally?"],
            "responses": [
                                "ELECTRONICS AND COMMUNICATION\n\n"
                                "Faculty\n\n"

                                "C V ANIL KUMAR\n"
                                "Principal\n\n"


                                "HOD : Dr. GOPAKUMAR C.\n"
                                "Associate Professor ( Cadre)\n\n"


                                "Dr. T E AYOOB KHAN\n"
                                "Associate Professor ( Cadre)\n\n"


                                "SALINI S.\n"
                                "Associate Professor ( Non Cadre)\n\n"


                                "SHINY C\n"
                                "Assistant Professor\n\n"


                                "REJU JOHN\n"
                                "Assistant Professor\n\n"


                                "JIBU J V\n"
                                "Assistant Professor\n\n"


                                "staff\n\n"

                                "RADHAKRISHNAPILLAI P B\n"
                                "Trade Instructor\n\n"


                                "JYOTHILEKSHMI.L\n"
                                "Demonstrator\n\n"
                          ],
                                                            "context": [""]

        },
         {
        "tag": "KNP eee ",
        "patterns": ["Tell me about the professors in the Electrical Engineering department of College Of Engineering Karunagappally.",
                    "Who are the faculty members in the Electrical Engineering department of College Of Engineering Karunagappally?",
                    "Can you provide information on the teaching staff in Electrical Engineering at College Of Engineering Karunagappally?",
                    "Give me details about the Electrical Engineering instructors of College Of Engineering Karunagappally.",
                    "I'd like to learn more about the professors teaching Electrical Engineering at College Of Engineering Karunagappally.",
                    "What can you tell me about the Electrical Engineering faculty of College Of Engineering Karunagappally?",
                    "Who makes up the staff in the Electrical Engineering of College Of Engineering Karunagappally?",
                    "Tell me about the Electrical Engineering instructors of College Of Engineering Karunagappally.",
                    "Share some insights into the Electrical Engineering staff of College Of Engineering Karunagappally.",
                    "Can you list the names of the professors in Electrical Engineering at College Of Engineering Karunagappally?"],
        "responses": [
                                "Electrical Engineering\n\n"

                                "HOD : LIBI A.\n"
                                "Assistant Professor\n\n"


                                "HASEENA P .Y."
                                "Assistant Professor\n\n"


                                "ARATHI P D\n"
                                "Assistant Professor\n\n"

                                "SHEENA K\n"
                                "Assistant Professor\n\n"


                                "ARYA V KURUP\n"
                                "Assistant Professor\n\n"


                                "THARA MURALI\n"
                                "Assistant Professor\n\n"


                                "LULU JOSEPH\n"
                                "Assistant Professor\n\n"


                                "SUMAYYA N\n"
                                "Assistant Professor\n\n"


                                "RADHIKA R CHANDRAN\n"
                                "Assistant Professor\n\n"


                                "PREEMA R. CHANDRAN\n"
                                "Assistant Professor\n\n"


                                "Staff\n"
                                "ANILKUMAR V\n"
                                "Trade Instructor\n\n" ],
                                                                    "context": [""]

        },
         {
        "tag": "KNP mech",
        "patterns": ["Tell me about the professors in the mechanical department of V.",
                    "Who are the faculty members in the mechanical engineering department of College Of Engineering Karunagappally?",
                    "Can you provide information on the teaching staff in mechanical engineering at College Of Engineering Karunagappally?",
                    "Give me details about the mechanical department instructors of College Of Engineering Karunagappally.",
                    "I'd like to learn more about the professors teaching mechanical engineering at College Of Engineering Karunagappally.",
                    "What can you tell me about the mechanical engineering faculty of College Of Engineering Karunagappally?",
                    "Who makes up the staff in the mechanical department of College Of Engineering Karunagappally?",
                    "Tell me about the mechanical engineering instructors of College Of Engineering Karunagappally.",
                    "Share some insights into the mechanical department staff of College Of Engineering Karunagappally.",
                    "Can you list the names of the professors in mechanical engineering at College Of Engineering Karunagappally?"],
        "responses": [
                            "Mechanical Enginereenig\n"

                            "Dr. AJILKUMAR A.\n"
                            "Associate Professor ( Cadre)\n\n"

                            "MANU M.JOHN\n"
                            "Assistant Professor\n\n"


                            "PREMNATH G\n"
                            "Assistant Professor\n\n"


                            "FATHIMA B NAZAR\n"
                            "Assistant Professor\n\n"


                            "AKASH R.S.\n"
                            "Assistant Professor\n\n"


                            "ASWIN R\n"
                            "Assistant Professor\n\n"


                            "GAUTHAM CHAND M\n"
                            "Assistant Professor\n\n"


                            "RAJESH KUMAR G\n"
                            "Demonstrator\n\n"
                      ],
                 "context": [""]
         },
          {
            "tag": "KNP applied ",
                 "patterns": ["Tell me about the professors in the Applied Engineering department of College Of Engineering Karunagapplly.",
                        "Who are the faculty members in the Applied Engineering department of College Of Engineering Karunagapplly?",
                        "Can you provide information on the teaching staff in Applied Engineering at College Of Engineering Karunagapplly?",
                        "Give me details about the Applied Engineering instructors of College Of Engineering Karunagapplly.",
                        "I'd like to learn more about the professors teaching Applied Engineering at College Of Engineering Karunagapplly.",
                        "What can you tell me about the Applied Engineering faculty of College Of Engineering Karunagappally?",
                        "Who makes up the staff in the Applied Engineering of College Of Engineering Karunagappally?",
                        "Tell me about the Applied Engineering instructors of College Of Engineering Karunagappally.",
                        "Share some insights into the Applied Engineering staff of College Of Engineering Karunagappally.",
                        "Can you list the names of the professors in Applied Engineering at College Of Engineering Karunagappally?"],
                 "responses": [
                                    "APPLIED SCIENCE\n"

                                    "SHEELA R.\n"
                                    "Assistant Professor\n\n"


                                    "Dr JOHNSY S PRASAD\n"
                                    "Professor\n\n"


                                    "PREMAKUMARI K. R.\n"
                                    "Associate Professor ( Non Cadre)\n\n"

                                    "LEKSHMI KRISHNAN\n"
                                    "Assistant Professor\n\n"
                               ],
                                  "context": [""]

         },
          {
            "tag": "Karunagappally hod ",
            "patterns": ["I'd like to know who the HODs of the College Of Engineering Karunagappally.",
                        "Can you share the HODs' names for the departments of College Of Engineering Karunagappally ?",
                        "Can you tell me about the other department heads of College Of Engineering Karunagappally?",
                        "Could you give me an overview of the department heads of College Of Engineering Karunagappally?",
                        "Tell me about the leadership in the departments of College Of Engineering Karunagappally.",
                        "Provide information about the Heads of Departments in theCollege Of Engineering Karunagappally."],
            "responses": [
                            "Computer Science and Engineering\n\n"

                            "DR,SMITHA P.\n"
                            "Associate Professor ( Cadre)\n"
                            "Department of Computer Science and Engineering,\n"
                            "College Of Engineering\n"
                            "Karunagappally\n\n"


                            "Electronics and Communication\n\n"

                            "Dr. GOPAKUMAR C.\n"
                            "Associate Professor ( Cadre)\n"
                            "Department of Electronics and Communication,\n"
                            "College Of Engineering\n"
                            "Karunagappally\n\n"


                            "Electrical and Electronics Engineering\n\n"

                            "LIBI A.\n"
                            "Assistant Professor\n"
                            "Department of Electrical Engineering,\n"
                            "College Of Engineering\n"
                            "Karunagappally\n\n"



                            "Applied Sciences\n\n"

                            "SAJEEVAN.M\n"
                            "Associate Professor ( Non Cadre)\n"
                            "Department of Applied Sciences,\n"
                            "College Of Engineering\n"
                            "Karunagappally\n\n"


                            "Mechanical Engineering\n\n"

                            "Dr. AJILKUMAR A.\n"
                            "Associate Professor ( Cadre)\n"
                            "Department of Mechanical Engineering,\n"
                            "College Of Engineering\n"
                            "Karunagappally\n\n"
                                                                        ],
                                              "context": [""]

         },
         {
            "tag": "Karunagappally Courses",
            "patterns": ["What courses are offered at College Of Engineering Karunagappally?" ,
                         "Tell me about the programs available at College Of Engineering Karunagappally" ,
                         "Can you list the available courses at College Of Engineering Karunagappally?" ,
                         "What are the academic programs at College Of Engineering Karunagappally?",
                         "Which degrees can I pursue at College Of Engineering Karunagappally?",
                         "Give me information on the available majors at College Of Engineering Karunagappally",
                         "What fields of study are available at College Of Engineering Karunagappally?",
                         "Tell me about the curriculum options provided by College Of Engineering Karunagappally"],
            "responses": ["M.Tech Courses =\n\n "
                          "Electronics with specialization in Signal Processing : 24 seats per year\n"
                          "Computer Science with specialization in Image Processing 24 seats per year\n\n"
                          "B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 120 seats per year \n"
                          "Electrical & Electronics Engineering : 60 seats per year \n"
                          "Electronics & Communication Engineering : 30 seats per year \n"
                          "Mechanical Engineering : 60 seats epr year\n\n"
                          "D.Voc Courses =\n\n"
                          "Artficial Intelligence and Robotics 30 seats per year\n"
                          "Computer Hardware and Networking	: 30 seats per year\n"],
            "context": [""]
        },
         {
            "tag": "Contact Karunagappally",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Karunagappally?",
                        "I need the contact information of the College Of Engineering Karunagappally, please.",
                        "How can I get in touch with the College Of Engineering Karunagappally?","What is the College Of Engineering Karunagappally phone number?",
                        "Please share the College Of Engineering Karunagappally email address.",
                        "I'm looking for the address of the College Of Engineering Karunagappally.","How can I contact the admissions department of the College Of Engineering Karunagappally?",
                        "I need to reach the financial aid office of College Of Engineering Karunagappally. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Karunagappally?","Do College Of Engineering Karunagappally have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Karunagappally official website for contact details?","How do I get in touch with the College Of Engineering Karunagappally for general queries?"],
            "responses":
                ["College of Engineering, Thodiyoor P.O Karunagappally, Kollam Dist. \n Pin. 690523.\n Phone: 0476- 2666160(P)\n Phone: 0476- 2665935(O) \nE-mail : cekarunagappally@ihrd.ac.in \nweb : www.ceknpy.ac.in"],
            "context": [""]
        },
         {
            "tag": "Karunagappally",
           "patterns": ["Tell me about College Of Engineering Karunagappally", "College Of Engineering Karunagappally", "Karunagappally",
                          "Details about College Of Engineering Karunagappally"],
            "responses": [
                "Run by IHRD, College of Engineering, Karunagappally has been the leading technical institution in Kerala since it's venture in 2000. Affiliated to CUSAT, CE Karunagappallay offers M.Tech in Electronics Engineering ( Signal Processing)  and Computer Science (Image Processing). B.Tech in Computer Science & Engineering, Electronics & Communication Engineering and Information Technology reflecting the modern technological advancements through its updated syllabi.The institution is approved by AICTE, New Delhi and affiliated to CUSAT. It is under the management of IHRD ( Institute of Human Resources Development ), a Kerala Government undertaking."],
            "context": [""]
         },
         {
            "tag": "Kottarakkara Faculty",
            "patterns": ["Tell me about the professors at College Of Engineering Kottarakkara.",
                        "Can you provide information about the teaching staff of College Of Engineering Kottarakkara?",
                        "Who are the faculty members here at College Of Engineering Kottarakkara?",
                        "Give me details about the academic staff of College Of Engineering Kottarakkara.",
                        "I'd like to learn more about the professors of College Of Engineering Kottarakkara.",
                        "What can you tell me about the teachers at College Of Engineering Kottarakkara?",
                        "Who makes up the faculty at College Of Engineering Kottarakkara?",
                        "Tell me about the instructors of College Of Engineering Kottarakkara.",
                        "Share some insights into the faculty members of College Of Engineering Kottarakkara.",
                        "Can you list the names of the professors of College Of Engineering Kottarakkara?"],
            "responses": ["Computer Science & Engineering\n\n"
                            "HOD :MANOJ RAY D\n"
                            "ASSOCIATE PROFESSOR\n\n"

                            "Facutly\n\n"

                            "Renjith S R\n"
                            "Designation :- Assistant Professor \n\n"

                            "Ajeesh S\n"
                            "Designation :- Assistant Professor\n\n"

                            "Indu P K\n"
                            "Designation :- Assistant Professor\n\n"

                            "Kala Karun\n"
                            "Designation :- Assistant Professor(on leave )\n\n"

                            "Sukanya M V\n"
                            "Designation :- Assistant Professor\n\n"

                            "Nivedya A R\n"
                            "Designation:- Assistant Professor\n\n"

                            "Jinu L\n"
                            "Designation:- Assistant Professor\n\n"

                            "Marina G\n"
                            "Designation:- Assistant Professor\n\n"

                            "Geethu Raju G\n"
                            "Designation:- Assistant Professor\n\n"

                            "Revathy P\n"
                            "Designation:- Computer Programmer\n\n"

                            "Jisha R Chandran\n"
                            "Designation:- Computer Programmer\n\n"

                            "Swathy R S\n"
                            "Designation:- Demonstrator\n\n"

                            "Electronics & Communication Engineering\n\n"
                            "HOD\n"
                            "ANOOP S\n"
                            "ASSISTANT PROFESSOR\n\n"

                            "Faculty\n\n"

                            "Soumya G\n"
                            "Designation:- Assistant Professor\n\n"

                            "Shahina S\n"
                            "Designation:- Assistant Professor\n\n"

                            "Chithra Raveendran\n"
                            "Designation:- Assistant Professor\n\n"

                            "Chithra B R\n"
                            "Designation:- Assistant Professor\n\n"

                            "Sibu M. S.\n"
                            "Designation Tradesman\n\n"

                            "Athira Thampi\n"
                            "Designation:- Demonstrator\n\n"

                            "Raji R C\n"
                            "Designation:- Demonstrator\n\n"

                            "Applied Science\n\n"
                            "HOD\n"
                            "JAYALEKSHMI A\n"
                            "Assoc. Prof. in Mathematics\n\n"

                            "Manu Rajendran\n"
                            "Designation:- Assoc. Prof in Physical Education\n\n"

                            "Arya S\n"
                            "Designation:- Asst. Prof. in Physics\n\n"

                            "Anjali Vijay\n"
                            "Designation:- Asst. Prof. in English\n\n"

                            "General Engineering\n\n"
                            "HOD\n"
                            "Dr. ASIFSHA A\n"
                            "Asst Prof in Mechanical Engineering\n\n"

                            "ASHNA MARIA MARTIN\n"
                            "Designation:- Asst Prof in Civil Engineering\n\n"

                            "GEORGE PETER\n"
                            "Designation:- Tradesman in Mechanical\n\n"],
            "context": [""]
        },
         {
            "tag": "Kottarakkara cse ",
            "patterns": ["Tell me about the professors in the Computer Science & Engineering department of College Of Engineering Kottarakkara.",
                        "Who are the faculty members in the Computer Science & Engineering department of College Of Engineering Kottarakkara?",
                        "Can you provide information on the teaching staff in Computer Science & Engineering at College Of Engineering Kottarakkara?",
                        "Give me details about the Computer Science & Engineering instructors of College Of Engineering Kottarakkara.",
                        "I'd like to learn more about the professors teaching Computer Science & Engineering at College Of Engineering Kottarakkara.",
                        "What can you tell me about the Computer Science & Engineering faculty of College Of Engineering Kottarakkara?",
                        "Who makes up the staff in the Computer Science & Engineering of College Of Engineering Kottarakkara?",
                        "Tell me about the Computer Science & Engineering instructors of College Of Engineering Kottarakkara.",
                        "Share some insights into the Computer Science & Engineering staff of College Of Engineering Kottarakkara.",
                        "Can you list the names of the professors in Computer Science & Engineering at College Of Engineering Kottarakkara?"],
            "responses": ["Computer Science & Engineering\n\n"
                        "HOD : MANOJ RAY D\n"
                        "ASSOCIATE PROFESSOR\n\n"

                        "Facutly\n\n"

                        "Renjith S R\n"
                        "Designation :- Assistant Professor \n\n"

                        "Ajeesh S\n"
                        "Designation :- Assistant Professor\n\n"

                        "Indu P K\n"
                        "Designation :- Assistant Professor\n\n"

                        "Kala Karun\n"
                        "Designation :- Assistant Professor(on leave )\n\n"

                        "Sukanya M V\n"
                        "Designation :- Assistant Professor\n\n"

                        "Nivedya A R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Jinu L\n"
                        "Designation:- Assistant Professor\n\n"

                        "Marina G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Geethu Raju G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Revathy P\n"
                        "Designation:- Computer Programmer\n\n"

                        "Jisha R Chandran\n"
                        "Designation:- Computer Programmer\n\n"

                        "Swathy R S\n"
                        "Designation:- Demonstrator\n\n"],
            "context": [""]
         },
        {
            "tag": "Kottarakkara ece ",
            "patterns": ["Tell me about the professors in the Electronics & Communication Engineering department of College Of Engineering Kottarakkara.",
                        "Who are the faculty members in the Electronics & Communication Engineering department of College Of Engineering Kottarakkara?",
                        "Can you provide information on the teaching staff in Electronics & Communication Engineering at College Of Engineering Kottarakkara?",
                        "Give me details about the Electronics & Communication Engineering instructors of College Of Engineering Kottarakkara.",
                        "I'd like to learn more about the professors teaching Electronics & Communication Engineering at College Of Engineering Kottarakkara.",
                        "What can you tell me about the Electronics & Communication Engineering faculty of College Of Engineering Kottarakkara?",
                        "Who makes up the staff in the Electronics & Communication Engineering of College Of Engineering Kottarakkara?",
                        "Tell me about the Electronics & Communication Engineering instructors of College Of Engineering Kottarakkara.",
                        "Share some insights into the Electronics & Communication Engineering staff of College Of Engineering Kottarakkara.",
                        "Can you list the names of the professors in Electronics & Communication Engineering at College Of Engineering Kottarakkara?"],
            "responses": ["Electronics & Communication Engineering\n\n"
                        "HOD : ANOOP S\n"
                        "ASSISTANT PROFESSOR\n\n"

                        "Faculty\n\n"

                        "Soumya G\n"
                        "Designation:- Assistant Professor\n\n"

                        "Shahina S\n"
                        "Designation:- Assistant Professor\n\n"

                        "Chithra Raveendran\n"
                        "Designation:- Assistant Professor\n\n"

                        "Chithra B R\n"
                        "Designation:- Assistant Professor\n\n"

                        "Sibu M. S.\n"
                        "Designation Tradesman\n\n"

                        "Athira Thampi\n"
                        "Designation:- Demonstrator\n\n"

                        "Raji R C\n"
                        "Designation:- Demonstrator\n\n"],
            "context": [""]
         },
        {
            "tag": "Kottarakkara as ",
            "patterns": ["Tell me about the professors in the Applied Science department of College Of Engineering Kottarakkara.",
                        "Who are the faculty members in the Applied Science department of College Of Engineering Kottarakkara?",
                        "Can you provide information on the teaching staff in Applied Science at College Of Engineering Kottarakkara?",
                        "Give me details about the Applied Science instructors of College Of Engineering Kottarakkara.",
                        "I'd like to learn more about the professors teaching Applied Science at College Of Engineering Kottarakkara.",
                        "What can you tell me about the Applied Science faculty of College Of Engineering Kottarakkara?",
                        "Who makes up the staff in the Applied Science of College Of Engineering Kottarakkara?",
                        "Tell me about the Applied Science instructors of College Of Engineering Kottarakkara.",
                        "Share some insights into the Applied Science staff of College Of Engineering Kottarakkara.",
                        "Can you list the names of the professors in Applied Science at College Of Engineering Kottarakkara?"],
            "responses": ["Applied Science\n\n"
                        "HOD : JAYALEKSHMI A\n"
                        "Assoc. Prof. in Mathematics\n\n"

                        "Manu Rajendran\n"
                        "Designation:- Assoc. Prof in Physical Education\n\n"

                        "Arya S\n"
                        "Designation:- Asst. Prof. in Physics\n\n"

                        "Anjali Vijay\n"
                        "Designation:- Asst. Prof. in English\n\n"],
            "context": [""]
         },
        {
            "tag": "Kottarakkara ge ",
            "patterns": ["Tell me about the professors in the General Engineering department of College Of Engineering Kottarakkara.",
                        "Who are the faculty members in the General Engineering department of College Of Engineering Kottarakkara?",
                        "Can you provide information on the teaching staff in General Engineering at College Of Engineering Kottarakkara?",
                        "Give me details about the General Engineering instructors of College Of Engineering Kottarakkara.",
                        "I'd like to learn more about the professors teaching General Engineering at College Of Engineering Kottarakkara.",
                        "What can you tell me about the General Engineering faculty of College Of Engineering Kottarakkara?",
                        "Who makes up the staff in the General Engineering of College Of Engineering Kottarakkara?",
                        "Tell me about the General Engineering instructors of College Of Engineering Kottarakkara.",
                        "Share some insights into the General Engineering staff of College Of Engineering Kottarakkara.",
                        "Can you list the names of the professors in General Engineering at College Of Engineering Kottarakkara?"],
            "responses": ["General Engineering\n\n"
                        "HOD : Dr. ASIFSHA A\n"
                        "Asst Prof in Mechanical Engineering\n\n"

                        "ASHNA MARIA MARTIN\n"
                        "Designation:- Asst Prof in Civil Engineering\n\n"

                        "GEORGE PETER\n"
                        "Designation:- Tradesman in Mechanical\n\n"],
            "context": [""]
         },
        {
            "tag": "Kottarakkara hod ",
            "patterns": ["I'd like to know who the HODs of the College Of Engineering Kottarakkara.",
                        "Can you share the HODs' names for the departments of College Of Engineering Kottarakkara ?",
                        "Can you tell me about the other department heads of College Of Engineering Kottarakkara?",
                        "Could you give me an overview of the department heads of College Of Engineering Kottarakkara?",
                        "Tell me about the leadership in the departments of College Of Engineering Kottarakkara.",
                        "Provide information about the Heads of Departments in theCollege Of Engineering Kottarakkara."],
            "responses": ["Computer Science & Engineering\n\n"
                            "HOD : MANOJ RAY D\n"
                            "ASSOCIATE PROFESSOR\n\n"

                            "Electronics & Communication Engineering\n\n"
                            "HOD : ANOOP S\n"
                            "ASSISTANT PROFESSOR\n\n"

                            "Applied Science\n\n"
                            "HOD : JAYALEKSHMI A\n"
                            "Assoc. Prof. in Mathematics\n\n"

                            "General Engineering\n\n"
                            "HOD : Dr. ASIFSHA A\n"
                            "Asst Prof in Mechanical Engineering\n\n"

                            "Electronics & Communication Engineering\n\n"
                            "HOD : ANOOP S\n"
                            "ASSISTANT PROFESSOR\n\n"

                            "Applied Science\n\n"
                            "HOD : JAYALEKSHMI A\n"
                            "Assoc. Prof. in Mathematics\n\n"

                            "General Engineering\n\n"
                            "HOD : Dr. ASIFSHA A\n"
                            "Asst Prof in Mechanical Engineering\n\n"],
            "context": [""]
         },
         {
            "tag": "Kottarakkara Courses",
            "patterns": ["What courses are offered at College Of Engineering Kottarakkara?" ,
                         "Tell me about the programs available at College Of Engineering Kottarakkara" ,
                         "Can you list the available courses at College Of Engineering Kottarakkara?" ,
                         "What are the academic programs at College Of Engineering Kottarakkara?",
                         "Which degrees can I pursue at College Of Engineering Kottarakkara?",
                         "Give me information on the available majors at College Of Engineering Kottarakkara",
                         "What fields of study are available at College Of Engineering Kottarakkara?",
                         "Tell me about the curriculum options provided by College Of Engineering Kottarakkara"],
            "responses": ["B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 120 seats per year \n"
                          "Computer Science and Engineering (Artificial Intelligence and Machine Learning) : 60 seats per year \n"
                          "Electronics & Communication Engineering : 30 seats per year \n"],
            "context": [""]
        },
         {
            "tag": "Contact Kottarakkara",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Kottarakkara?",
                        "I need the contact information of the College Of Engineering Kottarakkara, please.",
                        "How can I get in touch with the College Of Engineering Kottarakkara?","What is the College Of Engineering Kottarakkara phone number?",
                        "Please share the College Of Engineering Kottarakkara email address.",
                        "I'm looking for the address of the College Of Engineering Kottarakkara.","How can I contact the admissions department of the College Of Engineering Kottarakkara?",
                        "I need to reach the financial aid office of College Of Engineering Kottarakkara. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Kottarakkara?","Do College Of Engineering Kottarakkara have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Kottarakkara official website for contact details?","How do I get in touch with the College Of Engineering Kottarakkara for general queries?"],
            "responses":
                ["College of Engineering, Thrikkannamangalm, ETC P.O, Kottarakkara, Kollam Dist,\n Pin - 691 531\n Ph: 0474-2453300 \nMobile : 8547005039\n E-mail : cekottarakkara@ihrd.ac.in\n web : cekottarakkara.ihrd.ac.in"],
            "context": [""]
        },
         {
            "tag": "Kottarakkara",
           "patterns": ["Tell me about College Of Engineering Kottarakkara", "College Of Engineering Kottarakkara", "Kottarakkara",
                          "Details about College Of Engineering Kottarakkara"],
            "responses": [
                "Run by IHRD, College of Engineering, Kottarakkara has been the leading technical institution in Kerala since it's venture in 2004. Affiliated to CUSAT, CE Kottarakkara offers B.Tech in Computer Science & Engineering, Electronics & Communication Engineering, reflecting the modern technological advancements through its updated syllabi. The institution is approved by AICTE, New Delhi and affiliated to CUSAT. It is under the management of IHRD (Institute of Human Resources Development) , a Kerala Government undertaking"],
            "context": [""]
         },
            {
            "tag": "Poonjar Faculty",
            "patterns": ["Tell me about the professors at College Of Engineering Poonjar.",
                        "Can you provide information about the teaching staff of College Of Engineering Poonjar?",
                        "Who are the faculty members here at College Of Engineering Poonjar?",
                        "Give me details about the academic staff of College Of Engineering Poonjar.",
                        "I'd like to learn more about the professors of College Of Engineering Poonjar.",
                        "What can you tell me about the teachers at College Of Engineering Poonjar?",
                        "Who makes up the faculty at College Of Engineering Poonjar?",
                        "Tell me about the instructors of College Of Engineering Poonjar.",
                        "Share some insights into the faculty members of College Of Engineering Poonjar.",
                        "Can you list the names of the professors of College Of Engineering Poonjar?"],
            "responses": ["Electronics Engineering\n\n"
                        "HOD : Prof.Shine P james\n"
                        "Associate Professor\n\n"

                        "Faculty\n\n"

                        "Dr.Jobymol Jacob\n"
                        "Designation :- Professor & Principal in Charge\n"

                        "Shine P James\n"
                        "Designation :- Assistant Professor]\n"

                        "Flower Abraham Mundackal\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Najmal A\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Febin P A\n"
                        "Designation :Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Saptami Venugopal\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Treesa Maria Sunny\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Revathy M Kumar\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Mahesh Krishnan S\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Bijimol\n"
                        "Designation :-Demonstrator\n"
                        "Qualification:-Diploma\n\n"

                        "Electrical & Electronics Engineering\n\n"
                        "HOD : Prof. Joshy Joseph\n"
                        "Assistant Professor\n\n"

                        "faculty\n\n"

                        "Johnson Abraham Mundackal\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n"

                        "Babitha Abraham T\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Vishnu Venukuttan\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Neetha\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Augustine Joseph\n"
                        "Designation :-Demonstrator\n"
                        "Qualification:-Diploma\n\n"

                        "Computer Science & Engineering\n\n"
                        "HOD : Rajesh K R\n"
                        "Designation: Assistant Professor and HOD\n\n"

                        "Faculty\n\n"

                        "Anchal J vattakunnel\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Dr.Annie Julie Joseph\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Anjana C V\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Jismy Alphonse\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Alby Sam S\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Devika S\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Shilpa Shiva\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Priyanka \n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Sindhumol C R\n"
                        "Designation :- Programmer\n"
                        "Qualification:- B.A, PGDCA\n\n"

                        "Meera Ramachandran\n"
                        "Designation :- Programmer\n"
                        "Qualification:-PGDCA\n\n"

                        "Jaisemon Thomas\n"
                        "Designation :- Demonstrator\n"
                        "Qualification:- Diploma\n\n"

                        "Mechanical Engineering\n\n"
                        "HOD : Joshy Joseph\n"
                        "Designation :- Assistant Professor\n\n"

                        "Faculty\n\n"

                        "Jince Jose\n"
                        "Designation :- Demonstrator\n"
                        "Qualification:- B.Tech\n\n"

                        "Applied Science\n\n"
                        "HOD : Manoj K R\n"
                        "Designation :- Assistant Professor\n\n"

                        "Dr.Minu K K\n"
                        "Designation :- Assistant Professor Department of Mathematics\n\n"

                        "Suneetha S\n"
                        "Designation :-Assistant Professor Department of Chemistry\n\n"

                        "Snehamol Sabu\n"
                        "Designation :-Assistant Professor in Mathematics\n\n"

                        "Linta Maria George\n"
                        "Designation :-Assistant Professor in Physics\n\n"],
            "context": [""]
        },
         {
            "tag": "Poonjar ec ",
            "patterns": ["Tell me about the professors in the Electronics Engineering department of College Of Engineering Poonjar.",
                        "Who are the faculty members in the Electronics Engineering department of College Of Engineering Poonjar?",
                        "Can you provide information on the teaching staff in Electronics Engineering at College Of Engineering Poonjar?",
                        "Give me details about the Electronics Engineering instructors of College Of Engineering Poonjar.",
                        "I'd like to learn more about the professors teaching Electronics Engineering at College Of Engineering Poonjar.",
                        "What can you tell me about the Electronics Engineering faculty of College Of Engineering Poonjar?",
                        "Who makes up the staff in the Electronics Engineering of College Of Engineering Poonjar?",
                        "Tell me about the Electronics Engineering instructors of College Of Engineering Poonjar.",
                        "Share some insights into the Electronics Engineering staff of College Of Engineering Poonjar.",
                        "Can you list the names of the professors in Electronics Engineering at College Of Engineering Poonjar?"],
            "responses": ["Electronics Engineering\n\n"
                        "HOD : Prof.Shine P james\n"
                        "Associate Professor\n\n"

                        "Faculty\n\n"

                        "Dr.Jobymol Jacob\n"
                        "Designation :- Professor & Principal in Charge\n"

                        "Shine P James\n"
                        "Designation :- Assistant Professor]\n"

                        "Flower Abraham Mundackal\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Najmal A\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Febin P A\n"
                        "Designation :Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Saptami Venugopal\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Treesa Maria Sunny\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Revathy M Kumar\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Mahesh Krishnan S\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Bijimol\n"
                        "Designation :-Demonstrator\n"
                        "Qualification:-Diploma\n\n"],
            "context": [""]
         },
         {
            "tag": "Poonjar ece ",
            "patterns": ["Tell me about the professors in the Electrical & Electronics Engineering department of College Of Engineering Poonjar.",
                        "Who are the faculty members in the Electrical & Electronics Engineering department of College Of Engineering Poonjar?",
                        "Can you provide information on the teaching staff in Electrical & Electronics Engineering at College Of Engineering Poonjar?",
                        "Give me details about the Electrical & Electronics Engineering instructors of College Of Engineering Poonjar.",
                        "I'd like to learn more about the professors teaching Electrical & Electronics Engineering at College Of Engineering Poonjar.",
                        "What can you tell me about the Electrical & Electronics Engineering faculty of College Of Engineering Poonjar?",
                        "Who makes up the staff in the Electrical & Electronics Engineering of College Of Engineering Poonjar?",
                        "Tell me about the Electrical & Electronics Engineering instructors of College Of Engineering Poonjar.",
                        "Share some insights into the Electrical & Electronics Engineering staff of College Of Engineering Poonjar.",
                        "Can you list the names of the professors in Electrical & Electronics Engineering at College Of Engineering Poonjar?"],
            "responses": ["Electrical & Electronics Engineering\n\n"
                        "HOD : Prof. Joshy Joseph\n"
                        "Assistant Professor\n\n"

                        "faculty\n\n"

                        "Johnson Abraham Mundackal\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n"

                        "Babitha Abraham T\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Vishnu Venukuttan\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Neetha\n"
                        "Designation :-Assistant Professor\n"
                        "Qualification:-M.Tech\n\n"

                        "Augustine Joseph\n"
                        "Designation :-Demonstrator\n"
                        "Qualification:-Diploma\n\n"],
            "context": [""]
         },
         {
            "tag": "Poonjar cse ",
            "patterns": ["Tell me about the professors in the Computer Science & Engineering department of College Of Engineering Poonjar.",
                        "Who are the faculty members in the Computer Science & Engineering department of College Of Engineering Poonjar?",
                        "Can you provide information on the teaching staff in Computer Science & Engineering at College Of Engineering Poonjar?",
                        "Give me details about the Computer Science & Engineering instructors of College Of Engineering Poonjar.",
                        "I'd like to learn more about the professors teaching Computer Science & Engineering at College Of Engineering Poonjar.",
                        "What can you tell me about the Computer Science & Engineering faculty of College Of Engineering Poonjar?",
                        "Who makes up the staff in the Computer Science & Engineering of College Of Engineering Poonjar?",
                        "Tell me about the Computer Science & Engineering instructors of College Of Engineering Poonjar.",
                        "Share some insights into the Computer Science & Engineering staff of College Of Engineering Poonjar.",
                        "Can you list the names of the professors in Computer Science & Engineering at College Of Engineering Poonjar?"],
            "responses": ["Computer Science & Engineering\n\n"
                        "HOD : Rajesh K R\n"
                        "Designation: Assistant Professor and HOD\n\n"

                        "Faculty\n\n"

                        "Anchal J vattakunnel\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Dr.Annie Julie Joseph\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Anjana C V\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Jismy Alphonse\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Alby Sam S\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Devika S\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Shilpa Shiva\n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Priyanka \n"
                        "Designation :- Assistant Professor\n"
                        "Qualification:- M.Tech\n\n"

                        "Sindhumol C R\n"
                        "Designation :- Programmer\n"
                        "Qualification:- B.A, PGDCA\n\n"

                        "Meera Ramachandran\n"
                        "Designation :- Programmer\n"
                        "Qualification:-PGDCA\n\n"

                        "Jaisemon Thomas\n"
                        "Designation :- Demonstrator\n"
                        "Qualification:- Diploma\n\n"],
            "context": [""]
         },
         {
            "tag": "Poonjar mec ",
            "patterns": ["Tell me about the professors in the Mechanical Engineering department of College Of Engineering Poonjar.",
                        "Who are the faculty members in the Mechanical Engineering department of College Of Engineering Poonjar?",
                        "Can you provide information on the teaching staff in Mechanical Engineering at College Of Engineering Poonjar?",
                        "Give me details about the Mechanical Engineering instructors of College Of Engineering Poonjar.",
                        "I'd like to learn more about the professors teaching Mechanical Engineering at College Of Engineering Poonjar.",
                        "What can you tell me about the Mechanical Engineering faculty of College Of Engineering Poonjar?",
                        "Who makes up the staff in the Mechanical Engineering of College Of Engineering Poonjar?",
                        "Tell me about the Mechanical Engineering instructors of College Of Engineering Poonjar.",
                        "Share some insights into the Mechanical Engineering staff of College Of Engineering Poonjar.",
                        "Can you list the names of the professors in Mechanical Engineering at College Of Engineering Poonjar?"],
            "responses": ["Mechanical Engineering\n\n"
                            "HOD : Joshy Joseph\n"
                            "Designation :- Assistant Professor\n\n"

                            "Faculty\n\n"

                            "Jince Jose\n"
                            "Designation :- Demonstrator\n"
                            "Qualification:- B.Tech\n\n"],
            "context": [""]
         },
         {
            "tag": "Poonjar mec ",
            "patterns": ["Tell me about the professors in the Applied Science department of College Of Engineering Poonjar.",
                        "Who are the faculty members in the Applied Science department of College Of Engineering Poonjar?",
                        "Can you provide information on the teaching staff in Applied Science at College Of Engineering Poonjar?",
                        "Give me details about the Applied Science instructors of College Of Engineering Poonjar.",
                        "I'd like to learn more about the professors teaching Applied Science at College Of Engineering Poonjar.",
                        "What can you tell me about the Applied Science faculty of College Of Engineering Poonjar?",
                        "Who makes up the staff in the Applied Science of College Of Engineering Poonjar?",
                        "Tell me about the Applied Science instructors of College Of Engineering Poonjar.",
                        "Share some insights into the Applied Science staff of College Of Engineering Poonjar.",
                        "Can you list the names of the professors in Applied Science at College Of Engineering Poonjar?"],
            "responses": ["Applied Science\n\n"
                           "HOD : Manoj K R\n"
                            "Designation :- Assistant Professor\n\n"

                            "Dr.Minu K K\n"
                            "Designation :- Assistant Professor Department of Mathematics\n\n"

                            "Suneetha S\n"
                            "Designation :-Assistant Professor Department of Chemistry\n\n"

                            "Snehamol Sabu\n"
                            "Designation :-Assistant Professor in Mathematics\n\n"

                            "Linta Maria George\n"
                            "Designation :-Assistant Professor in Physics\n\n"],
            "context": [""]
         },
          {
            "tag": "Poonjar hod ",
            "patterns": ["I'd like to know who the HODs of the College Of Engineering Poonjar.",
                        "Can you share the HODs' names for the departments of College Of Engineering Poonjar ?",
                        "Can you tell me about the other department heads of College Of Engineering Poonjar?",
                        "Could you give me an overview of the department heads of College Of Engineering Poonjar?",
                        "Tell me about the leadership in the departments of College Of Engineering Poonjar.",
                        "Provide information about the Heads of Departments in the College Of Engineering Poonjar."],
            "responses": ["Electronics Engineering\n\n"
                            "HOD : Prof.Shine P james\n"
                            "Associate Professor\n\n"


                            "Electrical & Electronics Engineering\n\n"
                            "HOD : Prof. Joshy Joseph\n"
                            "Assistant Professor\n\n"

                            "Computer Science & Engineering\n\n"
                            "HOD : Rajesh K R\n"
                            "Designation: Assistant Professor and HOD\n\n"



                            "Mechanical Engineering\n\n"
                            "HOD : Joshy Joseph\n"
                            "Designation :- Assistant Professor\n\n"

                            "Applied Science\n\n"
                            "HOD : Manoj K R\n"
                            "Designation :- Assistant Professor\n\n"],
            "context": [""]
          },
          {
            "tag": "Poonjar Courses",
            "patterns": ["What courses are offered at College Of Engineering Poonjar?" ,
                         "Tell me about the programs available at College Of Engineering Poonjar" ,
                         "Can you list the available courses at College Of Engineering Poonjar?" ,
                         "What are the academic programs at College Of Engineering Poonjar?",
                         "Which degrees can I pursue at College Of Engineering Poonjar?",
                         "Give me information on the available majors at College Of Engineering Poonjar",
                         "What fields of study are available at College Of Engineering Poonjar?",
                         "Tell me about the curriculum options provided by College Of Engineering Poonjar"],
            "responses": ["B.Tech Courses = \n\n"
                          "Computer Science & Engineering : 60 seats per year \n\n"
                          "Master Degree = \n\n"
                          "Master of Computer Application : 30 seats per year\n\n"
                          "Diploma = \n\n"
                          "Computer Engineering : 60 seats per year\n"
                          "Electronics Engineering : 60 seats per year\n"
                          "Electrical and Electronics Engineering : 60 seats per year\n"],
            "context": [""]
        },
         {
            "tag": "Contact Poonjar",
            "patterns": ["Can you provide me with the contact details for the College Of Engineering Poonjar?",
                        "I need the contact information of the College Of Engineering Poonjar, please.",
                        "How can I get in touch with the College Of Engineering Poonjar?","What is the College Of Engineering Poonjar phone number?",
                        "Please share the College Of Engineering Poonjar email address.",
                        "I'm looking for the address of the College Of Engineering Poonjar.","How can I contact the admissions department of the College Of Engineering Poonjar?",
                        "I need to reach the financial aid office of College Of Engineering Poonjar. What's their contact?",
                        "Is there a separate contact for the academic affairs department of College Of Engineering Poonjar?","Do College Of EngineeringPoonjar have a website or social media where I can find contact information?",
                        "Can you direct me to the College Of Engineering Poonjar official website for contact details?","How do I get in touch with the College Of Engineering Poonjar for general queries?"],
            "responses":
                ["College of Engineering Poonjar, Thekkekkara P.O, Erattupettah, Kottayam Dist. Kerala State, India., \nPin .686 582\n Phone:  95624 01737\n Mobile : 8547005035 \nE-mail : cepoonjar@ihrd.ac.in, \nprincipal@cep.ac.in, \ncepoonjar.ihrd@gmail.com \nweb    : www.cep.ac.in"],
            "context": [""]
        },
        {
            "tag": "Poonjar",
           "patterns": ["Tell me about College Of Engineering Poonjar", "College Of Engineering Poonjar", "Poonjar",
                          "Details about College Of Engineering Poonjar"],
            "responses": [
                "College of Engineering, Poonjar is established by the Institute of Human Resources Development (IHRD), a Government of Kerala Undertaking. IHRD is a pioneer educational organization supported by Kearla Government  College of Engineering, Poonjar started its functioning in the academic year 2000-2001. The College is affiliated to the prestigious Cochin University of Science and Technology (CUSAT). Currently the institution offers  M.Tech in Electronics Engineering ( Signal Processing)  and Computer and information Science  and B.Tech Degree in Computer Science and Engineering, Electronics and Communication Engineering, Electrical and Electronics Engineering. The institution is approved by AICTE, New Delhi and affiliated to CUSAT. It is under the management of IHRD (Institute of Human Resources Development) , a Kerala Government undertaking"],
            "context": [""]
         },

    ]
}

df = pd.DataFrame(data["intents"])

def get_response(user_input):
    user_input = user_input.lower()
    for index, row in df.iterrows():
        for pattern in row["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(row["responses"])
    return "I'm sorry, I don't understand your question."

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = get_response(user_input)
    print("Bot:", response)
