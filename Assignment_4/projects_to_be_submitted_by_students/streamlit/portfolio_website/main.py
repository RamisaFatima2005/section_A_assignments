import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.title("👩‍💻 Welcome to My Portfolio!")
    st.write("Hello! I'm **Ramisa Fatima**, a passionate Web Developer specializing in **Next.js, Tailwind CSS, and TypeScript**.")
    st.write("I love building modern, responsive websites and exploring new technologies.")
    
    # Skills Section
    st.subheader("🔧 Skills")
    st.write("✅ HTML, CSS, Tailwind CSS")  
    st.write("✅ JavaScript, TypeScript")  
    st.write("✅ React.js, Next.js")  
    st.write("✅ UI/UX Design")

# Projects Page
elif page == "Projects":
    st.title("🚀 My Projects")
    project_data = {
        "🌸 Flower Shop": "An e-commerce website for buying flowers, built with Next.js and Tailwind CSS.",
        "📚 Books API": "A RESTful API for managing books, using Next.js API routes.",
        "🛍️ Skincare Brand": "A brand website designed in Figma and built using Next.js.",
        "🛒 Marketplace": "A fully functional marketplace for online shopping, built with Next.js and Tailwind CSS.",
        "📄 Resume Builder": "A dynamic resume builder that generates a unique resume URL,and download resume in PDF form, built with HTML, CSS and JavaScript."
    }

    for project, desc in project_data.items():
        st.subheader(project)
        st.write(desc)
        st.markdown("---")

# Contact Page
elif page == "Contact":
    st.title("📞 Contact Me")
    st.write("I'd love to connect with you! Reach out via:")
    st.write("𝕏 Twitter: https://x.com/FatimaRami73374?t=3Mq6r2xyJr3r3Bzk-0tMrw&s=09")  
    st.write("🖥️ Github: https://github.com/RamisaFatima2005")  
    st.write("💼 LinkedIn: https://www.linkedin.com/in/ramisa-fatima-8639822b8/")  

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
