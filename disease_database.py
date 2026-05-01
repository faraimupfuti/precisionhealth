"""
Disease Database for ClaraVision Health
Contains comprehensive information about skin conditions common in African populations
"""

DISEASE_DATABASE = {
    "Acne": {
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
            "Topical benzoyl peroxide (2.5-5% to minimize irritation in darker skin)",
            "Topical retinoids (tretinoin, adapalene) - start with lower concentrations",
            "Salicylic acid for mild cases",
            "Oral antibiotics (doxycycline, minocycline) for moderate to severe cases",
            "For severe cystic acne: Isotretinoin under dermatologist supervision",
            "Azelaic acid to reduce hyperpigmentation and treat acne simultaneously",
            "Avoid harsh scrubbing which can worsen hyperpigmentation"
        ],
        "prevention": [
            "Wash face twice daily with gentle, pH-balanced cleanser",
            "Use oil-free, non-comedogenic moisturizers and cosmetics",
            "Avoid touching or picking at acne to prevent scarring and hyperpigmentation",
            "Remove makeup before bed",
            "Protect skin from sun exposure to prevent darkening of acne marks",
            "Manage stress levels",
            "Maintain a balanced diet; some find dairy or high-glycemic foods trigger acne"
        ],
        "when_to_seek_care": [
            "Acne is severe or worsening despite over-the-counter treatments",
            "Developing painful nodules or cysts",
            "Significant scarring or hyperpigmentation is occurring",
            "Acne is affecting self-esteem or quality of life",
            "Signs of infection (increased warmth, swelling, pus)"
        ]
    },
    
    "Eczema": {
        "description": "Eczema (atopic dermatitis) is a chronic inflammatory skin condition that causes dry, itchy, and inflamed skin. In African skin, eczema may appear as darker brown, purple, or grey patches rather than the classic red appearance. It's particularly common in children but can persist into adulthood.",
        "symptoms": [
            "Dry, sensitive skin",
            "Intense itching, especially at night",
            "Dark brown, purple, or grey patches on darker skin (vs. red on lighter skin)",
            "Thickened, cracked, scaly skin",
            "Small, raised bumps that may leak fluid when scratched",
            "Raw, sensitive, swollen skin from scratching",
            "Common areas: hands, feet, ankles, wrists, neck, upper chest, eyelids, face"
        ],
        "treatment": [
            "Daily moisturizing with thick, fragrance-free emollients (apply within 3 minutes after bathing)",
            "Topical corticosteroids for flare-ups (use lower potency on face, higher on body)",
            "Tacrolimus or pimecrolimus (non-steroidal anti-inflammatory creams) for sensitive areas",
            "Oral antihistamines to reduce nighttime itching",
            "Antibiotics if secondary bacterial infection develops",
            "For severe cases: phototherapy, oral immunosuppressants (cyclosporine, methotrexate)",
            "Newer biologics (dupilumab) for moderate-to-severe atopic dermatitis",
            "Wet wrap therapy for acute flares"
        ],
        "prevention": [
            "Moisturize at least twice daily, especially after bathing",
            "Take short lukewarm baths or showers (avoid hot water)",
            "Use mild, fragrance-free soaps and detergents",
            "Identify and avoid personal triggers (certain fabrics, stress, allergens, weather changes)",
            "Wear soft, breathable fabrics like cotton",
            "Use a humidifier in dry environments",
            "Avoid scratching - keep nails short, consider cotton gloves at night",
            "Manage stress through relaxation techniques"
        ],
        "when_to_seek_care": [
            "Eczema is not improving with home care after 2-3 weeks",
            "Rash is painful, oozing, or shows signs of infection (increased warmth, yellow crusting, fever)",
            "Eczema is interfering with sleep or daily activities",
            "Skin is cracking or bleeding",
            "Developing new or widespread rash",
            "Symptoms around the eyes that could affect vision"
        ]
    },
    
    "Psoriasis": {
        "description": "Psoriasis is a chronic autoimmune condition that speeds up the growth cycle of skin cells, causing thick, scaly patches. In African skin, psoriasis plaques may appear violet, grey, or dark brown with grey scales, making it harder to diagnose than the classic red plaques with silvery scales seen in lighter skin.",
        "symptoms": [
            "Thick, violet, grey, or dark brown patches covered with grey or silvery scales (on darker skin)",
            "Dry, cracked skin that may bleed",
            "Itching, burning, or soreness",
            "Thickened, pitted, or ridged nails",
            "Swollen and stiff joints (psoriatic arthritis)",
            "Common areas: scalp, elbows, knees, lower back, palms, soles"
        ],
        "treatment": [
            "Topical corticosteroids for reducing inflammation and slowing cell turnover",
            "Vitamin D analogues (calcipotriene) alone or combined with corticosteroids",
            "Topical retinoids (tazarotene)",
            "Coal tar preparations (may cause temporary darkening on darker skin)",
            "Salicylic acid to remove scales",
            "Moisturizers to reduce scaling and itching",
            "Phototherapy (UVB, PUVA) - adjust protocols for darker skin to avoid burns",
            "Systemic medications: methotrexate, cyclosporine, acitretin for severe cases",
            "Biologic drugs targeting specific immune pathways (adalimumab, etanercept, ustekinumab, secukinumab)"
        ],
        "prevention": [
            "Moisturize regularly to prevent dry skin and reduce flares",
            "Avoid skin injuries (cuts, scrapes, sunburn) that can trigger new patches (Koebner phenomenon)",
            "Limit alcohol consumption and quit smoking",
            "Manage stress through yoga, meditation, or counseling",
            "Avoid medications that can trigger flares (beta-blockers, lithium, antimalarials)",
            "Protect skin from cold, dry weather",
            "Maintain a healthy weight",
            "Get adequate vitamin D (safely through diet/supplements rather than excess sun exposure)"
        ],
        "when_to_seek_care": [
            "Psoriasis is severe, widespread, or causing significant discomfort",
            "Joint pain or swelling (possible psoriatic arthritis)",
            "Signs of infection in affected areas",
            "Treatments are not working or causing side effects",
            "Psoriasis is significantly impacting quality of life or mental health",
            "Sudden worsening or new type of rash"
        ]
    },
    
    "Vitiligo": {
        "description": "Vitiligo is a condition where the skin loses melanocytes (pigment-producing cells), resulting in white or light patches. It's particularly noticeable and psychologically impactful in individuals with darker skin. While not harmful physically, it can significantly affect self-esteem and quality of life.",
        "symptoms": [
            "Loss of skin color in patches, creating stark contrast on darker skin",
            "Premature whitening or greying of hair on scalp, eyebrows, eyelashes, or beard",
            "Loss of color in the tissues inside the mouth and nose",
            "Common areas: face (around mouth, eyes), hands, arms, feet",
            "Symmetrical pattern in most cases (non-segmental vitiligo)",
            "Patches may spread over time or remain stable for years"
        ],
        "treatment": [
            "Topical corticosteroids to help restore pigment (best for early, limited vitiligo)",
            "Topical calcineurin inhibitors (tacrolimus, pimecrolimus) for face and neck",
            "Phototherapy: Narrowband UVB (most common), PUVA, or targeted excimer laser",
            "JAK inhibitors (ruxolitinib cream) - newer treatment showing promise",
            "Depigmentation therapy for extensive vitiligo (monobenzone) to create uniform tone",
            "Surgical options: skin grafting, melanocyte transplantation for stable, localized vitiligo",
            "Cosmetic camouflage (makeup, self-tanners) for temporary coverage",
            "Psychological support and counseling"
        ],
        "prevention": [
            "No proven prevention, as causes are not fully understood",
            "Protect depigmented skin from sun with SPF 30+ broad-spectrum sunscreen (prevents burning and reduces contrast)",
            "Avoid skin trauma which may trigger new patches (Koebner phenomenon)",
            "Manage autoimmune conditions if present",
            "Reduce stress which may trigger or worsen vitiligo",
            "Maintain good overall health"
        ],
        "when_to_seek_care": [
            "New white patches appear or existing ones are rapidly spreading",
            "Desire for treatment to restore pigment or manage appearance",
            "Vitiligo is causing psychological distress or affecting quality of life",
            "Need for counseling or support groups",
            "Considering more advanced treatments like phototherapy or surgery"
        ]
    },
    
    "Tinea (Ringworm)": {
        "description": "Tinea is a fungal infection of the skin, hair, or nails. In African skin, tinea may appear as darker or lighter patches with a scaly border, rather than the classic red ring. It's highly contagious and common in warm, humid climates. Different types include tinea corporis (body), tinea capitis (scalp), tinea pedis (athlete's foot), and tinea cruris (jock itch).",
        "symptoms": [
            "Circular or ring-shaped rash with defined edges",
            "On darker skin: patches may appear darker or lighter than surrounding skin",
            "Scaly, dry, or cracked skin",
            "Itching in affected area",
            "Hair loss if scalp is affected (tinea capitis)",
            "Thickened, discolored, or crumbling nails if nails are affected",
            "Rash may spread outward while clearing in the center"
        ],
        "treatment": [
            "Topical antifungal creams: clotrimazole, miconazole, terbinafine, ketoconazole (apply beyond visible rash)",
            "Continue treatment for 1-2 weeks after rash clears to prevent recurrence",
            "Oral antifungals for severe, widespread, or scalp/nail infections: griseofulvin, terbinafine, itraconazole, fluconazole",
            "Antifungal shampoos for scalp infections (ketoconazole)",
            "Keep area clean and dry",
            "For athlete's foot: antifungal powders or sprays in shoes"
        ],
        "prevention": [
            "Keep skin clean and dry, especially in skin folds",
            "Dry thoroughly after bathing, especially between toes",
            "Wear breathable, moisture-wicking fabrics",
            "Change socks and underwear daily",
            "Avoid sharing personal items (towels, clothing, combs, sports equipment)",
            "Wear sandals or shower shoes in public showers, pools, locker rooms",
            "Treat infected pets (ringworm can spread from animals)",
            "Wash bedding and towels in hot water if infected"
        ],
        "when_to_seek_care": [
            "Rash is not improving after 2 weeks of over-the-counter antifungal treatment",
            "Infection is on the scalp or nails (requires oral medication)",
            "Rash is severe, spreading rapidly, or very painful",
            "Signs of bacterial infection develop (increased warmth, pus, fever)",
            "Rash keeps coming back after treatment",
            "Multiple family members or pets are affected"
        ]
    },
    
    "Keloid Scars": {
        "description": "Keloids are raised overgrowths of scar tissue that develop at the site of skin injury. They are much more common in individuals with darker skin tones, particularly those of African descent. Keloids can grow larger than the original wound and may cause discomfort, itching, and cosmetic concern.",
        "symptoms": [
            "Raised, thick scar tissue that grows beyond the original wound boundary",
            "Smooth, shiny surface",
            "Color: pink, red, purple, brown, or darker than surrounding skin",
            "Itching, tenderness, or pain in the affected area",
            "Can continue growing for weeks, months, or years",
            "Common areas: earlobes, shoulders, upper chest, upper back, cheeks"
        ],
        "treatment": [
            "Intralesional corticosteroid injections (triamcinolone) to reduce size and symptoms",
            "Silicone gel sheets or ointments applied daily for several months",
            "Cryotherapy (freezing) to reduce keloid size",
            "Surgical removal (high recurrence risk; often combined with other treatments)",
            "Pressure therapy with compression garments or earrings",
            "Laser therapy to reduce redness and flatten keloids",
            "Radiation therapy after surgical removal to prevent recurrence",
            "Newer treatments: intralesional 5-fluorouracil, bleomycin, interferon injections"
        ],
        "prevention": [
            "Avoid unnecessary piercings, tattoos, or elective surgeries if you're keloid-prone",
            "Treat acne promptly to avoid scarring",
            "Avoid trauma to skin (minimize cuts, scrapes, burns)",
            "If surgery is necessary, discuss keloid risk with surgeon (use tension-free closure, minimize trauma)",
            "Apply silicone gel or sheets to new wounds or surgical incisions for 3-6 months",
            "Consider intralesional corticosteroid injections immediately after surgery in high-risk individuals",
            "Keep wounds moist and protected during healing",
            "If you develop a keloid, inform healthcare providers before any future procedures"
        ],
        "when_to_seek_care": [
            "Keloid is growing, painful, or causing functional impairment",
            "Keloid is affecting appearance or self-esteem",
            "Planning surgery or procedure and want to discuss prevention strategies",
            "Previous keloid treatment failed or keloid recurred",
            "Considering cosmetic or medical treatment options"
        ]
    },
    
    "Melanoma": {
        "description": "Melanoma is the most serious type of skin cancer, arising from melanocytes. While less common in African populations, melanoma in darker skin is often diagnosed at later stages and in unusual locations (palms, soles, under nails, mucous membranes), leading to worse outcomes. Early detection is critical.",
        "symptoms": [
            "New spot on the skin or existing mole that changes in size, shape, or color",
            "Asymmetry: one half doesn't match the other",
            "Border irregularity: edges are uneven, notched, or blurred",
            "Color variation: multiple colors (brown, black, tan, red, white, blue) within the same lesion",
            "Diameter: larger than 6mm (pencil eraser), though can be smaller",
            "Evolution: changing over time in size, shape, color, or symptoms",
            "In darker skin, often appears on palms, soles, under nails (subungual), or mucous membranes",
            "Dark streak under nail, especially on thumb or big toe",
            "Non-healing sore or lesion"
        ],
        "treatment": [
            "Surgical excision is primary treatment (wide local excision with margins)",
            "Sentinel lymph node biopsy to check if cancer has spread",
            "For advanced melanoma: immunotherapy (pembrolizumab, nivolumab, ipilimumab)",
            "Targeted therapy for BRAF-mutated melanoma (vemurafenib, dabrafenib + trametinib)",
            "Radiation therapy for certain cases or metastatic disease",
            "Chemotherapy (less common now with newer treatments)",
            "Regular follow-up with full-body skin exams and imaging",
            "Treatment depends on stage, location, and whether cancer has spread"
        ],
        "prevention": [
            "Perform monthly self-skin exams, especially palms, soles, nail beds, and mouth",
            "Use broad-spectrum SPF 30+ sunscreen daily (even on darker skin; prevents UV damage)",
            "Avoid peak sun hours (10am-4pm) and seek shade",
            "Wear protective clothing, wide-brimmed hats, and sunglasses",
            "Avoid tanning beds entirely",
            "Be aware of the ABCDEs of melanoma and changes in existing moles or new spots",
            "Annual skin check by dermatologist, especially if high-risk",
            "Protect scars and chronic wounds which can develop into skin cancer"
        ],
        "when_to_seek_care": [
            "ANY new or changing mole or spot on the skin",
            "Dark streak developing under a nail",
            "Spot that bleeds, itches, or doesn't heal",
            "Mole that looks different from others (\"ugly duckling\" sign)",
            "Family history of melanoma or atypical moles",
            "IMMEDIATE dermatology referral if melanoma is suspected - early diagnosis saves lives"
        ]
    },
    
    "Post-Inflammatory Hyperpigmentation (PIH)": {
        "description": "PIH is darkening of the skin that occurs after inflammation or injury (acne, eczema, cuts, burns, procedures). It's extremely common in African skin due to higher melanin content and melanocyte activity. PIH is not a separate disease but a response to skin trauma that can persist for months to years without treatment.",
        "symptoms": [
            "Flat, darkened patches or spots on skin (brown, black, grey, or purple)",
            "Occurs at sites of previous inflammation, injury, or acne",
            "No texture change - skin feels normal, just darker",
            "Darkening may be more pronounced than original injury",
            "Can affect any area but common on face, neck, chest, back",
            "May worsen with sun exposure"
        ],
        "treatment": [
            "Sunscreen (SPF 30+ broad-spectrum) daily - essential to prevent worsening",
            "Topical hydroquinone (2-4%) to lighten dark spots - use under supervision, limit duration",
            "Azelaic acid 15-20% (gentler alternative to hydroquinone)",
            "Retinoids (tretinoin, retinol) to increase cell turnover and fade pigmentation",
            "Vitamin C serums (L-ascorbic acid) to brighten and protect",
            "Niacinamide (vitamin B3) to reduce pigment transfer",
            "Alpha hydroxy acids (glycolic, lactic acid) for gentle exfoliation",
            "Kojic acid as a tyrosinase inhibitor",
            "Chemical peels (glycolic, salicylic, Jessner's) - performed by professionals",
            "Laser treatments (Q-switched, picosecond lasers) - high risk of worsening PIH in darker skin; only by experienced providers",
            "Patience - PIH can take 6-12 months to significantly improve"
        ],
        "prevention": [
            "Treat skin conditions (acne, eczema) promptly to minimize inflammation",
            "Avoid picking, scratching, or squeezing pimples",
            "Use gentle skin care products; avoid harsh scrubs",
            "Daily sunscreen to prevent darkening of existing PIH and new spots",
            "Discuss PIH risk before cosmetic procedures (chemical peels, lasers)",
            "Use anti-inflammatory ingredients in skincare routine",
            "Start lightening agents early when dark spots first appear"
        ],
        "when_to_seek_care": [
            "PIH is not improving after 3-6 months of consistent treatment",
            "Dark spots are spreading or worsening despite treatment",
            "Uncertain if dark spots are PIH or another condition (melasma, skin cancer)",
            "Interested in professional treatments like chemical peels or lasers",
            "PIH is causing significant cosmetic concern or affecting quality of life"
        ]
    },
    
    "Seborrheic Dermatitis": {
        "description": "Seborrheic dermatitis is a common inflammatory skin condition causing scaly, flaky, itchy patches, primarily in areas with high oil gland concentration. In African skin, it may appear as darker patches rather than the typical red appearance. It commonly affects the scalp (causing dandruff), face (especially eyebrows, sides of nose), and chest.",
        "symptoms": [
            "Scaly patches, flaking, and dandruff on scalp",
            "On darker skin: patches may appear brown or grey rather than red",
            "Greasy, yellowish scales or crusts",
            "Itching or burning sensation",
            "Common areas: scalp, eyebrows, sides of nose, behind ears, chest, upper back",
            "Symptoms often worsen in cold, dry weather or with stress",
            "In infants: 'cradle cap' on scalp"
        ],
        "treatment": [
            "Medicated shampoos: ketoconazole, selenium sulfide, zinc pyrithione, coal tar, salicylic acid",
            "Use medicated shampoo 2-3 times per week; leave on for 5-10 minutes before rinsing",
            "Topical antifungals (ketoconazole cream) for facial seborrheic dermatitis",
            "Mild topical corticosteroids for short-term inflammation control",
            "Calcineurin inhibitors (tacrolimus, pimecrolimus) for face and sensitive areas",
            "Regular moisturizing to reduce scaling",
            "For severe cases: oral antifungals (itraconazole, fluconazole)",
            "For infants with cradle cap: gentle brushing and baby oil or mineral oil to soften scales"
        ],
        "prevention": [
            "Wash hair and affected areas regularly with medicated shampoo",
            "Manage stress through relaxation techniques",
            "Get adequate sleep",
            "Eat a balanced diet rich in omega-3 fatty acids, zinc, and B vitamins",
            "Limit alcohol consumption",
            "Avoid harsh skin products or those with alcohol",
            "In dry weather, use a humidifier and moisturize regularly"
        ],
        "when_to_seek_care": [
            "Condition is not improving with over-the-counter treatments after 2-3 weeks",
            "Rash is severe, spreading, or very uncomfortable",
            "Signs of infection (increased warmth, pus, fever)",
            "Hair loss is occurring",
            "Condition is affecting quality of life or self-esteem",
            "Unsure of diagnosis or if other skin conditions are present"
        ]
    }
}
