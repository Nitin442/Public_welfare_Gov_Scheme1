def chatbot():
    print("ChatBot: Hello Dear! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print("ChatBot: Goodbye💓")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("ChatBot: Hello👋How can I help you today?")
        elif 'how are you' in user_input:
            print("ChatBot: I'm just a bot🤧 but I'm doing fine😊 How about you?")
        elif 'your name' in user_input:
            print("ChatBot: I'm ChatBot, your virtual assistant😊.")
        elif 'help' in user_input:
            print("ChatBot: Sure!I'm here to help😌. What do you need?")
        elif "data safe" in user_input or "privacy" in  user_input:
         print("Yes! We follow strict data protection laws (like DPDP Act 2023). "
                "Your Aadhaar/bank details are never stored—only used for real-time verification.")
        elif "documents" in user_input or "don't have" in user_input:
          print("We'll show alternative proofs (e.g., ration card instead of income certificate) "
                "and guide you to nearby CSC centers for help.")
        elif "offline" in  user_input or "apply without internet" in  user_input:
          print("Absolutely! Download the pre-filled form or SMS the scheme code to 1925 "
                "for doorstep assistance (partnered with India Post).")
        elif "missing scheme" in  user_input or "not listed" in  user_input:
          print('Our AI updates weekly, but some state schemes take time. '
                'Use "Report Missing Scheme" or check the State Portal link provided.')
        elif "scam" in user_input or "fake" in user_input:
              print('Look for the ✅ "Verified by MeitY" badge. All schemes link to official .gov.in websites. '
                'Still unsure? Cross-check on UMANG/NGSP.')
    
        elif "cost" in user_input or "fee" in user_input:
           print("We're a nonprofit/NGO (or govt-partnered). 100% free for citizens—"
                "funded by CSR grants and partnerships.")
        elif "internet slow" in  user_input or "village" in user_input:
          print('Try "Lite Mode" (text-only) or download scheme PDFs when online. '
                'We also send SMS summaries!')
        elif "how long" in user_input or "time" in user_input:
         print("Each scheme differs (e.g.,PM Kisan credits in 3 months). "
                "Track status under 'My Applications' or get SMS updates.")
        elif "rejected" in user_input or "denied" in user_input:
          print("Our AI will explain reasons (e.g., 'Document blurry') and suggest reappeal steps. "
                "Book a free CSC consultation too.")
        else:
         print("ChatBot: Sorry🥴, I didn’t understand that.")
chatbot()