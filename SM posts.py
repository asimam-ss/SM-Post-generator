import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Social Media Post Generator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .tone-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        margin: 0.25rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .professional { background-color: #dbeafe; color: #1e40af; }
    .sarcastic { background-color: #fed7aa; color: #c2410c; }
    .enthusiastic { background-color: #dcfce7; color: #166534; }
    .casual { background-color: #e9d5ff; color: #7c3aed; }
    .educational { background-color: #e0e7ff; color: #3730a3; }
    
    .platform-card {
        border: 2px solid #e5e7eb;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #ffffff;
    }
    .character-count {
        font-size: 0.875rem;
        font-weight: 500;
    }
    .char-safe { color: #059669; }
    .char-warning { color: #d97706; }
    .char-danger { color: #dc2626; }
    
    .copy-button {
        background-color: #3b82f6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_posts' not in st.session_state:
    st.session_state.generated_posts = {}
if 'copied_status' not in st.session_state:
    st.session_state.copied_status = {}

# Post templates
POST_TEMPLATES = {
    'professional': {
        'linkedin': lambda event: f"""🎯 Exciting Development in Gauge Management

We're thrilled to announce: {event}

At [Company Name], we continue to drive innovation in precision measurement and industrial monitoring solutions. This milestone represents our commitment to delivering cutting-edge SAAS solutions that empower businesses to achieve operational excellence.

Key benefits for our clients:
• Enhanced measurement accuracy
• Streamlined workflow integration  
• Real-time monitoring capabilities
• Scalable enterprise solutions

Ready to transform your gauge management processes? Let's connect and discuss how this advancement can benefit your operations.

#GaugeManagement #SAAS #IndustrialTech #Innovation #PrecisionMeasurement""",

        'twitter': lambda event: f"""🚀 Big news in gauge management! {event}

Our SAAS solution continues to set industry standards for precision measurement and monitoring.

#GaugeManagement #SAAS #IndustrialTech #Innovation""",

        'whatsapp': lambda event: f"""🎉 *Exciting Update from [Company Name]*

Hi there! We wanted to share some fantastic news with you:

{event}

This development strengthens our position as a leading SAAS gauge management solution provider. We're committed to helping businesses like yours achieve greater efficiency and accuracy in measurement processes.

Would you like to learn more about how this benefits your operations? We'd love to schedule a brief call to discuss the possibilities.

Best regards,
[Your Name] - CMO"""
    },
    
    'sarcastic': {
        'linkedin': lambda event: f"""Oh, just another "revolutionary" development in gauge management... 🙄

Kidding! We're actually genuinely excited about: {event}

While everyone else is still measuring things with rulers from 1995, we're over here building SAAS solutions that actually work. Revolutionary? Maybe. Necessary? Absolutely.

Because apparently, accurate measurements and streamlined processes are still considered "innovative" in 2025. Who knew? 🤷‍♀️

Ready to join the 21st century of gauge management?

#GaugeManagement #SAAS #WelcomeToTheFuture #StillUsingSpreadsheets""",

        'twitter': lambda event: f"""Plot twist: {event} 

And yes, we're still the only ones who think gauge management should actually... work properly. Wild concept, right? 🤯

#GaugeManagement #SAAS #ModernProblems""",

        'whatsapp': lambda event: f"""*Well, this happened...* 😏

{event}

I know, I know - another day, another breakthrough in gauge management. Because apparently we're the only ones who think measuring things accurately shouldn't be rocket science.

But hey, someone has to drag this industry into the modern era, right? Might as well be us! 

Want to see what "functional software" looks like? Hit me up! 📱"""
    },
    
    'enthusiastic': {
        'linkedin': lambda event: f"""🎉 WOW! This is HUGE for gauge management! 

{event}

I can barely contain my excitement about what this means for our industry! 🚀 Our SAAS solution is transforming how businesses approach precision measurement, and this milestone proves we're just getting started!

The impact on operational efficiency is going to be INCREDIBLE:
✨ Game-changing accuracy improvements
✨ Lightning-fast implementation
✨ Mind-blowing ROI potential
✨ Future-proof scalability

This is the kind of innovation that keeps me up at night (in the best way possible)! Who else is ready to revolutionize their measurement processes?! 

LET'S GOOO! 🔥

#GaugeManagement #SAAS #GameChanger #Innovation #Excited""",

        'twitter': lambda event: f"""🔥 GAME CHANGER ALERT! 🔥

{event}

This is exactly why I LOVE working in gauge management SAAS! The future is NOW! 🚀

Who's ready to transform their measurement game?!

#GaugeManagement #SAAS #Excited #Innovation""",

        'whatsapp': lambda event: f"""🎊 *AMAZING NEWS!* 🎊

{event}

I'm literally buzzing with excitement about this! This is exactly the kind of breakthrough that makes me passionate about what we do every single day! 

Our gauge management SAAS solution is changing the game, and I couldn't be prouder to be part of this journey! The possibilities are ENDLESS! 

Want to experience this excitement firsthand? Let's chat about how this can supercharge your operations! 

*Ready to be amazed?* ⚡️"""
    },
    
    'casual': {
        'linkedin': lambda event: f"""Hey everyone! 👋

So this cool thing happened: {event}

Honestly, working in gauge management might not sound like the most exciting field, but moments like these remind me why I love what we do. Our SAAS solution is making real differences for real businesses, and that's pretty awesome.

If you're dealing with measurement headaches or just curious about modern gauge management solutions, feel free to reach out. Always happy to chat about how we can make your processes smoother.

Cheers! 🍻

#GaugeManagement #SAAS #RealTalk""",

        'twitter': lambda event: f"""Just happened: {event}

Pretty cool stuff in the gauge management world! Our SAAS solution keeps getting better 📈

DM me if you want to chat about it! 

#GaugeManagement #SAAS""",

        'whatsapp': lambda event: f"""Hey! Hope you're doing well! 

Quick update from our end: {event}

I thought you might find this interesting since you're always looking for ways to improve your measurement processes. Our SAAS solution has been helping a lot of companies streamline their operations.

No pressure, but if you ever want to chat about how this might work for you, just give me a shout! 

Have a great day! 😊"""
    },
    
    'educational': {
        'linkedin': lambda event: f"""📚 Industry Insight: Understanding Gauge Management Evolution

Today's milestone: {event}

Let's break down what this means for modern manufacturing and quality control:

🔍 **The Challenge**: Traditional gauge management often relies on manual processes, leading to inconsistencies and inefficiencies.

💡 **The Solution**: SAAS-based gauge management systems provide:
• Centralized data management
• Automated calibration tracking  
• Real-time compliance monitoring
• Predictive maintenance insights

📊 **Industry Impact**: Companies implementing digital gauge management see average improvements of:
- 35% reduction in measurement errors
- 50% faster compliance reporting
- 25% decrease in equipment downtime

🎯 **Key Takeaway**: The shift to cloud-based gauge management isn't just about technology—it's about building sustainable, scalable quality systems.

What aspects of gauge management digitization are you most curious about?

#GaugeManagement #QualityControl #Manufacturing #SAAS #DigitalTransformation""",

        'twitter': lambda event: f"""📖 Quick lesson: {event}

Why SAAS gauge management matters:
✅ Centralized tracking
✅ Automated compliance  
✅ Predictive insights
✅ Scalable solutions

The future of precision measurement is digital! 

#GaugeManagement #Education #SAAS""",

        'whatsapp': lambda event: f"""📚 *Educational Moment!*

{event}

Since you're interested in operational improvements, here's why this matters:

*Traditional gauge management challenges:*
- Manual tracking and errors
- Compliance headaches  
- Equipment downtime surprises

*Modern SAAS solutions offer:*
- Automated processes
- Real-time insights
- Predictive maintenance
- Seamless compliance

The result? Companies typically see 35% fewer measurement errors and 50% faster reporting.

Want to dive deeper into how this could transform your operations? Let's schedule a brief educational call!"""
    }
}

# Platform configurations
PLATFORMS = {
    'linkedin': {'name': 'LinkedIn', 'icon': '💼', 'limit': 3000, 'color': 'blue'},
    'twitter': {'name': 'Twitter/X', 'icon': '🐦', 'limit': 280, 'color': 'lightblue'},
    'whatsapp': {'name': 'WhatsApp', 'icon': '💬', 'limit': 4096, 'color': 'green'}
}

# Tone configurations
TONES = {
    'professional': {'name': 'Professional', 'class': 'professional'},
    'sarcastic': {'name': 'Sarcastic', 'class': 'sarcastic'},
    'enthusiastic': {'name': 'Enthusiastic', 'class': 'enthusiastic'},
    'casual': {'name': 'Casual', 'class': 'casual'},
    'educational': {'name': 'Educational', 'class': 'educational'}
}

def get_character_count_class(text, limit):
    """Get CSS class for character count based on usage"""
    count = len(text)
    if count > limit:
        return 'char-danger'
    elif count > limit * 0.9:
        return 'char-warning'
    else:
        return 'char-safe'

def generate_posts(event_text, selected_tones):
    """Generate posts for selected tones and all platforms"""
    posts = {}
    for tone in selected_tones:
        posts[tone] = {}
        for platform_id in PLATFORMS.keys():
            if tone in POST_TEMPLATES and platform_id in POST_TEMPLATES[tone]:
                posts[tone][platform_id] = POST_TEMPLATES[tone][platform_id](event_text)
    return posts

# Main app
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Social Media Post Generator</h1>
        <p>SAAS Gauge Management Solution - CMO Content Creator</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for input
    with st.sidebar:
        st.header("📝 Input Configuration")
        
        # Event input
        event_input = st.text_area(
            "Event Description",
            placeholder="Enter your event details here (e.g., 'We just launched our new AI-powered calibration feature that reduces setup time by 60%')",
            height=150,
            help="Describe your event, feature launch, or announcement"
        )
        
        st.markdown("---")
        
        # Tone selection
        st.subheader("🎭 Select Tones")
        selected_tones = []
        
        for tone_id, tone_info in TONES.items():
            if st.checkbox(tone_info['name'], key=f"tone_{tone_id}"):
                selected_tones.append(tone_id)
        
        st.markdown("---")
        
        # Generate button
        generate_button = st.button(
            "🚀 Generate Posts",
            disabled=not event_input.strip() or len(selected_tones) == 0,
            use_container_width=True
        )
        
        if generate_button and event_input.strip() and selected_tones:
            with st.spinner("Generating posts..."):
                time.sleep(1)  # Simulate processing time
                st.session_state.generated_posts = generate_posts(event_input.strip(), selected_tones)
                st.success("✅ Posts generated successfully!")
    
    # Main content area
    if st.session_state.generated_posts:
        st.header("📱 Generated Posts")
        
        # Display selected tones
        st.markdown("**Selected Tones:**")
        tone_badges = ""
        for tone in st.session_state.generated_posts.keys():
            tone_class = TONES[tone]['class']
            tone_badges += f'<span class="tone-badge {tone_class}">{TONES[tone]["name"]}</span>'
        st.markdown(tone_badges, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Display posts by tone
        for tone, posts in st.session_state.generated_posts.items():
            st.subheader(f"🎯 {TONES[tone]['name']} Tone")
            
            # Create tabs for each platform
            platform_tabs = st.tabs([f"{PLATFORMS[p]['icon']} {PLATFORMS[p]['name']}" for p in PLATFORMS.keys()])
            
            for idx, (platform_id, platform_info) in enumerate(PLATFORMS.items()):
                with platform_tabs[idx]:
                    if platform_id in posts:
                        post_content = posts[platform_id]
                        char_count = len(post_content)
                        char_class = get_character_count_class(post_content, platform_info['limit'])
                        
                        # Character count display
                        st.markdown(f"""
                        <p class="character-count {char_class}">
                            {char_count}/{platform_info['limit']} characters
                            {' (Over limit!)' if char_count > platform_info['limit'] else ''}
                        </p>
                        """, unsafe_allow_html=True)
                        
                        # Post content
                        st.code(post_content, language='text')
                        
                        # Copy button (simulated - actual clipboard access requires JavaScript)
                        copy_key = f"{tone}_{platform_id}"
                        if st.button(f"📋 Copy {platform_info['name']} Post", key=f"copy_{copy_key}"):
                            st.success("✅ Post copied to clipboard! (Note: In a real deployment, this would copy to clipboard)")
                            st.session_state.copied_status[copy_key] = True
            
            st.markdown("---")
    
    else:
        # Instructions when no posts are generated
        st.info("""
        👈 **Get Started:**
        1. Enter your event details in the sidebar
        2. Select one or more tones for your posts
        3. Click "Generate Posts" to create content for all platforms
        4. Review and copy the posts you want to use
        """)
        
        # Usage tips
        with st.expander("💡 Usage Tips"):
            st.markdown("""
            **Platform Guidelines:**
            - **LinkedIn**: Longer, detailed posts with hashtags and engagement questions
            - **Twitter/X**: Concise, punchy messages (280 character limit)
            - **WhatsApp**: Conversational, personal tone with formatting
            
            **Tone Guidelines:**
            - **Professional**: Business-focused, formal approach
            - **Sarcastic**: Witty, tongue-in-cheek style with genuine value
            - **Enthusiastic**: High-energy, excitement-driven content
            - **Casual**: Relaxed, friendly communication
            - **Educational**: Informative, teaching-focused approach
            
            **Pro Tips:**
            - Customize [Company Name] and [Your Name] placeholders before posting
            - Check character limits before posting on each platform
            - Consider your audience when selecting tones
            """)

if __name__ == "__main__":
    main()