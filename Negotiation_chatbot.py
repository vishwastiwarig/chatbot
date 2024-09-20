import google.generativeai as genai
from google.colab import userdata
import random

# Set up API key (same as before)
api_key = userdata.get('GOOGLE_API_KEY')#i can not share api key here so sorry:)
if not api_key:
    api_key = input("Enter your Google API key: ")
    userdata.set('GOOGLE_API_KEY', api_key)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Enhanced product database with pricing flexibility
products = {
    "laptop": {
        "name": "ProBook X1",
        "description": "Revolutionary laptop with AI-powered performance optimization",
        "list_price": 1200,
        "min_price": 1000,
        "features": [
            "16GB RAM", "512GB SSD", "AI-powered GPU", "15.6 inch 4K display", 
            "24-hour adaptive battery life", "Biometric security", "Holographic keyboard"
        ],
        "use_cases": [
            "Professional video editing", "Advanced machine learning development",
            "Immersive gaming experience", "Virtual reality content creation"
        ],
        "eco_friendly": "Made with 80% recycled materials",
        "future_proof": "Guaranteed compatibility with next-gen software for 5 years",
        "customer_story": "A filmmaker completed a feature-length documentary entirely on the ProBook X1, praising its performance and battery life during remote shoots."
    },
    "phone": {
        "name": "GalaxyPro 12",
        "description": "Next-gen smartphone with holographic display and quantum encryption",
        "list_price": 800,
        "min_price": 650,
        "features": [
            "Holographic 3D display", "Quantum-encrypted communications",
            "1TB neural storage", "AI personal assistant", "50MP adaptive camera",
            "Biosensor health monitoring", "Seamless AR integration"
        ],
        "use_cases": [
            "Secure business communications", "Immersive AR gaming",
            "Professional-grade mobile photography", "Real-time health tracking"
        ],
        "eco_friendly": "Solar-charging back panel",
        "future_proof": "Modular design for easy upgrades",
        "customer_story": "A travel vlogger livestreamed an entire Antarctic expedition using just the GalaxyPro 12, showcasing its durability and camera quality."
    },
    "tablet": {
        "name": "SlateTab Ultra",
        "description": "Versatile tablet with e-ink mode and AI-powered productivity suite",
        "list_price": 600,
        "min_price": 500,
        "features": [
            "10-inch adaptive display with e-ink mode", "Neural pen with haptic feedback",
            "AI-powered productivity suite", "360-degree flexibility", "Dual OS capability",
            "Immersive spatial audio", "5G + Satellite connectivity"
        ],
        "use_cases": [
            "Digital art creation", "E-reading with zero eye strain",
            "Mobile office with AI assistance", "Augmented reality education"
        ],
        "eco_friendly": "Biodegradable casing",
        "future_proof": "Lifetime software updates guaranteed",
        "customer_story": "An architect designed an award-winning sustainable building using the SlateTab Ultra's AR capabilities for on-site visualization."
    }
}

# Innovative conversation and negotiation elements
conversation_enhancers = [
    "virtual_demo",
    "personalized_use_case",
    "future_technology_preview",
    "eco_impact_visualization",
    "customer_success_story",
    "interactive_feature_exploration",
    "value_over_time_calculation",
    "competitive_comparison",
    "unexpected_benefit_revelation",
    "tailored_bundle_suggestion"
]

def get_ai_response(conversation_history, user_message):
    chat = model.start_chat(history=conversation_history)
    response = chat.send_message(user_message)
    return response.text

def innovative_negotiation(product_id, user_input, conversation_history=[], user_profile={}, current_offer=None):
    product = products[product_id]
    
    # Select a random conversation enhancer
    enhancer = random.choice(conversation_enhancers)
    
    prompt = f"""
    You are Alex, an innovative AI sales representative for TechMart, negotiating the price of the {product['name']} ({product['description']}) with a potential customer.
    Your goal is to create an engaging, personalized conversation that highlights the unique value of the product while working towards a mutually beneficial price agreement.

    Product details:
    {product}

    User profile (use this to personalize your response):
    {user_profile}

    Current negotiation status:
    List price: ${product['list_price']}
    Minimum acceptable price: ${product['min_price']}
    Current offer from customer: {"$" + str(current_offer) if current_offer else "Not yet provided"}

    The customer said: "{user_input}"

    Use the following conversation enhancer in your response: {enhancer}

    Guidelines for your response:
    1. Be creative, engaging, and personable in your approach to negotiation.
    2. Tailor your response to the user's profile, previous interactions, and current offer (if any).
    3. Incorporate the selected conversation enhancer in an organic way to support your negotiation strategy.
    4. If the customer hasn't made an offer, encourage them to propose a price they think is fair.
    5. If their offer is too low, explain the value proposition creatively and make a counteroffer.
    6. If their offer is acceptable, you may accept it or try to upsell with additional features or services.
    7. Use the product's innovative features, eco-friendly aspects, and future-proofing capabilities to justify its value.
    8. Be prepared to offer small concessions or bonuses to move the negotiation forward.
    9. Ask thought-provoking questions to understand the user's needs and budget constraints.
    10. Use storytelling techniques to make the product benefits and price points more relatable.

    Respond in a conversational manner, as if you're having an exciting discussion about future technology with a friend while also working out a fair deal.
    """
    
    ai_response = get_ai_response(conversation_history, prompt)
    
    # Update conversation history
    conversation_history.append({"role": "user", "parts": [f"Customer: {user_input}"]})
    conversation_history.append({"role": "model", "parts": [ai_response]})
    
    return {
        "ai_response": ai_response,
        "conversation_history": conversation_history,
        "enhancer_used": enhancer
    }

def interactive_innovative_negotiation():
    print("Welcome to TechMart's Futuristic Product Negotiation Experience!")
    print("Available products: laptop (ProBook X1), phone (GalaxyPro 12), tablet (SlateTab Ultra)")
    product_id = input("Which product would you like to explore and negotiate for today? ").lower()
    
    if product_id not in products:
        print("I'm sorry, that product isn't in our futuristic lineup yet. Please choose from laptop, phone, or tablet.")
        return
    
    product = products[product_id]
    print(f"\nExcellent choice! Let's dive into the world of the {product['name']} and find a price that works for you.")
    
    # Collect some user info for personalization
    user_profile = {
        "occupation": input("To personalize your experience, could you tell me your occupation? "),
        "main_use": input("What's the primary use you have in mind for this device? "),
        "tech_savviness": input("On a scale of 1-10, how tech-savvy would you say you are? ")
    }
    
    conversation_history = []
    current_offer = None
    
    while True:
        user_input = input("\nWhat are your thoughts on the product or its price? (Type 'end' to finish): ")
        if user_input.lower() == 'end':
            print("Thank you for exploring the future of technology with us. We hope to see you again soon!")
            break
        
        # Try to extract a numerical offer from the user input
        offer_match = re.search(r'\$?(\d+)', user_input)
        if offer_match:
            current_offer = int(offer_match.group(1))
        
        result = innovative_negotiation(product_id, user_input, conversation_history, user_profile, current_offer)
        print(f"\nAI Negotiator Alex: {result['ai_response']}")
        conversation_history = result['conversation_history']
        
        print(f"\n[Debug: Conversation enhancer used: {result['enhancer_used']}]")


interactive_innovative_negotiation()
