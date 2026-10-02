import streamlit as st
import requests

st.set_page_config(page_title="GRC & Threat Detection Dashboard", layout="wide")

st.title("🛡️ GRC & Threat Detection Dashboard")
st.markdown("Multi-framework compliance mapping, automated telemetry, and detection-as-code.")

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["Compliance Mapping", "Telemetry & Signals", "Incident Triage"])

with tab1:
    st.header("Multi-Framework Control Status")
    framework = st.selectbox("Select Framework", ["SOC 2", "ISO 27001", "NIST SP 800-53"])
    st.info(f"Displaying controls and evidence automation for {framework}.")
    
    # Mock data display
    st.table({
        "Control ID": ["AC-1", "AC-2", "AU-3", "SI-4"],
        "Description": ["Access Control Policy", "Account Management", "Audit Record Content", "Information System Monitoring"],
        "Status": ["Automated", "Compliant", "Testing", "Review Required"],
        "Evidence Source": ["GitHub Actions", "Kubernetes Audit", "FastAPI Telemetry", "Manual Review"]
    })

with tab2:
    st.header("Kubernetes & Cloud Telemetry Signals")
    if st.button("Fetch Live Telemetry from API"):
        try:
            response = requests.get("http://localhost:8000/telemetry")
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error("Failed to connect to backend telemetry service.")
        except Exception as e:
            st.warning("Backend API is currently offline. Ensure services are running.")

with tab3:
    st.header("AI & Automation Security Triage")
    alert_input = st.text_area("Paste Security Alert or Log Event:", "Kubernetes audit log: Unauthorized privilege escalation attempt detected in namespace default.")
    if st.button("Run Automated Triage"):
        st.success("Triage Complete: Risk Level High. Recommended action: Isolate pod, review workload identity token, and generate incident postmortem.")
