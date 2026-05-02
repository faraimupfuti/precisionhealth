"""
Comprehensive Disease Database for ClaraVision Health
Contains detailed information about skin conditions optimized for African populations
Based on Roboflow model classes: 20+ conditions
"""

DISEASE_DATABASE = {
    "acne": {
        "display_name": "Acne Vulgaris",
        "description": "Acne is a common skin condition that occurs when hair follicles become plugged with oil and dead skin cells, leading to whiteheads, blackheads, or pimples. In African skin, acne often results in post-inflammatory hyperpigmentation (dark spots) that can persist long after the acne heals.",
        "symptoms": [
            "Whiteheads (closed plugged pores)",
            "Blackheads (open plugged pores)",
            "Small red, tender bumps (papules)",
            "Pimples with pus at their tips (pustules)",
            "Large, solid, painful lumps under the skin (nodules)",
            "Post-inflammatory hyperpigmentation (dark spots) particularly common in darker skin tones"
        ],
        "treatment": [
            "Gentle cleansing twice daily with non-comedogenic products",
            "Topical benzoyl peroxide (2.5-5% to minimize irritation)",
            "Topical retinoids (tretinoin, adapalene) - start with lower concentrations",
            "Salicylic acid for mild cases",
            "Oral antibiotics (doxycycline, minocycline) for moderate to severe cases",
            "For severe cystic acne: Isotretinoin under dermatologist supervision",
            "Azelaic acid to reduce hyperpigmentation and treat acne simultaneously"
        ],
        "prevention": [
            "Wash face twice daily with gentle cleanser",
            "Use oil-free, non-comedogenic products",
            "Avoid touching or picking at acne",
            "Remove makeup before bed",
            "Protect skin from sun (SPF 30+) to prevent darkening of marks",
            "Manage stress levels"
        ],
        "when_to_seek_care": [
            "Acne is severe or worsening despite treatment",
            "Developing painful nodules or cysts",
            "Significant scarring or hyperpigmentation",
            "Acne affecting self-esteem or quality of life"
        ]
    },
    
    "acnevulgaris": {
        "display_name": "Acne Vulgaris",
        "description": "Common acne affecting face, neck, chest, and back. Often leads to post-inflammatory hyperpigmentation in darker skin tones.",
        "symptoms": [
            "Comedones (blackheads and whiteheads)",
            "Inflammatory papules and pustules",
            "Nodules and cysts in severe cases",
            "Post-inflammatory hyperpigmentation"
        ],
        "treatment": [
            "Topical retinoids (adapalene, tretinoin)",
            "Benzoyl peroxide 2.5-5%",
            "Topical or oral antibiotics",
            "Azelaic acid for hyperpigmentation",
            "Isotretinoin for severe cases"
        ],
        "prevention": [
            "Gentle skincare routine",
            "Non-comedogenic products",
            "Sun protection",
            "Avoid picking or squeezing"
        ],
        "when_to_seek_care": [
            "Moderate to severe acne",
            "Not responding to over-the-counter treatment",
            "Scarring or significant hyperpigmentation"
        ]
    },
    
    "actinickeratosis": {
        "display_name": "Actinic Keratosis",
        "description": "Precancerous skin growth caused by sun damage. Can progress to squamous cell carcinoma if untreated.",
        "symptoms": [
            "Rough, scaly patches on sun-exposed areas",
            "Skin-colored, pink, red, or brown lesions",
            "Flat or slightly raised bumps",
            "Itching or burning in some cases"
        ],
        "treatment": [
            "Cryotherapy (liquid nitrogen freezing)",
            "Topical 5-fluorouracil cream",
            "Imiquimod cream",
            "Photodynamic therapy",
            "Surgical removal for suspicious lesions"
        ],
        "prevention": [
            "Daily broad-spectrum sunscreen SPF 30+",
            "Protective clothing and hats",
            "Avoid peak sun hours (10 AM - 4 PM)",
            "Regular skin checks"
        ],
        "when_to_seek_care": [
            "New rough, scaly patches on skin",
            "Lesion becomes painful or bleeds",
            "Rapid growth or changes",
            "Multiple lesions present"
        ]
    },
    
    "allergic_contact_dermatitis": {
        "display_name": "Allergic Contact Dermatitis",
        "description": "Allergic reaction occurring when skin contacts an allergen. May appear as darker patches in African skin.",
        "symptoms": [
            "Itchy rash at contact site",
            "Dark brown or purple patches on darker skin",
            "Swelling and inflammation",
            "Blisters in severe cases",
            "Symptoms appear 24-72 hours after exposure"
        ],
        "treatment": [
            "Identify and avoid the allergen",
            "Topical corticosteroids",
            "Cool compresses",
            "Oral antihistamines for itch",
            "Oral corticosteroids for severe cases"
        ],
        "prevention": [
            "Avoid known allergens",
            "Use hypoallergenic products",
            "Patch testing to identify triggers",
            "Wear protective gloves when needed"
        ],
        "when_to_seek_care": [
            "Severe or widespread rash",
            "No improvement after 2-3 weeks",
            "Signs of infection",
            "Difficulty identifying allergen"
        ]
    },
    
    "Atopic Dermatitis": {
        "display_name": "Atopic Dermatitis (Eczema)",
        "description": "Chronic inflammatory skin condition causing dry, itchy skin. Appears as darker patches in African skin.",
        "symptoms": [
            "Dry, sensitive skin",
            "Intense itching, especially at night",
            "Dark brown, purple, or grey patches",
            "Thickened, cracked skin",
            "Raw, swollen skin from scratching"
        ],
        "treatment": [
            "Daily moisturizing with thick emollients",
            "Topical corticosteroids for flare-ups",
            "Tacrolimus or pimecrolimus for face",
            "Oral antihistamines for itching",
            "Dupilumab injection for severe cases"
        ],
        "prevention": [
            "Moisturize at least twice daily",
            "Lukewarm baths (avoid hot water)",
            "Mild, fragrance-free soaps",
            "Identify and avoid triggers",
            "Manage stress"
        ],
        "when_to_seek_care": [
            "Not improving with home care",
            "Signs of infection (oozing, crusting)",
            "Interfering with sleep or daily life",
            "Severe or widespread rash"
        ]
    },
    
    "basal_cell_carcinoma": {
        "display_name": "Basal Cell Carcinoma",
        "description": "Most common skin cancer. While less common in darker skin, can occur and may be diagnosed at later stages.",
        "symptoms": [
            "Pearly or waxy bump",
            "Flat, scar-like lesion",
            "Bleeding or oozing sore",
            "Brown or black bump on darker skin",
            "Most common on face, ears, neck"
        ],
        "treatment": [
            "Surgical excision",
            "Mohs micrographic surgery",
            "Electrodesiccation and curettage",
            "Topical imiquimod for superficial types",
            "Radiation therapy in some cases"
        ],
        "prevention": [
            "Daily sunscreen SPF 30+",
            "Protective clothing",
            "Avoid tanning beds",
            "Monthly self-skin exams",
            "Annual dermatologist visits"
        ],
        "when_to_seek_care": [
            "Any new growth that doesn't heal",
            "Existing spot changes",
            "Bleeding or crusting lesion",
            "IMMEDIATE dermatology referral needed"
        ]
    },
    
    "Contact Dermatitis": {
        "display_name": "Contact Dermatitis",
        "description": "Skin inflammation from contact with irritants or allergens.",
        "symptoms": [
            "Itchy, red rash (dark patches on darker skin)",
            "Dry, cracked skin",
            "Blisters and oozing",
            "Burning or stinging",
            "Localized to contact area"
        ],
        "treatment": [
            "Remove irritant/allergen immediately",
            "Topical corticosteroids",
            "Cool compresses",
            "Oral antihistamines",
            "Emollient creams"
        ],
        "prevention": [
            "Identify and avoid triggers",
            "Use protective barriers",
            "Fragrance-free products",
            "Patch testing if needed"
        ],
        "when_to_seek_care": [
            "Severe or spreading rash",
            "No improvement after 2 weeks",
            "Signs of infection",
            "Unknown trigger"
        ]
    },
    
    "eczema": {
        "display_name": "Eczema",
        "description": "General term for inflammatory skin conditions causing dryness and itching.",
        "symptoms": [
            "Dry, rough, itchy skin",
            "Darker patches on African skin",
            "Thickened skin from scratching",
            "Small bumps that may ooze",
            "Sensitive, inflamed skin"
        ],
        "treatment": [
            "Intensive moisturization",
            "Topical corticosteroids",
            "Non-steroidal immunomodulators",
            "Antihistamines",
            "Phototherapy for severe cases"
        ],
        "prevention": [
            "Daily moisturizing",
            "Gentle cleansers",
            "Avoid triggers",
            "Manage stress",
            "Soft, breathable fabrics"
        ],
        "when_to_seek_care": [
            "Not responding to treatment",
            "Signs of infection",
            "Interfering with daily life",
            "Widespread rash"
        ]
    },
    
    "folliculitis": {
        "display_name": "Folliculitis",
        "description": "Inflammation of hair follicles. Can lead to keloids and hyperpigmentation in darker skin.",
        "symptoms": [
            "Small red or white-headed pimples",
            "Pustules around hair follicles",
            "Itching or tenderness",
            "Post-inflammatory hyperpigmentation",
            "Common on scalp, beard, groin, legs"
        ],
        "treatment": [
            "Antibacterial soap",
            "Warm compresses",
            "Topical antibiotics (mupirocin)",
            "Oral antibiotics for severe cases",
            "Antifungal if fungal cause"
        ],
        "prevention": [
            "Keep skin clean and dry",
            "Avoid tight clothing",
            "Proper shaving technique",
            "Don't share towels or razors",
            "Shower after sweating"
        ],
        "when_to_seek_care": [
            "Widespread or severe",
            "No improvement after 1-2 weeks",
            "Recurrent episodes",
            "Development of boils or abscesses"
        ]
    },
    
    "keloid": {
        "display_name": "Keloid Scars",
        "description": "Overgrown scar tissue extending beyond original wound. Much more common in African descent (15-20x higher).",
        "symptoms": [
            "Raised, thick scar tissue",
            "Smooth, shiny surface",
            "Pink, red, purple, or darker than surrounding skin",
            "Itching, tenderness, or pain",
            "Can continue growing for months or years"
        ],
        "treatment": [
            "Intralesional corticosteroid injections",
            "Silicone gel sheets or ointments",
            "Cryotherapy",
            "Surgical excision with steroid injection",
            "Laser therapy",
            "Radiation after surgery"
        ],
        "prevention": [
            "Avoid unnecessary piercings or surgeries",
            "Treat acne promptly",
            "Avoid skin trauma",
            "Apply silicone gel to new wounds",
            "Consider steroid injection immediately after surgery"
        ],
        "when_to_seek_care": [
            "Keloid is growing or painful",
            "Affecting appearance or movement",
            "Planning surgery (discuss prevention)",
            "Previous treatment failed"
        ]
    },
    
    "melanoma": {
        "display_name": "Melanoma",
        "description": "Most dangerous skin cancer. In darker skin, often on palms, soles, or under nails. Diagnosed at later stages.",
        "symptoms": [
            "New or changing mole",
            "Asymmetry, irregular borders",
            "Multiple colors (brown, black, red, blue)",
            "Larger than 6mm",
            "On darker skin: often on palms, soles, under nails",
            "Dark streak under nail"
        ],
        "treatment": [
            "Surgical excision with wide margins",
            "Sentinel lymph node biopsy",
            "Immunotherapy (pembrolizumab, nivolumab)",
            "Targeted therapy for BRAF mutations",
            "Radiation for advanced cases"
        ],
        "prevention": [
            "Monthly self-exams (check palms, soles, nails)",
            "Annual dermatologist exam",
            "Daily sunscreen SPF 30+",
            "Protective clothing",
            "Avoid tanning beds"
        ],
        "when_to_seek_care": [
            "ANY new or changing mole",
            "Dark streak under nail",
            "Non-healing sore",
            "URGENT - early diagnosis is life-saving"
        ]
    },
    
    "rosacea": {
        "display_name": "Rosacea",
        "description": "Chronic facial redness and inflammation. Less visible but still occurs in darker skin.",
        "symptoms": [
            "Facial redness or flushing",
            "Visible blood vessels",
            "Acne-like breakouts",
            "Burning or stinging",
            "Eye irritation (ocular rosacea)"
        ],
        "treatment": [
            "Avoid triggers (spicy food, alcohol, heat)",
            "Topical metronidazole",
            "Topical azelaic acid",
            "Oral antibiotics (doxycycline)",
            "Laser therapy for blood vessels"
        ],
        "prevention": [
            "Identify and avoid triggers",
            "Gentle skincare",
            "Daily sunscreen",
            "Manage stress",
            "Avoid extreme temperatures"
        ],
        "when_to_seek_care": [
            "Persistent facial redness",
            "Eye symptoms",
            "Not controlled by OTC treatments",
            "Thickening facial skin"
        ]
    },
    
    "scabies": {
        "display_name": "Scabies",
        "description": "Highly contagious mite infestation causing intense itching. Common in crowded conditions.",
        "symptoms": [
            "Intense itching, especially at night",
            "Pimple-like rash",
            "Burrow tracks (hard to see on darker skin)",
            "Between fingers, wrists, elbows, genitals",
            "Family members often affected"
        ],
        "treatment": [
            "Permethrin 5% cream (apply head to toe, wash off after 8-14 hours)",
            "Repeat after 1-2 weeks",
            "Treat all household members simultaneously",
            "Wash all bedding and clothing in hot water",
            "Oral ivermectin for severe cases"
        ],
        "prevention": [
            "Avoid skin contact with infected persons",
            "Don't share clothing or bedding",
            "Promptly treat infected household members",
            "Decontaminate environment"
        ],
        "when_to_seek_care": [
            "Intense itching interfering with sleep",
            "Rash or burrows on skin",
            "Multiple family members affected",
            "Persistent itching after treatment"
        ]
    },
    
    "Seborrheic Dermatitis": {
        "display_name": "Seborrheic Dermatitis",
        "description": "Inflammatory condition causing scaly patches. Appears brown or grey on darker skin.",
        "symptoms": [
            "Scaly patches and dandruff on scalp",
            "Brown, grey, or purple patches",
            "Greasy, yellowish scales",
            "Itching or burning",
            "Affects scalp, eyebrows, sides of nose, chest"
        ],
        "treatment": [
            "Medicated shampoos (ketoconazole, selenium sulfide, zinc pyrithione)",
            "Use 2-3 times weekly, leave on 5-10 minutes",
            "Topical antifungals for face",
            "Mild topical corticosteroids",
            "Regular moisturizing"
        ],
        "prevention": [
            "Regular use of medicated shampoo",
            "Manage stress",
            "Adequate sleep",
            "Balanced diet",
            "Avoid harsh products"
        ],
        "when_to_seek_care": [
            "Not improving after 2-3 weeks",
            "Severe or spreading",
            "Signs of infection",
            "Hair loss"
        ]
    },
    
    "Tinea Corporis": {
        "display_name": "Tinea Corporis (Ringworm)",
        "description": "Fungal infection of the body. Highly contagious. May appear as darker or lighter patches on African skin.",
        "symptoms": [
            "Circular ring-shaped rash",
            "Darker or lighter patches on darker skin",
            "Scaly border",
            "Itching",
            "Clears in center while spreading outward"
        ],
        "treatment": [
            "Topical antifungals (clotrimazole, miconazole, terbinafine) for 2-4 weeks",
            "Apply beyond visible rash",
            "Oral antifungals for severe cases (griseofulvin, terbinafine)",
            "Continue 1-2 weeks after rash clears"
        ],
        "prevention": [
            "Keep skin clean and dry",
            "Avoid sharing towels or clothing",
            "Wear breathable fabrics",
            "Shower after contact sports",
            "Treat infected pets"
        ],
        "when_to_seek_care": [
            "No improvement after 2 weeks of OTC treatment",
            "Widespread infection",
            "Severe or painful",
            "Keeps coming back"
        ]
    },
    
    "urticaria": {
        "display_name": "Urticaria (Hives)",
        "description": "Raised, itchy welts caused by histamine release. May be harder to see on darker skin but still raised and itchy.",
        "symptoms": [
            "Raised, itchy welts",
            "May be skin-colored or pink",
            "Appear suddenly, change location",
            "Individual welts fade within 24 hours",
            "Intense itching"
        ],
        "treatment": [
            "Antihistamines (cetirizine, loratadine, fexofenadine)",
            "Can increase doses up to 4x if needed",
            "Oral corticosteroids for severe cases",
            "Omalizumab injection for chronic hives",
            "Cool compresses"
        ],
        "prevention": [
            "Identify and avoid triggers",
            "Avoid aspirin and NSAIDs if triggers",
            "Manage stress",
            "Avoid hot showers",
            "Daily antihistamines for chronic cases"
        ],
        "when_to_seek_care": [
            "Difficulty breathing or throat swelling (CALL 911)",
            "Severe or widespread hives",
            "Chronic hives (>6 weeks)",
            "Not controlled by antihistamines"
        ]
    },
    
    "urticaria_pigmentosa": {
        "display_name": "Urticaria Pigmentosa",
        "description": "Accumulation of mast cells causing brown spots. Rubbing causes hives (Darier's sign). Usually in childhood.",
        "symptoms": [
            "Multiple brown or tan spots",
            "Darker brown on darker skin",
            "Darier's sign: rubbing causes swelling and hives",
            "Itching with triggers",
            "Usually trunk, arms, legs",
            "Most common in infants"
        ],
        "treatment": [
            "Avoid triggers (heat, friction, certain medications)",
            "H1 antihistamines",
            "H2 antihistamines can be added",
            "Topical corticosteroids for itchy lesions",
            "Most childhood cases improve with age"
        ],
        "prevention": [
            "Avoid known triggers",
            "Carry antihistamines",
            "Inform healthcare providers about diagnosis",
            "Avoid trigger medications (aspirin, NSAIDs)",
            "Loose-fitting clothing"
        ],
        "when_to_seek_care": [
            "Multiple brown spots in children",
            "Severe flushing or anaphylaxis",
            "Abdominal pain or GI symptoms",
            "Need for diagnosis confirmation"
        ]
    },
    
    "vitiligo": {
        "display_name": "Vitiligo",
        "description": "Autoimmune loss of skin pigment causing white patches. Particularly noticeable and impactful in darker skin.",
        "symptoms": [
            "White patches on skin (stark contrast on darker skin)",
            "Usually symmetrical",
            "Premature greying of hair",
            "Loss of color in mouth, nose",
            "Common on face, hands, arms, feet",
            "May spread or remain stable"
        ],
        "treatment": [
            "Topical corticosteroids for early vitiligo",
            "Topical tacrolimus for face",
            "Narrowband UVB phototherapy",
            "Excimer laser for localized patches",
            "Topical ruxolitinib cream (NEW FDA-approved)",
            "Skin grafting for stable vitiligo",
            "Cosmetic camouflage",
            "Psychological support"
        ],
        "prevention": [
            "No proven prevention (autoimmune)",
            "Protect white patches from sun (SPF 30+)",
            "Avoid skin trauma",
            "Manage associated conditions",
            "Early treatment may prevent spread"
        ],
        "when_to_seek_care": [
            "New white patches or rapid spreading",
            "Desire for treatment",
            "Significant psychological distress",
            "Affecting quality of life",
            "Need for counseling or support"
        ]
    },
    
    "xanthomas": {
        "display_name": "Xanthomas",
        "description": "Yellowish fat deposits indicating high cholesterol or lipid disorder. Signal cardiovascular risk.",
        "symptoms": [
            "Yellowish, orange, or tan bumps",
            "On darker skin: may be flesh-colored",
            "On eyelids, elbows, knees, tendons",
            "Firm, waxy texture",
            "Usually painless"
        ],
        "treatment": [
            "Treat underlying lipid disorder (statins, fibrates)",
            "Low-fat diet",
            "Regular exercise",
            "Weight loss if needed",
            "Xanthomas may regress with lipid control",
            "Surgical removal for cosmetic reasons"
        ],
        "prevention": [
            "Maintain healthy cholesterol levels",
            "Heart-healthy diet",
            "Regular exercise",
            "Avoid smoking",
            "Screen if family history"
        ],
        "when_to_seek_care": [
            "New yellowish bumps",
            "Family history of early heart disease",
            "Need for cardiovascular risk assessment",
            "Known lipid disorder with new xanthomas"
        ]
    },
    
    "xerodermapigmentosum": {
        "display_name": "Xeroderma Pigmentosum",
        "description": "Rare inherited disorder with extreme UV sensitivity. 10,000x increased skin cancer risk. Strict sun avoidance essential.",
        "symptoms": [
            "Severe sunburn after minimal sun exposure",
            "Freckling before age 2",
            "Dry, scaly skin",
            "Multiple skin cancers at young age",
            "Eye problems",
            "Neurological issues in some"
        ],
        "treatment": [
            "STRICT sun avoidance - LIFE-SAVING",
            "UV-blocking window films",
            "UV-protective clothing and face shields",
            "SPF 50+ sunscreen on any exposed skin",
            "Monthly dermatologist exams",
            "Aggressive treatment of all skin cancers",
            "Prophylactic retinoids"
        ],
        "prevention": [
            "Total sun avoidance",
            "UV-protective measures",
            "Early skin cancer detection",
            "Genetic counseling for families",
            "Prenatal diagnosis available"
        ],
        "when_to_seek_care": [
            "Severe sunburn in infant after minimal sun",
            "Excessive freckling in young child",
            "Family history of XP",
            "ANY new skin lesion in XP patient (URGENT)"
        ]
    }
}

# Helper function to get disease info with flexible matching
def get_disease_info(class_name):
    """
    Get disease information with flexible matching for class names
    Handles variations like 'acne' vs 'Acne', spaces, underscores, etc.
    """
    # Direct match
    if class_name in DISEASE_DATABASE:
        return DISEASE_DATABASE[class_name]
    
    # Try lowercase
    class_lower = class_name.lower()
    if class_lower in DISEASE_DATABASE:
        return DISEASE_DATABASE[class_lower]
    
    # Try with spaces replaced by underscores
    class_underscore = class_name.replace(' ', '_')
    if class_underscore in DISEASE_DATABASE:
        return DISEASE_DATABASE[class_underscore]
    
    # Try without underscores
    class_no_underscore = class_name.replace('_', ' ')
    if class_no_underscore in DISEASE_DATABASE:
        return DISEASE_DATABASE[class_no_underscore]
    
    # Try title case
    class_title = class_name.title()
    if class_title in DISEASE_DATABASE:
        return DISEASE_DATABASE[class_title]
    
    return None
