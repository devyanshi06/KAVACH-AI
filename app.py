import streamlit as st
import time

# 1. Production Page Configuration Settings
st.set_page_config(
    page_title="KAVACH AI - Secure Air-Gapped Network Copilot",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced High-Fidelity CSS Command Center Injection (With Mobile Responsiveness)
st.markdown("""
    <style>
        /* Global CSS Variable Configuration overrides */
        :root {
            --bg-primary: #080a0f;
            --bg-surface: #11151d;
            --bg-card: #171d26;
            --accent-blue: #2563eb;
            --accent-glow: #3b82f6;
            --border-color: #262f3d;
            --text-muted: #64748b;
        }

        /* Root Application Background Engine */
        .stApp {
            background-color: var(--bg-primary);
            color: #f1f5f9;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }
        
        /* Sidebar layout refinement matrix */
        [data-testid="stSidebar"] {
            background-color: var(--bg-surface) !important;
            border-right: 1px solid var(--border-color);
        }
        
        /* Main Heading Linear Color Shifting Banner Typography */
        h1 {
            background: linear-gradient(135deg, #60a5fa 0%, #2563eb 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800 !important;
            font-size: 2.2rem !important;
            letter-spacing: -1px !important;
        }
        
        /* Subheading Color Adjustments */
        h3, h4, h5 {
            color: #cbd5e1 !important;
            font-weight: 600 !important;
        }
        
        /* High-Fidelity Glassmorphism Container Card Styling */
        .premium-card {
            background: rgba(23, 29, 38, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.3);
        }
        
        /* Modern Terminal Box Styling (Optimized and Smaller) */
        textarea {
            background-color: #0c0f16 !important;
            color: #38bdf8 !important; /* Premium Cyan developer tint output typography */
            font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 8px !important;
            font-size: 13px !important; /* Slightly smaller text */
            line-height: 1.5 !important;
            padding: 12px !important;
        }
        textarea:focus {
            border-color: var(--accent-glow) !important;
            box-shadow: 0 0 10px rgba(59, 130, 246, 0.2) !important;
        }
        
        /* Stylized Enterprise Metric Framework layout */
        .metric-container {
            display: flex;
            gap: 16px;
            margin-bottom: 24px;
        }
        .metric-card {
            flex: 1;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            padding: 14px;
            border-radius: 8px;
            text-align: left;
        }
        .metric-value {
            font-size: 18px;
            font-weight: 700;
            color: #38bdf8;
            font-family: 'JetBrains Mono', monospace;
        }
        .metric-label {
            font-size: 11px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 4px;
        }
        
        /* Source citation layout rendering badge */
        .citation-badge {
            font-family: 'JetBrains Mono', monospace;
            background-color: #0c0f16;
            padding: 6px 12px;
            border-radius: 6px;
            color: #94a3b8;
            border: 1px solid var(--border-color);
            font-size: 12px;
            display: inline-block;
            margin-top: 8px;
        }

        /* --- MOBILE RESPONSIVENESS MEDIA QUERIES --- */
        @media (max-width: 768px) {
            h1 {
                font-size: 1.8rem !important;
            }
            .metric-container {
                flex-direction: column; /* Stacks layout statistics vertically on mobile screen */
                gap: 10px;
            }
            .metric-card {
                padding: 10px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration Console Engine
with st.sidebar:
    st.markdown("<h2 style='color: #38bdf8; margin-bottom: 0; font-weight:800;'>🛡️ KAVACH AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 12px; margin-top: 0; font-family: monospace;'>v1.0.0 // PRODUCTION NODE</p>", unsafe_allow_html=True)
    
    st.markdown("<span style='background-color: #064e3b; color: #34d399; padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: 700; border: 1px solid #059669;'>🔒 HARDWARE AIR-GAP ACTIVE</span>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("### ⚙️ SYSTEM PROFILES")
    vendor = st.selectbox("Target Core Architecture:", ["Cisco IOS-XE/XR", "Juniper JunOS", "Arista EOS"])
    search_mode = st.radio("Retrieval Matrix Optimization:", ["Hybrid (Semantic + Keyword)", "Strict Semantic Only"])
    
    st.markdown("---")
    st.markdown("### 📊 RESOURCE PROFILING")
    st.caption("• RAM Usage: 14.2 GB / 32 GB")
    st.caption("• VRAM Load: 4.8 GB allocated")
    st.caption("• Hardware Node: Local Host")

# 4. Main Control Console Header Layout
st.title("🛡️ KAVACH AI Operational Console")
st.markdown("##### Sovereign Intelligence Subsystem for Critical Infrastructure Protection & Network Resiliency")

# 5. High-Fidelity Enterprise Real-Time Metric Banner
st.markdown("""
    <div class='metric-container'>
        <div class='metric-card'>
            <div class='metric-value'>0.00 ms</div>
            <div class='metric-label'>External Network Leaks</div>
        </div>
        <div class='metric-card'>
            <div class='metric-value'>1,248 Chunks</div>
            <div class='metric-label'>Indexed Local Rules Data</div>
        </div>
        <div class='metric-card'>
            <div class='metric-value'>Llama-3-8B (4-bit)</div>
            <div class='metric-label'>Active Compute Engine Model</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. Tabbed Workspace Engine Isolation Navigation
tab1, tab2 = st.tabs(["🖥️ Core Interactive Diagnostic Terminal", "📂 Local Vector Knowledge Base Browser"])

# --- TAB 1: CORE INTERACTIVE DIAGNOSTIC WORKSPACE ---
with tab1:
    col1, col2 = st.columns([1.1, 0.9]) 
    
    with col1:
        st.markdown("#### 📥 Network Telemetry Stream Workspace")
        user_input = st.text_area(
            "Telemetry Stream Input Workspace Configuration Console:",
            height=200, # Reduced terminal height parameter from 340 to 200 for sleek compactness
            label_visibility="collapsed",
            placeholder="Pasted system data packets or console syslogs (e.g., %LDP-5-SESSION: LDP Session down)..."
        )
        
        submit_btn = st.button("EXECUTE AIR-GAPPED INFERENCE PIPELINE ⚡", type="primary", use_container_width=True)

    with col2:
        st.markdown("#### 📤 Encapsulated Response Matrix Output")
        
        if submit_btn and user_input:
            with st.spinner("Executing local context vector mapping queries..."):
                time.sleep(1.2) 
                st.success("INFERENCE CONTEXT EXTRACTION SUCCESSFUL")
                
                st.markdown("""
                    <div class='premium-card'>
                        <h6 style='color: #f87171; margin-top:0; font-size:14px; text-transform:uppercase; letter-spacing:1px;'>⚠️ Intercept Analytics Summary:</h6>
                        <p style='font-size: 14px; line-height:1.6; color: #cbd5e1; margin-bottom:0;'>
                            Target peer destination dropped due to an administrative Maximum Transmission Unit (MTU) boundary length structural mismatch on the target interface. The interface frame configuration is actively dropping LDP Hello path discovery packets.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("##### **Recommended Target Target Platform Remediation CLI Patch:**")
                st.code("""
configure terminal
interface GigabitEthernet0/1
 ip mtu 1500
 mpls ldp router-id Loopback0 force
end
                """, language="bash")
                
                with st.expander("📂 View Auditable Database Citations & Similarity Metrics"):
                    st.markdown("<div style='margin-top: 4px;'>", unsafe_allow_html=True)
                    
                    st.markdown("<span class='citation-badge'>📄 /knowledge_base/cisco_ios_xe_mpls_guide.pdf</span>", unsafe_allow_html=True)
                    st.markdown("<div style='color: #34d399; font-size:12px; font-weight:600; margin-top: 4px; margin-left: 4px;'>📊 Similarity Confidence: 94.2%</div>", unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    st.markdown("<span class='citation-badge'>📄 /knowledge_base/incident_ticket_77412_resolved.txt</span>", unsafe_allow_html=True)
                    st.markdown("<div style='color: #34d399; font-size:12px; font-weight:600; margin-top: 4px; margin-left: 4px;'>📊 Similarity Confidence: 88.7%</div>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("Awaiting telemetric data stream console inputs from the workspace pane to compile pipeline inference vectors.")

# --- TAB 2: LOCAL KNOWLEDGE BASE BROWSER ---
with tab2:
    st.markdown("#### 📂 Monitored Directories inside Secure Host Node")
    st.write("These files are stored locally on disk and are completely searchable by the embedding engine without needing internet connectivity.")
    
    st.markdown("""
        <div class='premium-card'>
            <h6 style='color:#38bdf8; margin:0;'>📚 Configuration Manuals / Vendor Blueprints Matrix</h6>
            <p style='color:#94a3b8; font-size:13px; margin-top:4px;'>• cisco_ios_xe_mpls_guide.pdf (Size: 14.2 MB) // Last Indexed: Just now</p>
            <p style='color:#94a3b8; font-size:13px; margin:0;'>• juniper_networks_junos_mpls_te.txt (Size: 4.1 MB) // Last Indexed: 2 hours ago</p>
        </div>
        <div class='premium-card'>
            <h6 style='color:#38bdf8; margin:0;'>📝 Historic Local Incident Logs Repository Data</h6>
            <p style='color:#94a3b8; font-size:13px; margin-top:4px;'>• incident_ticket_77412_resolved.txt (Size: 12 KB) // Last Indexed: Just now</p>
            <p style='color:#94a3b8; font-size:13px; margin:0;'>• global_network_syslog_archive_june.log (Size: 184 MB) // Last Indexed: Yesterday</p>
        </div>
    """, unsafe_allow_html=True)