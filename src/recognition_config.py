
alternativeLANG =   [
                                        "en-AU",
#                                        "en-CA",
#                                        "en-GH",
#                                        "en-HK",
#                                        "en-IN",
#                                        "en-IE",
#                                        "en-KE",
#                                        "en-NZ",
                                        "en-NG",
#                                        "en-PK",
#                                        "en-PH",
#                                        "en-SG",
                                        "en-ZA",
                                        "en-TZ",
#                                        "en-GB",
                                        "en-US"
                    ]

recognitionArray = [] 

recognitionResults = []

"""
    #This comes from result.properties
    <PropertyId.SpeechServiceResponse_JsonResult: 5000>: 
    '{"DisplayText":"Rest easy.","Duration":11500000,"Id":"67d33c3ccb6e407f94733e0c0e6d60f4",
    "NBest":[{"Confidence":0.9163978,"Display":"Rest easy.","ITN":"rest easy","Lexical":"rest easy","MaskedITN":""},
    {"Confidence":0.90946555,"Display":"breast easy","ITN":"breast easy","Lexical":"breast easy","MaskedITN":""},
    {"Confidence":0.9224477,"Display":"best easy","ITN":"best easy","Lexical":"best easy","MaskedITN":""},
    {"Confidence":0.8572453,"Display":"pressed easy","ITN":"pressed easy","Lexical":"pressed easy","MaskedITN":""},
    {"Confidence":0.8758984,"Display":"crest easy","ITN":"crest easy","Lexical":"crest easy","MaskedITN":""}],
    "Offset":700000,"RecognitionStatus":"Success"}', <PropertyId.SpeechServiceResponse_RecognitionLatencyMs: 5002>: '1483'
"""
#Usefull for google speech but not for any other
"""
phrasesOBJ = [
    {
      "phrases": ["forward"],
      "boost": 19
    },
     {
      "phrases": ["the"],
      "boost": 15
    },
     {
      "phrases": ["to"],
      "boost": 19
    },
     {
      "phrases": ["them"],
      "boost": 15
    },
     {
      "phrases": ["for"],
      "boost": 19
    },
     {
      "phrases": ["you"],
      "boost": 18
    },
     {
      "phrases": ["we"],
      "boost": 18
    },
     {
      "phrases": ["ready"],
      "boost": 17
    },
     {
      "phrases": ["your"],
      "boost": 17
    },
     {
      "phrases": ["I"],
      "boost": 16
    },
     {
      "phrases": ["of"],
      "boost": 16
    },
     {
      "phrases": ["and"],
      "boost": 15
    },
     {
      "phrases": ["on"],
      "boost": 15
    },
     {
      "phrases": ["fire"],
      "boost": 20
    },
     {
      "phrases": ["will"],
      "boost": 20
    },
     {
      "phrases": ["is"],
      "boost": 15
    },
     {
      "phrases": ["my"],
      "boost": 14
    }, {
      "phrases": ["at"],
      "boost": 14
    },
     {
      "phrases": ["men"],
      "boost": 17
    },
         {
      "phrases": ["many"],
      "boost": 17
    },
     {
      "phrases": ["are"],
      "boost": 15
    },
     {
      "phrases": ["our"],
      "boost": 15
    },
     {
      "phrases": ["warriors"],
      "boost": 15
    },
     {
      "phrases": ["they"],
      "boost": 15
    },
     {
      "phrases": ["get"],
      "boost": 15
    },
     {
      "phrases": ["the"],
      "boost": 20
    }, 
    {
      "phrases": ["this"],
      "boost": 13
    },
     {
      "phrases": ["us"],
      "boost": 13
    },
     {
      "phrases": ["that"],
      "boost": 13
    },
     {
      "phrases": ["have"],
      "boost": 15
    },
     {
      "phrases": ["ships"],
      "boost": 15
    },
     {
      "phrases": ["now"],
      "boost": 15
    },
     {
      "phrases": ["me"],
      "boost": 12
    },
    {
      "phrases": ["it"],
      "boost": 14
    },
     {
      "phrases": ["not"],
      "boost": 12
    },
     {
      "phrases": ["their"],
      "boost": 12
    },
     {
      "phrases": ["be"],
      "boost": 12
    },
     {
      "phrases": ["enemy"],
      "boost": 13
    },
     {
      "phrases": ["formation"],
      "boost": 13
    },
     {
      "phrases": ["in"],
      "boost": 11
    },
     {
      "phrases": ["do"],
      "boost": 11
    },
     {
      "phrases": ["so"],
      "boost": 15
    },
     {
      "phrases": ["all"],
      "boost": 10
    },
     {
      "phrases": ["gods"],
      "boost": 12
    },
     {
      "phrases": ["take"],
      "boost": 12
    },
     {
      "phrases": ["attack"],
      "boost": 12
    },
     {
      "phrases": ["move"],
      "boost": 15
    },
     {
      "phrases": ["battle"],
      "boost": 15
    },
     {
      "phrases": ["down"],
      "boost": 12
    },
     {
      "phrases": ["destroy"],
      "boost": 12
    },
    {
      "phrases": ["the word"],
      "boost": 0
    },
    {
      "phrases": ["word"],
      "boost": 9
    },
    {
      "phrases": ["bastard"],
      "boost": 15
    },
    {
      "phrases": ["boss"],
      "boost": 2
    },
    {
      "phrases": ["lad"],
      "boost": 15
    },
    {
      "phrases": ["done"],
      "boost": 5
    },
    {
      "phrases": ["dead"],
      "boost": 15
    },
    {
      "phrases": ["honor"],
      "boost": 18
    },
    {
      "phrases": ["glory"],
      "boost": 18
    },
    {
       "phrases": ["carthage"],
      "boost": 18
    }
     ]
"""