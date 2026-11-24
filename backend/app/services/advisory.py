DISCLAIMERS = {
    "en": "General educational guidance only. Confirm local recommendations with your Krishi Vigyan Kendra or agricultural officer.",
    "hi": "यह सामान्य शैक्षिक जानकारी है। स्थानीय सलाह के लिए कृषि विज्ञान केंद्र या कृषि अधिकारी से पुष्टि करें।",
    "mr": "ही सर्वसाधारण शैक्षणिक माहिती आहे. स्थानिक सल्ल्यासाठी कृषी विज्ञान केंद्र किंवा कृषी अधिकाऱ्यांशी खात्री करा.",
    "gu": "આ સામાન્ય શૈક્ષણિક માહિતી છે. સ્થાનિક સલાહ માટે કૃષિ વિજ્ઞાન કેન્દ્ર અથવા કૃષિ અધિકારીની પુષ્ટિ કરો.",
    "ta": "இது பொதுவான கல்வித் தகவல் மட்டுமே. உள்ளூர் ஆலோசனைக்கு வேளாண் அறிவியல் மையம் அல்லது வேளாண் அலுவலரிடம் உறுதிப்படுத்தவும்.",
    "te": "ఇది సాధారణ విద్యా సమాచారం మాత్రమే. స్థానిక సలహా కోసం కృషి విజ్ఞాన కేంద్రం లేదా వ్యవసాయ అధికారిని సంప్రదించండి."
}

def build_advisory(crop: str, location: str, question: str, language: str, soil_type: str | None):
    # Deliberately avoids fabricating agronomic prescriptions before a verified RAG corpus is connected.
    return {
        "status": "knowledge_base_pending",
        "crop": crop,
        "location": location,
        "soil_type": soil_type,
        "question": question,
        "answer": "The verified regional agricultural knowledge service is not connected yet. Please consult your local KVK/agriculture officer for crop-specific or time-sensitive decisions.",
        "sources": [],
        "disclaimer": DISCLAIMERS.get(language, DISCLAIMERS["en"]),
        "requires_expert_review": True
    }
