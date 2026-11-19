"""
🌸 SAHAKARI AI — THE COOPERATIVE PRODUCTION TRUST OS
Streamlit Web Application & Interactive Premium Dashboard
Problem Statement 8.1: Women's self-help groups lose orders and members' trust because fulfilment and pay are chaotic.

Multilingual Support: English (en), Tamil (ta), Kannada (kn), Hindi (hi).
"""

import streamlit as st
import pandas as pd
import numpy as np
import cv2
import json
import hashlib
import time
from datetime import datetime
from PIL import Image, ImageDraw

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & MULTILINGUAL FONT SYSTEM
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Sahakari AI — Proof-to-Pay Operating System",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Contrast, Glassmorphism, Multilingual Premium Dark CSS Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+Tamil:wght@400;500;600;700&family=Noto+Sans+Kannada:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap');
    
    :root {
        --bg-main: #0b0f19;
        --surface-dark: #151d2e;
        --surface-card: linear-gradient(135deg, rgba(22, 31, 48, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        --surface-border: rgba(255, 255, 255, 0.08);
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --accent-indigo: #6366f1;
        --accent-emerald: #10b981;
    }
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', 'Inter', 'Noto Sans Tamil', 'Noto Sans Kannada', 'Noto Sans Devanagari', -apple-system, sans-serif;
        color: #f8fafc;
    }
    
    .stApp, .main {
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
    }
    
    /* Premium Glassmorphic KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, rgba(22, 31, 48, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px 22px;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 8px 30px -4px rgba(99, 102, 241, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    .kpi-label {
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        color: #94a3b8;
        letter-spacing: 0.6px;
    }
    .kpi-value {
        font-size: 28px;
        font-weight: 800;
        color: #f8fafc;
        margin-top: 6px;
        letter-spacing: -0.5px;
    }
    .kpi-sub {
        font-size: 12px;
        color: #34d399;
        font-weight: 600;
        margin-top: 4px;
    }
    
    .member-action-card {
        background: linear-gradient(135deg, rgba(22, 31, 48, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    
    /* Modern Pill Badges */
    .action-badge-green {
        background-color: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 6px 14px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 13px;
        display: inline-block;
        letter-spacing: 0.3px;
    }
    
    .action-badge-amber {
        background-color: rgba(245, 158, 11, 0.15);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.3);
        padding: 6px 14px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 13px;
        display: inline-block;
        letter-spacing: 0.3px;
    }

    .action-badge-indigo {
        background-color: rgba(99, 102, 241, 0.15);
        color: #a5b4fc;
        border: 1px solid rgba(99, 102, 241, 0.3);
        padding: 6px 14px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 13px;
        display: inline-block;
        letter-spacing: 0.3px;
    }
    
    /* Explainer Banners with Subtle Glow */
    .explainer-banner {
        background: rgba(30, 41, 59, 0.7);
        border-left: 4px solid #818cf8;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        padding: 16px 20px;
        border-radius: 10px;
        margin-bottom: 18px;
        font-size: 13.5px;
        color: #cbd5e1;
        line-height: 1.6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 8px 8px 0 0;
        color: #94a3b8;
        font-weight: 600;
        padding: 8px 16px;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(99, 102, 241, 0.15) !important;
        color: #a5b4fc !important;
        border-bottom: 2px solid #818cf8 !important;
    }

    /* Primary and Secondary Buttons */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35) !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button[kind="primary"]:hover {
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button[kind="secondary"] {
        background: rgba(30, 41, 59, 0.8) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }
    .stButton > button[kind="secondary"]:hover {
        background: rgba(51, 65, 85, 0.8) !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #f8fafc !important;
    }
    
    /* Streamlit Metric / Number display */
    [data-testid="stMetricValue"] {
        color: #f8fafc !important;
    }

    /* Input borders & backgrounds */
    .stTextInput input, .stNumberInput input {
        background-color: rgba(15, 23, 42, 0.8) !important;
        color: #f8fafc !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 10px !important;
    }
    
    /* Expander Container */
    [data-testid="stExpander"] {
        background-color: rgba(22, 31, 48, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. MULTILINGUAL DICTIONARY (EN, TA, KN, HI)
# -----------------------------------------------------------------------------
TRANSLATIONS = {
    "en": {
        "lang_tag": "en-IN",
        "app_title": "SAHAKARI AI",
        "app_subtitle": "Proof-to-Pay Intelligence Platform for Women's Self-Help Producer Groups",
        "challenge_badge": "PS 8.1 • The JanAI Mass Entrepreneurship Challenge • Tech4Bharat 2026",
        "login_box_title": "🔑 Select Language, Role & Profile",
        "select_lang": "Choose Language / மொழியைத் தேர்ந்தெடுக்கவும்:",
        "select_access": "Select Access Level:",
        "role_leader": "👑 SHG Cluster Leader",
        "role_artisan": "🧵 SHG Artisan / Member",
        "select_leader_name": "Select Leader Profile:",
        "select_artisan_name": "Select Artisan Profile:",
        "security_pin": "4-Digit Security PIN:",
        "launch_btn": "🚀 Launch Workspace",
        "demo_pin_hint": "💡 Default Demo PIN: 1234 • Zero literacy barrier with vernacular audio passbook",
        "switch_profile": "🚪 Switch Profile / Logout",
        "leader_view_badge": "👑 LEADER VIEW",
        "artisan_view_badge": "🧵 ARTISAN VIEW",
        "active_bulk_order": "Active Bulk Order",
        "stage_b_throughput": "Stage B Throughput",
        "jains_index": "Jain's Fairness Index",
        "enterprise_quote": "Enterprise Quote Target",
        "proven_fair": "Target ≥ 0.9500 (PROVEN FAIR)",
        "tab1": "📊 1. Production Pipeline & Schedule",
        "tab2": "⚡ 2. 7-Phase Agentic Rebalancing (Day 4)",
        "tab3": "💰 3. Anti-Underpricing Costing BOM",
        "tab4": "🔍 4. Assistive CV Quality Desk",
        "tab5": "🗳️ 5. Micro-Payroll & Quorum Gate",
        "tab6": "📄 6. B2B Order Passport",
        "pipeline_overview_title": "🏭 Conserved 3-Stage Production Pipeline",
        "stage_a_title": "✂️ Stage A: Cutting & Kitting (2 Members)",
        "stage_b_title": "🧵 Stage B: Sewing & Assembly (8 Members • BOTTLENECK)",
        "stage_c_title": "🏷️ Stage C: Finishing, QC & Pack (2 Members)",
        "morning_rollcall_title": "🌅 Daily Morning Roll-Call & Machine Availability Studio",
        "morning_rollcall_desc": "In the morning, the Leader records who is present and machine health. Quotas and fairness index recalculate automatically for the day.",
        "btn_save_rollcall": "💾 Save Today's Morning Availability & Recalculate Quotas",
        "rollcall_saved_toast": "Morning roll-call saved! Today's group capacity: {cap} sets/day. Jain's Fairness Index: {jain}",
        "table_title": "📋 12-Member Dynamic Allocation & Capacity Table",
        "jains_note": "💡 Jain's Fairness Index: {val} (Mathematical proof that workload is distributed proportionally to individual machine speed and available caregiving hours).",
        "day4_crisis_title": "⚡ 7-Phase Bounded Delay-Recovery Agent",
        "day4_explainer": "💡 WHAT IS THIS? This is the automated emergency assistant. When a woman gets sick on Day 4, traditional SHGs fail because nobody notices until delivery day. This agent detects the shortfall, checks downstream buffers, finds volunteer peers with spare machine capacity, asks their consent (no forced labor), and safely recovers the deadline.",
        "day4_crisis_desc": "Operational Incident: On Day 4, Member M06 (Geetha Shankar) experiences family illness and reports 0 of 7 scheduled sewing units. The agent executes a consensual, capacity-bounded recovery.",
        "sim_emergency_btn": "🚨 Simulate Day 4 M06 Emergency (Trigger Shortfall)",
        "agent_generate_btn": "🧠 Agent: Search Spare Buffers & Generate Proposal",
        "obtain_consent_btn": "🤝 Obtain Member Consent (Simulate M02 & M03 Opt-in)",
        "commit_rebalance_btn": "💾 Leader: Commit & Update Production State",
        "reset_sim_btn": "🔄 Reset Incident Simulation",
        "phase1_title": "1. DETECT",
        "phase1_desc": "Senses Day 4 pipeline shortfall: Member M06 completed 0 of 7 units due to domestic illness.",
        "phase2_title": "2. INVESTIGATE",
        "phase2_desc": "Inspects Stage B queue & Stage C buffer: 35 units in buffer = 3.5 operating hours before line starvation.",
        "phase3_title": "3. GENERATE",
        "phase3_desc": "Synthesizes candidate transfer: Split 7 units into 4 units to M03 (Selvi) + 3 units to M02 (Lakshmi).",
        "phase4_title": "4. EVALUATE",
        "phase4_desc": "Verifies constraint bounds: M03 spare buffer 50.1 sets (4 <= 0.75*50.1); M02 buffer 42.8 sets (3 <= 0.75*42.8).",
        "phase5_title": "5. EXPLAIN",
        "phase5_desc": "Synthesized audio explanation: 'Volunteer rebalance proposal sent to Selvi (4) and Lakshmi (3)...'",
        "phase6_title": "6. APPROVE (GOVERNANCE GATE)",
        "phase6_desc": "HALTS EXECUTION! Requires voluntary member opt-in. Zero forced algorithmic labor.",
        "phase7_title": "7. COMMIT",
        "phase7_desc": "Appends immutable rebalance event to CPL ledger with previous_event_hash. Recomputes Jain's Index: J = 0.9841.",
        "bom_explainer": "💡 WHAT IS THIS? Rural women underprice by 30–40% because fabric shrinkage, trims, cutting wastage, and machine upkeep are never calculated. When a buyer makes an offer, this tool tests it against 3 financial baselines so the group never takes an order at a loss.",
        "buyer_offer_label": "Simulate Buyer Price Offer per Set (₹):",
        "vs_operating_floor": "1. Cash Break-Even Floor (₹260.55)",
        "vs_cost_plus": "2. Group Safety + 12% Reserve (₹291.82)",
        "vs_enterprise_margin": "3. Enterprise Quote + 10% Margin (₹324.24)",
        "predatory_alert": "⚠️ PREDATORY UNDERPRICING ALERT: Buyer offer of ₹{offer}.00 fails to cover baseline material and operating costs by ₹{deficit}/unit. Accepting this offer causes ₹{loss:,} in uncompensated losses across the 500-set batch!",
        "bom_title": "Itemized Unit Economics BOM (500 Sets)",
        "cv_title": "🔍 Assistive Computer Vision Quality Pre-Screening",
        "cv_desc": "Operational Boundary: The Computer Vision pipeline is assistive only (screening for blur and gross placket asymmetry). The Human Group Leader retains 100% final decision authority.",
        "cv_sample_prompt": "Select Realistic Uniform Shirt Sample for Inspection:",
        "cv_sample1": "Sample 1: ✅ High-Quality Standard Uniform Shirt (Straight Placket)",
        "cv_sample2": "Sample 2: ⚠️ Blurry Low-Light Photo (Laplacian Var < 55)",
        "cv_sample3": "Sample 3: ❌ Crooked / Asymmetric Placket Seam (Angle > 3.5°)",
        "cv_or_upload": "Or Upload Real Garment Photo for Live Inspection:",
        "cv_original": "Uniform Shirt Image Under Test:",
        "cv_overlay": "OpenCV Hough Seam Overlay:",
        "cv_diagnostics": "Pre-Screen Diagnostics",
        "blur_var_label": "Laplacian Blur Variance",
        "angle_dev_label": "Max Placket Angular Deviation",
        "human_decision": "Human Leader Decision:",
        "btn_accept": "✅ Accept",
        "btn_rework": "⚠️ Rework",
        "btn_reject": "❌ Reject",
        "payroll_title": "🗳️ Democratic Micro-Payroll & Quorum Authorization",
        "payroll_desc": "Democratic Quorum Gate: Payout statements are frozen in a deterministic SHA-256 snapshot. Final authorization requires Leader signature + 66.7% member quorum (8 of 12 votes).",
        "quorum_progress_label": "Member Consensus Quorum Progress:",
        "quorum_met": "✅ QUORUM THRESHOLD MET (≥ 66.7%): Payout statement is eligible for final leader signature and external batch disbursement!",
        "quorum_pending": "⏳ QUORUM PENDING: Need {needed} more affirmative votes to achieve two-thirds majority.",
        "btn_cast_votes": "🗳️ Cast Positive Votes for Pending Members",
        "btn_sign_disburse": "✍️ Leader Sign & Export Simulated UPI Batch",
        "passport_title": "📄 B2B Order Passport & Fair Wage Traceability Dossier",
        "passport_desc": "Buyers (school districts, CSR programs, garment brands) receive an auditable, privacy-safe Order Passport verifying ethical labor, material compliance, and on-time fulfilment.",
        "btn_download_passport": "📥 Download Official B2B Order Passport (TXT/PDF)",
        # Member View Translations
        "member_greeting": "Welcome, {name}!",
        "member_workspace_sub": "Member Workspace • {stage} • Machine: {machine}",
        "my_work_today_title": "1. 🟢 My Work Today",
        "today_target_badge": "TODAY'S TARGET",
        "shirts_unit": "shirts",
        "piece_rate_label": "Rate: ₹{rate} / shirt",
        "completed_submission_title": "2. 📸 I Completed / Work Submission",
        "completed_units_label": "Completed Units Today:",
        "offline_toggle_label": "✈️ Simulate Offline Mode (No Internet)",
        "submit_work_btn": "📤 Submit Completed Work",
        "saved_offline_msg": "🟡 Saved in Local IndexedDB Outbox: {qty} shirts recorded. Will auto-sync when network is restored!",
        "synced_online_msg": "✅ Successfully Recorded! {qty} shirts credited to your ledger. Receipt: REC-{ts}",
        "network_restored_msg": "📶 Network Restored! Auto-syncing {count} offline entries without duplicates...",
        "upload_garment_photo": "Upload Photo of Completed Garment:",
        "take_camera_photo": "Or Take Photo Using Device Camera:",
        "photo_pass_msg": "🟢 Photo Quality Verified: Crisp & Clear (Laplacian: {val} > 55.0) — Ready to submit!",
        "photo_blur_fail_msg": "🔴 Photo Too Blurry (Laplacian: {val} < 55.0) — Please hold phone steady and retake in good lighting!",
        "hear_earnings_title": "3. 🔊 Hear My Audio Passbook",
        "gross_label": "Gross Work Earned",
        "advance_label": "Advance Deducted",
        "net_payable_label": "Net Payable to Bank Account",
        "awaiting_quorum_badge": "⏳ Awaiting Group Approval",
        "audio_btn_text": "🔊 Listen to My Earnings Audio Passbook",
        "dispute_btn_text": "⚠️ Report an Error / Dispute an Entry",
        "dispute_raised_msg": "⚠️ Dispute recorded. Affected advance amount is frozen in escrow while undisputed earnings proceed!",
        "withdraw_dispute_btn": "✅ Withdraw Dispute",
        "quorum_vote_title": "4. 🗳️ Cast Quorum Vote for Group Payroll",
        "vote_approve_btn": "👍 I Approve This Payroll",
        "vote_object_btn": "❌ I Object to This Payroll",
        "vote_cast_toast": "Your vote was recorded successfully!",
        "current_vote_caption": "Your Current Vote Status: {status} • Governed by collective group bylaws."
    },
    "ta": {
        "lang_tag": "ta-IN",
        "app_title": "சககாரி AI (SAHAKARI AI)",
        "app_subtitle": "சுயஉதவிக் குழு பெண்களுக்கான உற்பத்தி மற்றும் ஊதிய மேலாண்மை தளம்",
        "challenge_badge": "PS 8.1 • The JanAI Mass Entrepreneurship Challenge • Tech4Bharat 2026",
        "login_box_title": "🔑 மொழி, பங்கு மற்றும் சுயவிவரத்தை தேர்வு செய்க",
        "select_lang": "மொழியைத் தேர்ந்தெடுக்கவும்:",
        "select_access": "உங்கள் பங்கு (Select Role):",
        "role_leader": "👑 SHG குழுத் தலைவி (Leader)",
        "role_artisan": "🧵 SHG உறுப்பினர் (Artisan / Member)",
        "select_leader_name": "தலைவர் சுயவிவரம்:",
        "select_artisan_name": "உறுப்பினர் சுயவிவரம்:",
        "security_pin": "4-இலக்க பாதுகாப்புக் குறியீடு (PIN):",
        "launch_btn": "🚀 பணித்தளத்தை தொடங்கு",
        "demo_pin_hint": "💡 மாதிரி குறியீடு (Demo PIN): 1234 • குரல் பாஸ்புக் ஆதரவுடன்",
        "switch_profile": "🚪 சுயவிவரம் மாற்று / வெளியேறு",
        "leader_view_badge": "👑 தலைவர் பார்வை (LEADER)",
        "artisan_view_badge": "🧵 உறுப்பினர் பார்வை (ARTISAN)",
        "active_bulk_order": "செயலில் உள்ள மொத்த ஆணை",
        "stage_b_throughput": "தையல் பிரிவு உற்பத்தி (Stage B)",
        "jains_index": "ஜெயின் சமத்துவ குறியீடு (Jain's Index)",
        "enterprise_quote": "பரிந்துரைக்கப்பட்ட வணிக விலை",
        "proven_fair": "இலக்கு ≥ 0.9500 (நிரூபிக்கப்பட்ட சமத்துவம்)",
        "tab1": "📊 1. உற்பத்தி வரிசை & ஒதுக்கீடு",
        "tab2": "⚡ 2. தன்னாட்சி மறுஒதுக்கீடு (Day 4 Crisis)",
        "tab3": "💰 3. விலை நிர்ணய கணக்கீடு (Costing BOM)",
        "tab4": "🔍 4. கணினி பார்வை தர ஆய்வு (Vision QC)",
        "tab5": "🗳️ 5. ஊதிய ஒப்புதல் & வாக்குப்பதிவு (Quorum)",
        "tab6": "📄 6. வாடிக்கையாளர் ஆவணம் (Order Passport)",
        "pipeline_overview_title": "🏭 3-நிலை தொடர் உற்பத்தி வரிசை",
        "stage_a_title": "✂️ பிரிவு A: துணி வெட்டுதல் (2 உறுப்பினர்கள்)",
        "stage_b_title": "🧵 பிரிவு B: சட்டை தையல் (8 உறுப்பினர்கள் • முக்கிய பிரிவு)",
        "stage_c_title": "🏷️ பிரிவு C: பொத்தான் & பொதி செய்தல் (2 உறுப்பினர்கள்)",
        "morning_rollcall_title": "🌅 காலை வருகை பதிவு & இயந்திர நிலை (Morning Roll-Call)",
        "morning_rollcall_desc": "காலையில் யார் வந்துள்ளார்கள் மற்றும் இயந்திர நிலையை தலைவர் இதில் பதிவு செய்யலாம். தினசரி இலக்கு தானாக மாறும்.",
        "btn_save_rollcall": "💾 காலை வருகை & ஒதுக்கீட்டை சேமிக்க",
        "rollcall_saved_toast": "காலை வருகை சேமிக்கப்பட்டது! இன்றைய குழு திறன்: {cap} சட்டைகள்/நாள். சமத்துவ குறியீடு: {jain}",
        "table_title": "📋 12-உறுப்பினர்களின் தினசரி திறன் மற்றும் ஒதுக்கீட்டு அட்டவணை",
        "jains_note": "💡 ஜெயின் சமத்துவ குறியீடு: {val} (இயந்திர வேகம் மற்றும் வீட்டு நேரத்திற்கு ஏற்ப வேலை சமமாக பகிரப்பட்டதற்கான கணித ஆதாரம்).",
        "day4_crisis_title": "⚡ 7-படிநிலை தாமத மீட்பு தன்னாட்சி முகவர்",
        "day4_explainer": "💡 இதன் பங்கு என்ன? இது குழுவின் அவசர உதவி முகவர். 4-ஆம் நாளில் ஒரு பெண்ணுக்கு உடல்நிலை சரியில்லாமல் போனால் வழக்கமான குழுக்களில் கடைசி நாள் வரை தெரியாது, ஆணை ரத்தாகும். ஆனால் இந்த முகவர் பற்றாக்குறையை உடனடியாக கண்டறிந்து, ஓய்வு நேரம் உள்ள சக உறுப்பினர்களிடம் சம்மதம் கேட்டு வேலையை பகிர்ந்து குழுவின் ஆணையை காப்பாற்றுகிறது.",
        "day4_crisis_desc": "செயல்பாட்டு நிகழ்வு: 4-ஆம் நாளில் உறுப்பினர் கீதா சங்கர் (M06) குடும்ப நோய் காரணமாக 7 சட்டைகளை முடிக்கவில்லை. முகவர் விருப்ப அடிப்படையிலான மறுஒதுக்கீட்டை செய்கிறது.",
        "sim_emergency_btn": "🚨 4-ஆம் நாள் அவசரநிலையை உருவகப்படுத்து (M06 Shortfall)",
        "agent_generate_btn": "🧠 முகவர்: கூடுதல் திறன் உள்ளோரை கண்டறிந்து பரிந்துரை செய்",
        "obtain_consent_btn": "🤝 உறுப்பினர்களின் ஒப்புதல் பெறு (செல்வி & லட்சுமி விருப்பம்)",
        "commit_rebalance_btn": "💾 தலைவர்: ஒப்புதல் அளித்து பதிவேட்டில் சேமி",
        "reset_sim_btn": "🔄 உருவகப்படுத்துதலை மீட்டமை (Reset)",
        "phase1_title": "1. கண்டறிதல் (DETECT)",
        "phase1_desc": "4-ஆம் நாள் பற்றாக்குறை: உறுப்பினர் M06 நோய் காரணமாக 7 சட்டைகளை முடிக்கவில்லை.",
        "phase2_title": "2. ஆய்வு (INVESTIGATE)",
        "phase2_desc": "அடுத்த பிரிவின் கையிருப்பு 35 சட்டைகள் (3.5 மணி நேர வேலை பாதுகாப்பு உள்ளது).",
        "phase3_title": "3. திட்டம் உருவாக்குதல் (GENERATE)",
        "phase3_desc": "7 சட்டைகளை செல்வி (4) மற்றும் லட்சுமிக்கு (3) பகிர்ந்தளிக்கும் திட்டம்.",
        "phase4_title": "4. கணித சரிபார்ப்பு (EVALUATE)",
        "phase4_desc": "செல்வியின் கூடுதல் திறன் 50.1 சட்டைகள்; லட்சுமியின் கூடுதல் திறன் 42.8 சட்டைகள் (விதிக்குள் உள்ளது).",
        "phase5_title": "5. விளக்குதல் (EXPLAIN)",
        "phase5_desc": "குரல் வழி விளக்கம்: 'கீதா அவர்களுக்கு பதில் செல்வி (4) மற்றும் லட்சுமி (3) கூடுதல் பணி ஏற்க ஒப்புதல்...'",
        "phase6_title": "6. உறுப்பினர் ஒப்புதல் (GOVERNANCE GATE)",
        "phase6_desc": "இயக்கம் நிற்கிறது! கட்டாய வேலை திணிப்பு இன்றி உறுப்பினர்களின் சுயமாக சம்மதம் தேவை.",
        "phase7_title": "7. பதிவேற்றம் (COMMIT)",
        "phase7_desc": "மாற்ற முடியாத பதிவேட்டில் பதிவு செய்யப்படுகிறது. புதிய சமத்துவ குறியீடு: J = 0.9841.",
        "bom_explainer": "💡 இதன் பங்கு என்ன? துணி கழிவு, தையல் இயந்திர தேய்மானம் ஆகியவற்றை கணக்கிடாததால் பெண்கள் 30-40% குறைந்த விலைக்கு வேலை செய்கிறார்கள். வாங்குபவர் தரும் விலையை 3 நிலைகளில் சோதித்து நஷ்டத்தை தடுக்க இந்த கருவி உதவுகிறது.",
        "buyer_offer_label": "வாங்குபவர் வழங்கும் விலையை சோதிக்க (₹):",
        "vs_operating_floor": "1. அடிப்படை உற்பத்தி செலவு (₹260.55)",
        "vs_cost_plus": "2. 12% சேமிப்பு நிதியுடன் (₹291.82)",
        "vs_enterprise_margin": "3. 10% நிறுவன லாபத்துடன் (₹324.24)",
        "predatory_alert": "⚠️ குறைந்த விலை எச்சரிக்கை: வாங்குபவரின் ₹{offer}.00 சலுகை அடிப்படை உற்பத்தி செலவை விட ₹{deficit}/சட்டை குறைவாக உள்ளது. இதை ஏற்றால் ₹{loss:,} நஷ்டம் ஏற்படும்!",
        "bom_title": "பொருளாதார உற்பத்தி செலவு பட்டியல் (500 சீருடைகள்)",
        "cv_title": "🔍 கணினி பார்வை உதவி தரப் பரிசோதனை (Vision Pre-Screening)",
        "cv_desc": "செயல்பாட்டு எல்லை: கணினி பார்வை மங்கலான படம் மற்றும் தையல் கோணத்தை மட்டுமே சுட்டிக்காட்டும். இறுதி முடிவை மனித தலைவரே (அணித்தலைவி) எடுப்பார்.",
        "cv_sample_prompt": "ஆய்வுக்கான மாதிரி ஆடை படத்தை தேர்ந்தெடுக்கவும்:",
        "cv_sample1": "மாதிரி 1: ✅ நல்ல தரமான சீருடை சட்டை (நேரான தையல்)",
        "cv_sample2": "மாதிரி 2: ⚠️ மங்கலான புகைப்படம் (Laplacian Var < 55)",
        "cv_sample3": "மாதிரி 3: ❌ கோணலான பொத்தான் பட்டி தையல் (Angle > 3.5°)",
        "cv_or_upload": "அல்லது உண்மையான ஆடை படத்தை பதிவேற்றவும்:",
        "cv_original": "ஆய்வு செய்யப்படும் சட்டை படம்:",
        "cv_overlay": "OpenCV தையல் நேர்கோடு பகுப்பாய்வு:",
        "cv_diagnostics": "ஆய்வு முடிவுகள் (Diagnostics)",
        "blur_var_label": "மங்கலான அளவு (Laplacian Variance)",
        "angle_dev_label": "பட்டி தையல் கோண விலகல்",
        "human_decision": "அணித்தலைவரின் முடிவு:",
        "btn_accept": "✅ ஏற்றுக்கொள் (Accept)",
        "btn_rework": "⚠️ திருத்தம் செய் (Rework)",
        "btn_reject": "❌ நிராகரி (Reject)",
        "payroll_title": "🗳️ ஜனநாயக ஊதிய ஒப்புதல் & குழு வாக்குப்பதிவு",
        "payroll_desc": "ஜனநாயக ஒப்புதல் வாயில்: ஊதிய பட்டியல் மாற்ற முடியாத SHA-256 குறியீட்டில் பூட்டப்பட்டுள்ளது. தலைவர் கையொப்பம் மற்றும் 66.7% உறுப்பினர் வாக்குகள் தேவை.",
        "quorum_progress_label": "குழுவின் ஒப்புதல் வாக்கு முன்னேற்றம்:",
        "quorum_met": "✅ பெரும்பான்மை வாக்குகள் பெறப்பட்டன (≥ 66.7%): ஊதியப் பட்டியல் வங்கி பரிமாற்றத்திற்கு தயாராக உள்ளது!",
        "quorum_pending": "⏳ ஒப்புதல் நிலுவையில் உள்ளது: இன்னும் {needed} வாக்குகள் தேவை.",
        "btn_cast_votes": "🗳️ நிலுவையில் உள்ள உறுப்பினர்களின் வாக்குகளை பதிவு செய்",
        "btn_sign_disburse": "✍️ தலைவர் கையொப்பமிட்டு வங்கிக்கு அனுப்புக",
        "passport_title": "📄 B2B வாடிக்கையாளர் ஆவணம் (Order Passport)",
        "passport_desc": "வாங்குபவர்கள் (பள்ளிகள், பெருநிறுவனங்கள்) நியாயமான ஊதியம் மற்றும் தரத்தை சரிபார்க்கும் அதிகாரப்பூர்வ ஆவணம்.",
        "btn_download_passport": "📥 அதிகாரப்பூர்வ ஆவணத்தை பதிவிறக்கு (Download Passport)",
        # Member View Translations
        "member_greeting": "வணக்கம் {name}!",
        "member_workspace_sub": "உறுப்பினர் பணித்தளம் • {stage} • இயந்திரம்: {machine}",
        "my_work_today_title": "1. 🟢 என் இன்றைய வேலை",
        "today_target_badge": "இன்றைய இலக்கு (TARGET)",
        "shirts_unit": "சட்டைகள்",
        "piece_rate_label": "கட்டணம்: ₹{rate} / சட்டை",
        "completed_submission_title": "2. 📸 முடித்தேன் - சமர்ப்பி",
        "completed_units_label": "இன்று முடித்த எண்ணிக்கை:",
        "offline_toggle_label": "✈️ இணையம் இல்லை / ஆஃப்லைன் பயன்முறை (Offline Mode)",
        "submit_work_btn": "📤 வேலையை பதிவு செய்",
        "saved_offline_msg": "🟡 ஆஃப்லைனில் பாதுகாப்பாக சேமிக்கப்பட்டது: {qty} சட்டைகள் பதிவாகியுள்ளது. இணையம் வந்ததும் தானாக சர்வரில் இணையும்!",
        "synced_online_msg": "✅ வெற்றிகரமாக பதிவானது! {qty} சட்டைகள் உங்கள் கணக்கில் சேர்க்கப்பட்டது. ரசீது: REC-{ts}",
        "network_restored_msg": "📶 இணையம் கிடைத்துள்ளது! ஆஃப்லைனில் உள்ள {count} பதிவுகள் சர்வரில் ஒத்திசைக்கப்படுகின்றன...",
        "upload_garment_photo": "முடித்த ஆடையின் புகைப்படத்தை பதிவேற்றுக:",
        "take_camera_photo": "அல்லது கேமரா மூலம் புகைப்படம் எடுக்கவும்:",
        "photo_pass_msg": "🟢 படத்தின் தரம் சரியானது: மங்கலில்லை (Laplacian: {val} > 55.0) — சமர்ப்பிக்க தயார்!",
        "photo_blur_fail_msg": "🔴 படம் மிகவும் மங்கலாக உள்ளது (Laplacian: {val} < 55.0) — நல்ல வெளிச்சத்தில் மீண்டும் எடுக்கவும்!",
        "hear_earnings_title": "3. 🔊 என் வருமானம் கேள் (குரல் பாஸ்புக்)",
        "gross_label": "மொத்த உழைப்பு வருமானம்",
        "advance_label": "முன்பணம் கழிவு",
        "net_payable_label": "வங்கியில் சேரும் நிகர தொகை",
        "awaiting_quorum_badge": "⏳ குழு ஒப்புதலுக்கு காத்திருக்கிறது",
        "audio_btn_text": "🔊 என் கணக்கை தமிழில் கேள் (Listen in Tamil)",
        "dispute_btn_text": "⚠️ தவறான பதிவு - புகார் செய் (Dispute)",
        "dispute_raised_msg": "⚠️ புகார் பதிவு செய்யப்பட்டுள்ளது. மறுக்கப்பட்ட தொகை மட்டும் நிறுத்தி வைக்கப்பட்டு, மற்ற ஊதியம் பாதுகாக்கப்படும்!",
        "withdraw_dispute_btn": "✅ புகாரை திரும்பப் பெறு",
        "quorum_vote_title": "4. 🗳️ ஊதிய ஒப்புதல் வாக்கு (Quorum Vote)",
        "vote_approve_btn": "👍 நான் இந்த ஊதியப் பட்டியலை ஏற்கிறேன்",
        "vote_object_btn": "❌ எனக்கு ஆட்சேபனை உள்ளது",
        "vote_cast_toast": "உங்கள் வாக்கு வெற்றிகரமாக பதிவானது!",
        "current_vote_caption": "உங்கள் தற்போதைய வாக்கு: {status} • குழு விதிகளுக்கு உட்பட்டது."
    },
    "kn": {
        "lang_tag": "kn-IN",
        "app_title": "ಸಹಕಾರಿ AI (SAHAKARI AI)",
        "app_subtitle": "ಮಹಿಳಾ ಸ್ವಸಹಾಯ ಉತ್ಪಾದಕ ಗುಂಪುಗಳಿಗೆ ಪಾರದರ್ಶಕ ಉತ್ಪಾದನೆ ಮತ್ತು ವೇತನ ವೇದಿಕೆ",
        "challenge_badge": "PS 8.1 • The JanAI Mass Entrepreneurship Challenge • Tech4Bharat 2026",
        "login_box_title": "🔑 ಭಾಷೆ, ಪಾತ್ರ ಮತ್ತು ಪ್ರೊಫೈಲ್ ಆಯ್ಕೆಮಾಡಿ",
        "select_lang": "ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "select_access": "ನಿಮ್ಮ ಪ್ರವೇಶ ಮಟ್ಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "role_leader": "👑 SHG ಗುಂಪಿನ ಮುಖ್ಯಸ್ಥೆ (Leader)",
        "role_artisan": "🧵 SHG ಸದಸ್ಯೆ / ಕುಶಲಕರ್ಮಿ (Artisan)",
        "select_leader_name": "ಮುಖ್ಯಸ್ಥೆಯ ಪ್ರೊಫೈಲ್ ಆಯ್ಕೆಮಾಡಿ:",
        "select_artisan_name": "ಸದಸ್ಯೆಯ ಪ್ರೊಫೈಲ್ ಆಯ್ಕೆಮಾಡಿ:",
        "security_pin": "4-ಅಂಕಿಯ ಭದ್ರತಾ ಪಿನ್ (PIN):",
        "launch_btn": "🚀 ಕಾರ್ಯಸ್ಥಳವನ್ನು ಪ್ರಾರಂಭಿಸಿ",
        "demo_pin_hint": "💡 ಡೆಮೊ ಪಿನ್: 1234 • ಸ್ಥಳೀಯ ಧ್ವನಿ ಪಾಸ್‌ಬುಕ್ ಬೆಂಬಲದೊಂದಿಗೆ",
        "switch_profile": "🚪 ಪ್ರೊಫೈಲ್ ಬದಲಾಯಿಸಿ / ನಿರ್ಗಮಿಸಿ",
        "leader_view_badge": "👑 ನಾಯಕಿ ವೀಕ್ಷಣೆ (LEADER)",
        "artisan_view_badge": "🧵 ಸದಸ್ಯೆ ವೀಕ್ಷಣೆ (ARTISAN)",
        "active_bulk_order": "ಸಕ್ರಿಯ ಬೃಹತ್ ಆದೇಶ",
        "stage_b_throughput": "ಹೊಲಿಗೆ ವಿಭಾಗದ ಉತ್ಪಾದನೆ (Stage B)",
        "jains_index": "ಜೈನ್ ನ್ಯಾಯಸಮ್ಮತ ಸೂಚ್ಯಂಕ (Jain's Index)",
        "enterprise_quote": "ಉದ್ದೇಶಿತ ವಾಣಿಜ್ಯ ಬೆಲೆ",
        "proven_fair": "ಗುರಿ ≥ 0.9500 (ಸಾಬೀತಾದ ನ್ಯಾಯಸಮ್ಮತತೆ)",
        "tab1": "📊 1. ಉತ್ಪಾದನಾ ಹರಿವು ಮತ್ತು ಹಂಚಿಕೆ",
        "tab2": "⚡ 2. ಸ್ವಾಯತ್ತ ಮರುಹಂಚಿಕೆ (Day 4 Crisis)",
        "tab3": "💰 3. ವೆಚ್ಚ ಮತ್ತು ಬೆಲೆ ನಿರ್ಣಯ (BOM)",
        "tab4": "🔍 4. ಗಣಕ ದೃಷ್ಟಿ ಗುಣಮಟ್ಟ ತಪಾಸಣೆ (Vision QC)",
        "tab5": "🗳️ 5. ವೇತನ ಅನುಮೋದನೆ ಮತ್ತು ಮತದಾನ",
        "tab6": "📄 6. ಗ್ರಾಹಕರ ಆದೇಶ ಪಾಸ್‌ಪೋರ್ಟ್",
        "pipeline_overview_title": "🏭 ಸಂರಕ್ಷಿತ 3-ಹಂತದ ಉತ್ಪಾದನಾ ಹರಿವು",
        "stage_a_title": "✂️ ಹಂತ A: ಬಟ್ಟೆ ಕತ್ತರಿಸುವುದು (2 ಸದಸ್ಯರು)",
        "stage_b_title": "🧵 ಹಂತ B: ಸಮವಸ್ತ್ರ ಹೊಲಿಗೆ (8 ಸದಸ್ಯರು • ಪ್ರಮುಖ ಹಂತ)",
        "stage_c_title": "🏷️ ಹಂತ C: ಅಂತಿಮ ಸ್ಪರ್ಶ ಮತ್ತು ಪ್ಯಾಕಿಂಗ್ (2 ಸದಸ್ಯರು)",
        "morning_rollcall_title": "🌅 ಬೆಳಗಿನ ಹಾಜರಾತಿ ಮತ್ತು ಯಂತ್ರ ಲಭ್ಯತೆ (Morning Roll-Call)",
        "morning_rollcall_desc": "ಮುಖ್ಯಸ್ಥೆಯು ಪ್ರತಿದಿನ ಬೆಳಿಗ್ಗೆ ಯಾರು ಹಾಜರಿದ್ದಾರೆ ಮತ್ತು ಯಂತ್ರದ ಸ್ಥಿತಿಯನ್ನು ದಾಖಲಿಸುತ್ತಾರೆ. ದಿನದ ಗುರಿಗಳು ತಕ್ಷಣವೇ ಮರುಹೊಂದಾಣಿಕೆಯಾಗುತ್ತವೆ.",
        "btn_save_rollcall": "💾 ಇಂದಿನ ಹಾಜರಾತಿ ಮತ್ತು ಹಂಚಿಕೆಯನ್ನು ಉಳಿಸಿ",
        "rollcall_saved_toast": "ಬೆಳಗಿನ ಹಾಜರಾತಿ ಉಳಿಸಲಾಗಿದೆ! ಇಂದಿನ ಗುಂಪಿನ ಸಾಮರ್ಥ್ಯ: {cap} ಸಮವಸ್ತ್ರಗಳು/ದಿನ. ಜೈನ್ ಸೂಚ್ಯಂಕ: {jain}",
        "table_title": "📋 12-ಸದಸ್ಯರ ಸಾಮರ್ಥ್ಯ ಮತ್ತು ಹಂಚಿಕೆ ಕೋಷ್ಟಕ",
        "jains_note": "💡 ಜೈನ್ ನ್ಯಾಯಸಮ್ಮತ ಸೂಚ್ಯಂಕ: {val} (ಯಂತ್ರ ಮತ್ತು ಮನೆಕೆಲಸದ ಸಮಯಕ್ಕೆ ಅನುಗುಣವಾಗಿ ಕೆಲಸ ಹಂಚಿಕೆಯಾಗಿರುವ ಗಣಿತದ ಪುರಾವೆ).",
        "day4_crisis_title": "⚡ 7-ಹಂತದ ವಿಳಂಬ ಚೇತರಿಕೆ ಸ್ವಾಯತ್ತ ಏಜೆಂಟ್",
        "day4_explainer": "💡 ಇದರ ಪಾತ್ರವೇನು? ಇದು ತುರ್ತು ಪರಿಸ್ಥಿತಿಯ ಸ್ವಯಂಚಾಲಿತ ಸಹಾಯಕ. 4 ನೇ ದಿನ ಮಹಿಳೆಯೊಬ್ಬರಿಗೆ ಅನಾರೋಗ್ಯವಾದಾಗ, ವಿತರಣಾ ದಿನದವರೆಗೆ ಯಾರಿಗೂ ತಿಳಿಯದೆ ಆದೇಶ ರದ್ದಾಗುವುದನ್ನು ಇದು ತಡೆಯುತ್ತದೆ. ಈ ಏಜೆಂಟ್ ವಿಳಂಬವನ್ನು ಪತ್ತೆಹಚ್ಚಿ, ಬಿಡುವಿರುವ ಇತರ ಸದಸ್ಯರ ಸಮ್ಮತಿಯೊಂದಿಗೆ ಕೆಲಸವನ್ನು ಹಂಚಿ ಆದೇಶವನ್ನು ಪೂರ್ಣಗೊಳಿಸುತ್ತದೆ.",
        "day4_crisis_desc": "ಘಟನೆ: 4 ನೇ ದಿನ ಗೀತಾ ಶಂಕರ್ (M06) ಕುಟುಂಬ ಅನಾರೋಗ್ಯದಿಂದಾಗಿ 7 ಸಮವಸ್ತ್ರಗಳನ್ನು ಹೊಲಿಯಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ಏಜೆಂಟ್ ಒಪ್ಪಿಗೆಯ ಆಧಾರದ ಮೇಲೆ ಮರುಹಂಚಿಕೆ ಮಾಡುತ್ತದೆ.",
        "sim_emergency_btn": "🚨 4 ನೇ ದಿನದ ತುರ್ತು ಪರಿಸ್ಥಿತಿ ಸಿಮ್ಯುಲೇಶನ್ (M06 Shortfall)",
        "agent_generate_btn": "🧠 ಏಜೆಂಟ್: ಹೆಚ್ಚುವರಿ ಸಾಮರ್ಥ್ಯ ಹುಡುಕಿ ಪ್ರಸ್ತಾಪ ರಚಿಸಿ",
        "obtain_consent_btn": "🤝 ಸದಸ್ಯರ ಒಪ್ಪಿಗೆ ಪಡೆಯಿರಿ (ಸೆಲ್ವಿ ಮತ್ತು ಲಕ್ಷ್ಮಿ ಒಪ್ಪಿಗೆ)",
        "commit_rebalance_btn": "💾 ಮುಖ್ಯಸ್ಥೆ: ಒಪ್ಪಿಗೆ ನೀಡಿ ಖಾತೆಗೆ ಸೇರಿಸಿ",
        "reset_sim_btn": "🔄 ಸಿಮ್ಯುಲೇಶನ್ ಮರುಹೊಂದಿಸಿ (Reset)",
        "phase1_title": "1. ಪತ್ತೆಹಚ್ಚುವಿಕೆ (DETECT)",
        "phase1_desc": "4 ನೇ ದಿನದ ಕೊರತೆ: ಸದಸ್ಯೆ M06 ಅನಾರೋಗ್ಯದ ಕಾರಣ 7 ಯೂನಿಟ್ ಹೊಲಿದಿಲ್ಲ.",
        "phase2_title": "2. ತನಿಖೆ (INVESTIGATE)",
        "phase2_desc": "ಮುಂದಿನ ಹಂತದಲ್ಲಿ 35 ಯೂನಿಟ್‌ಗಳ ಬಫರ್ ಇದೆ (3.5 ಗಂಟೆಗಳ ಕಾಲ ಕೆಲಸ ನಿಲ್ಲುವುದಿಲ್ಲ).",
        "phase3_title": "3. ಯೋಜನೆ (GENERATE)",
        "phase3_desc": "7 ಯೂನಿಟ್‌ಗಳನ್ನು ಸೆಲ್ವಿ (4) ಮತ್ತು ಲಕ್ಷ್ಮಿಗೆ (3) ವರ್ಗಾಯಿಸುವ ಪ್ರಸ್ತಾಪ.",
        "phase4_title": "4. ಮೌಲ್ಯಮಾಪನ (EVALUATE)",
        "phase4_desc": "ಸೆಲ್ವಿಯ ಹೆಚ್ಚುವರಿ ಸಾಮರ್ಥ್ಯ 50.1; ಲಕ್ಷ್ಮಿಯ ಹೆಚ್ಚುವರಿ ಸಾಮರ್ಥ್ಯ 42.8 (ನಿಯಮದ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆ).",
        "phase5_title": "5. ವಿವರಣೆ (EXPLAIN)",
        "phase5_desc": "ಕನ್ನಡ ಧ್ವನಿ ವಿವರಣೆ: 'ಗೀತಾ ಅವರ ಬದಲಿಗೆ ಸೆಲ್ವಿ (4) ಮತ್ತು ಲಕ್ಷ್ಮಿ (3) ಹೆಚ್ಚುವರಿ ಕೆಲಸ ಸ್ವೀಕರಿಸಲು ಒಪ್ಪಿದ್ದಾರೆ...'",
        "phase6_title": "6. ಸಮ್ಮತಿ ಗೇಟ್ (GOVERNANCE GATE)",
        "phase6_desc": "ಕಾರ್ಯ ಸ್ಥಗಿತ! ಬಲವಂತವಿಲ್ಲದೆ ಸದಸ್ಯರ ಸ್ವಯಂಪ್ರೇರಿತ ಒಪ್ಪಿಗೆ ಅತ್ಯಗತ್ಯ.",
        "phase7_title": "7. ಸಮರ್ಪಣೆ (COMMIT)",
        "phase7_desc": "ಬದಲಾಯಿಸಲಾಗದ ಲೆಡ್ಜರ್‌ನಲ್ಲಿ ದಾಖಲಿಸಲಾಗಿದೆ. ಹೊಸ ನ್ಯಾಯಸಮ್ಮತ ಸೂಚ್ಯಂಕ: J = 0.9841.",
        "bom_explainer": "💡 ಇದರ ಪಾತ್ರವೇನು? ಬಟ್ಟೆ ಪೋಲಾಗುವುದು ಮತ್ತು ಯಂತ್ರ ಸವೆತವನ್ನು ಲೆಕ್ಕಿಸದೆ ಮಹಿಳೆಯರು 30-40% ಕಡಿಮೆ ಬೆಲೆಗೆ ಕೆಲಸ ಮಾಡುತ್ತಾರೆ. ಖರೀದಿದಾರರ ಆಫರ್ ಲಾಭದಾಯಕವೇ ಅಥವಾ ನಷ್ಟವೇ ಎಂದು 3 ಹಂತಗಳಲ್ಲಿ ಪರಿಶೀಲಿಸಲು ಇದು ನೆರವಾಗುತ್ತದೆ.",
        "buyer_offer_label": "ಖರೀದಿದಾರರ ಬೆಲೆ ಆಫರ್ ಪರೀಕ್ಷಿಸಿ (₹):",
        "vs_operating_floor": "1. ಬ್ರೇಕ್-ಈವನ್ ವೆಚ್ಚ (₹260.55)",
        "vs_cost_plus": "2. 12% ಉಳಿತಾಯ ನಿಧಿಯೊಂದಿಗೆ (₹291.82)",
        "vs_enterprise_margin": "3. 10% ಉದ್ಯಮ ಲಾಭಾಂಶದೊಂದಿಗೆ (₹324.24)",
        "predatory_alert": "⚠️ ಕಡಿಮೆ ಬೆಲೆಯ ಎಚ್ಚರಿಕೆ: ಖರೀದಿದಾರರ ₹{offer}.00 ಆಫರ್ ಮೂಲ ಉತ್ಪಾದನಾ ವೆಚ್ಚಕ್ಕಿಂತ ₹{deficit}/ಯೂನಿಟ್ ಕಡಿಮೆಯಾಗಿದೆ. ಇದನ್ನು ಒಪ್ಪಿಕೊಂಡರೆ ₹{loss:,} ನಷ್ಟವಾಗುತ್ತದೆ!",
        "bom_title": "ಘಟಕ ಆರ್ಥಿಕತೆಯ ವೆಚ್ಚ ವಿವರ (500 ಸಮವಸ್ತ್ರಗಳು)",
        "cv_title": "🔍 ಕಂಪ್ಯೂಟರ್ ದೃಷ್ಟಿ ಸಹಾಯಕ ಗುಣಮಟ್ಟ ತಪಾಸಣೆ",
        "cv_desc": "ಕಾರ್ಯಾಚರಣೆಯ ಮಿತಿ: ಕಂಪ್ಯೂಟರ್ ದೃಷ್ಟಿಯು ಕೇವಲ ಮಸುಕು ಮತ್ತು ಹೊಲಿಗೆ ವಕ್ರತೆಯನ್ನು ಮಾತ್ರ ಸೂಚಿಸುತ್ತದೆ. ಅಂತಿಮ ನಿರ್ಧಾರವನ್ನು ನಾಯಕಿಯೇ ತೆಗೆದುಕೊಳ್ಳುತ್ತಾರೆ.",
        "cv_sample_prompt": "ಪರಿಶೀಲನೆಗಾಗಿ ವಾಸ್ತವಿಕ ಸಮವಸ್ತ್ರ ಚಿತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "cv_sample1": "ಮಾದರಿ 1: ✅ ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಸಮವಸ್ತ್ರ (ಸರಿಯಾದ ಪ್ಲ್ಯಾಕೆಟ್ ಹೊಲಿಗೆ)",
        "cv_sample2": "ಮಾದರಿ 2: ⚠️ ಮಸುಕಾದ ಫೋಟೋ (Laplacian Var < 55)",
        "cv_sample3": "ಮಾದರಿ 3: ❌ ವಕ್ರವಾದ ಪ್ಲ್ಯಾಕೆಟ್ ಹೊಲಿಗೆ (Angle > 3.5°)",
        "cv_or_upload": "ಅಥವಾ ನೈಜ ಸಮವಸ್ತ್ರ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ:",
        "cv_original": "ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿರುವ ಸಮವಸ್ತ್ರ ಚಿತ್ರ:",
        "cv_overlay": "OpenCV ಹೊಲಿಗೆ ರೇಖೆಯ ವಿಶ್ಲೇಷಣೆ:",
        "cv_diagnostics": "ಪರಿಶೀಲನಾ ಫಲಿತಾಂಶಗಳು",
        "blur_var_label": "ಮಸುಕು ವ್ಯತ್ಯಾಸ (Laplacian Variance)",
        "angle_dev_label": "ಪ್ಲ್ಯಾಕೆಟ್ ಹೊಲಿಗೆ ಕೋನ ವಿಚಲನೆ",
        "human_decision": "ನಾಯಕಿಯ ಅಂತಿಮ ನಿರ್ಧಾರ:",
        "btn_accept": "✅ ಸ್ವೀಕರಿಸಿ (Accept)",
        "btn_rework": "⚠️ ಮರುಕೆಲಸ (Rework)",
        "btn_reject": "❌ ತಿರಸ್ಕರಿಸಿ (Reject)",
        "payroll_title": "🗳️ ಪ್ರಜಾಸತ್ತಾತ್ಮಕ ವೇತನ ಅನುಮೋದನೆ ಮತ್ತು ಕೋರಂ",
        "payroll_desc": "ಪ್ರಜಾಸತ್ತಾತ್ಮಕ ಕೋರಂ ಗೇಟ್: ವೇತನ ಪಟ್ಟಿಯನ್ನು ಬದಲಾಯಿಸಲಾಗದ SHA-256 ಸ್ನ್ಯಾಪ್‌ಶಾಟ್‌ನಲ್ಲಿ ಲಾಕ್ ಮಾಡಲಾಗಿದೆ. ನಾಯಕಿಯ ಸಹಿ ಮತ್ತು 66.7% ಸದಸ್ಯರ ಮತಗಳು ಅಗತ್ಯವಿದೆ.",
        "quorum_progress_label": "ಸದಸ್ಯರ ಸಮ್ಮತಿಯ ಕೋರಂ ಪ್ರಗತಿ:",
        "quorum_met": "✅ ಕೋರಂ ಪೂರ್ಣಗೊಂಡಿದೆ (≥ 66.7%): ವೇತನ ಪಟ್ಟಿಯು ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆಗೆ ಸಿದ್ಧವಾಗಿದೆ!",
        "quorum_pending": "⏳ ಅನುಮೋದನೆ ಬಾಕಿಯಿದೆ: ಇನ್ನೂ {needed} ಮತಗಳು ಬೇಕಾಗಿವೆ.",
        "btn_cast_votes": "🗳️ ಬಾಕಿ ಇರುವ ಸದಸ್ಯರ ಪರವಾಗಿ ಮತ ಚಲಾಯಿಸಿ",
        "btn_sign_disburse": "✍️ ನಾಯಕಿ ಸಹಿ ಮಾಡಿ ಬ್ಯಾಂಕ್‌ಗೆ ರವಾನಿಸಿ",
        "passport_title": "📄 B2B ಆದೇಶ ಪಾಸ್‌ಪೋರ್ಟ್ (Order Passport)",
        "passport_desc": "ಖರೀದಿದಾರರಿಗೆ ನ್ಯಾಯಯುತ ವೇತನ ಮತ್ತು ಉತ್ಪಾದನಾ ಪಾರದರ್ಶಕತೆಯನ್ನು ದೃಢೀಕರಿಸುವ ಅಧಿಕೃತ ವರದಿ.",
        "btn_download_passport": "📥 ಅಧಿಕೃತ ಆದೇಶ ಪಾಸ್‌ಪೋರ್ಟ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        # Member View Translations
        "member_greeting": "ನಮಸ್ಕಾರ {name}!",
        "member_workspace_sub": "ಸದಸ್ಯೆಯ ಕಾರ್ಯಸ್ಥಳ • {stage} • ಯಂತ್ರ: {machine}",
        "my_work_today_title": "1. 🟢 ನನ್ನ ಇಂದಿನ ಕೆಲಸ",
        "today_target_badge": "ಇಂದಿನ ಗುರಿ (TARGET)",
        "shirts_unit": "ಸಮವಸ್ತ್ರಗಳು",
        "piece_rate_label": "ದರ: ₹{rate} / ಸಮವಸ್ತ್ರ",
        "completed_submission_title": "2. 📸 ಕೆಲಸ ಮುಗಿದಿದೆ - ಸಲ್ಲಿಸಿ",
        "completed_units_label": "ಇಂದು ಮುಗಿಸಿದ ಸಂಖ್ಯೆ:",
        "offline_toggle_label": "✈️ ಆಫ್‌ಲೈನ್ ಮೋಡ್ (ಇಂಟರ್ನೆಟ್ ಇಲ್ಲ)",
        "submit_work_btn": "📤 ಕೆಲಸವನ್ನು ದಾಖಲಿಸಿ",
        "saved_offline_msg": "🟡 ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ದಾಖಲಿಸಲಾಗಿದೆ: {qty} ಸಮವಸ್ತ್ರಗಳು ನಮೂದಾಗಿವೆ. ಇಂಟರ್ನೆಟ್ ಬಂದಾಗ ಸರ್ವರ್‌ಗೆ ಸೇರುತ್ತದೆ!",
        "synced_online_msg": "✅ ಯಶಸ್ವಿಯಾಗಿ ದಾಖಲಾಗಿದೆ! {qty} ಸಮವಸ್ತ್ರಗಳು ನಿಮ್ಮ ಲೆಕ್ಕಕ್ಕೆ ಸೇರಿವೆ. ರಸೀದಿ: REC-{ts}",
        "network_restored_msg": "📶 ಇಂಟರ್ನೆಟ್ ಮರುಸ್ಥಾಪನೆಗೊಂಡಿದೆ! {count} ಆಫ್‌ಲೈನ್ ನಮೂದುಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನವೀಕರಿಸಲಾಗುತ್ತಿದೆ...",
        "upload_garment_photo": "ಮುಗಿಸಿದ ಸಮವಸ್ತ್ರದ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ:",
        "take_camera_photo": "ಅಥವಾ ಮೊಬೈಲ್ ಕ್ಯಾಮೆರಾ ಬಳಸಿ ಫೋಟೋ ತೆಗೆಯಿರಿ:",
        "photo_pass_msg": "🟢 ಫೋಟೋ ಸ್ಪಷ್ಟವಾಗಿದೆ (Laplacian: {val} > 55.0) — ಸಲ್ಲಿಸಲು ಸಿದ್ಧ!",
        "photo_blur_fail_msg": "🔴 ಫೋಟೋ ತುಂಬಾ ಮಸುಕಾಗಿದೆ (Laplacian: {val} < 55.0) — ಉತ್ತಮ ಬೆಳಕಿನಲ್ಲಿ ಮತ್ತೆ ತೆಗೆಯಿರಿ!",
        "hear_earnings_title": "3. 🔊 ನನ್ನ ಗಳಿಕೆ ಆಲಿಸಿ (ಧ್ವನಿ ಪಾಸ್‌ಬುಕ್)",
        "gross_label": "ಒಟ್ಟು ಗಳಿಕೆ",
        "advance_label": "ಮುಂಗಡ ಕಡಿತ",
        "net_payable_label": "ಬ್ಯಾಂಕ್‌ಗೆ ಜಮೆಯಾಗುವ ಮೊತ್ತ",
        "awaiting_quorum_badge": "⏳ ಗುಂಪಿನ ಅನುಮೋದನೆಗೆ ಕಾಯುತ್ತಿದೆ",
        "audio_btn_text": "🔊 ನನ್ನ ಖಾತೆಯನ್ನು ಕನ್ನಡದಲ್ಲಿ ಕೇಳಿ (Listen in Kannada)",
        "dispute_btn_text": "⚠️ ತಪ್ಪಾದ ನಮೂದು - ಆಕ್ಷೇಪಿಸಿ (Dispute)",
        "dispute_raised_msg": "⚠️ ಆಕ್ಷೇಪಣೆ ದಾಖಲಾಗಿದೆ. ಆಕ್ಷೇಪಿಸಲಾದ ಮೊತ್ತವನ್ನು ಮಾತ್ರ ತಡೆಹಿಡಿಯಲಾಗಿದ್ದು, ಉಳಿದ ವೇತನ ಸುರಕ್ಷಿತವಾಗಿದೆ!",
        "withdraw_dispute_btn": "✅ ಆಕ್ಷೇಪಣೆ ಹಿಂಪಡೆಯಿರಿ",
        "quorum_vote_title": "4. 🗳️ ವೇತನ ಅನುಮೋದನೆಗೆ ನಿಮ್ಮ ಮತ",
        "vote_approve_btn": "👍 ನಾನು ಈ ವೇತನ ಪಟ್ಟಿಯನ್ನು ಒಪ್ಪುತ್ತೇನೆ",
        "vote_object_btn": "❌ ನನಗೆ ಆಕ್ಷೇಪಣೆಯಿದೆ",
        "vote_cast_toast": "ನಿಮ್ಮ ಮತ ಯಶಸ್ವಿಯಾಗಿ ದಾಖಲಾಗಿದೆ!",
        "current_vote_caption": "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಮತ: {status} • ಗುಂಪಿನ ನಿಯಮಗಳಿಗೆ ಒಳಪಟ್ಟಿದೆ."
    },
    "hi": {
        "lang_tag": "hi-IN",
        "app_title": "सहकारी AI (SAHAKARI AI)",
        "app_subtitle": "महिला स्वयं सहायता समूहों के लिए पारदर्शी उत्पादन और सूक्ष्म-वेतन प्रणाली",
        "challenge_badge": "PS 8.1 • The JanAI Mass Entrepreneurship Challenge • Tech4Bharat 2026",
        "login_box_title": "🔑 भाषा, भूमिका और प्रोफ़ाइल चुनें",
        "select_lang": "भाषा चुनें:",
        "select_access": "अपनी भूमिका चुनें:",
        "role_leader": "👑 SHG समूह लीडर (Leader)",
        "role_artisan": "🧵 SHG सदस्य / कारीगर (Artisan)",
        "select_leader_name": "लीडर का नाम चुनें:",
        "select_artisan_name": "कारीगर का नाम चुनें:",
        "security_pin": "4-अंकों का सुरक्षा पिन (PIN):",
        "launch_btn": "🚀 कार्यस्थल शुरू करें",
        "demo_pin_hint": "💡 डेमो पिन: 1234 • क्षेत्रीय ऑडियो पासबुक सुविधा के साथ",
        "switch_profile": "🚪 प्रोफ़ाइल बदलें / बाहर निकलें",
        "leader_view_badge": "👑 लीडर दृश्य (LEADER)",
        "artisan_view_badge": "🧵 कारीगर दृश्य (ARTISAN)",
        "active_bulk_order": "सक्रिय थोक आर्डर",
        "stage_b_throughput": "सिलाई विभाग उत्पादन (Stage B)",
        "jains_index": "जैन निष्पक्षता सूचकांक (Jain's Index)",
        "enterprise_quote": "लक्षित व्यावसायिक उद्धरण",
        "proven_fair": "लक्ष्य ≥ 0.9500 (सिद्ध निष्पक्षता)",
        "tab1": "📊 1. उत्पादन पाइपलाइन और आवंटन",
        "tab2": "⚡ 2. स्वायत्त पुनर्संतुलन (Day 4 Crisis)",
        "tab3": "💰 3. लागत और मूल्य निर्धारण (BOM)",
        "tab4": "🔍 4. कंप्यूटर विज़न गुणवत्ता जांच",
        "tab5": "🗳️ 5. पेरोल अनुमोदन और कोरम मतदान",
        "tab6": "📄 6. खरीदार आर्डर पासपोर्ट",
        "pipeline_overview_title": "🏭 3-चरणीय संरक्षित उत्पादन पाइपलाइन",
        "stage_a_title": "✂️ चरण A: कटिंग और किट बनाना (2 सदस्य)",
        "stage_b_title": "🧵 चरण B: शर्ट सिलाई (8 सदस्य • मुख्य चरण)",
        "stage_c_title": "🏷️ चरण C: फिनिशिंग और पैकिंग (2 सदस्य)",
        "morning_rollcall_title": "🌅 सुबह की हाजिरी और मशीन उपलब्धता (Morning Roll-Call)",
        "morning_rollcall_desc": "सुबह लीडर दर्ज करती हैं कि कौन उपस्थित है और मशीन चालू है। दैनिक लक्ष्य स्वतः पुनर्गणित होते हैं।",
        "btn_save_rollcall": "💾 आज की हाजिरी सहेजें और कोटा पुनर्गणित करें",
        "rollcall_saved_toast": "हाजिरी सहेजी गई! आज की समूह क्षमता: {cap} यूनिट/दिन। जैन सूचकांक: {jain}",
        "table_title": "📋 12 सदस्यों की दैनिक क्षमता और कार्य आवंटन तालिका",
        "jains_note": "💡 जैन निष्पक्षता सूचकांक: {val} (मशीन की गति और घरेलू समय के आधार पर काम के निष्पक्ष वितरण का गणितीय प्रमाण)।",
        "day4_crisis_title": "⚡ 7-चरणीय विलंब पुनर्प्राप्ति स्वायत्त एजेंट",
        "day4_explainer": "💡 इसकी क्या भूमिका है? यह स्वचालित आपातकालीन सहायक है। चौथे दिन जब किसी महिला की तबीयत खराब होती है, तो सामान्य समूहों में डिलीवरी के दिन तक पता नहीं चलता और आर्डर रद्द हो जाता है। यह एजेंट तुरंत कमी को भांपकर खाली समय वाली महिलाओं से सहमति लेकर काम का पुनर्वितरण करता है।",
        "day4_crisis_desc": "परिचालन घटना: चौथे दिन सदस्य गीता शंकर (M06) पारिवारिक बीमारी के कारण 7 शर्ट नहीं बना पाईं। एजेंट सहमति से काम का पुनर्वितरण करता है।",
        "sim_emergency_btn": "🚨 चौथे दिन की आपात स्थिति का अनुकरण करें (M06 Shortfall)",
        "agent_generate_btn": "🧠 एजेंट: अतिरिक्त क्षमता खोजें और प्रस्ताव बनाएं",
        "obtain_consent_btn": "🤝 सदस्यों की सहमति प्राप्त करें (सेल्वी और लक्ष्मी की सहमति)",
        "commit_rebalance_btn": "💾 लीडर: अनुमोदन करें और लेजर में सहेजें",
        "reset_sim_btn": "🔄 अनुकरण रीसेट करें (Reset)",
        "phase1_title": "1. पहचान (DETECT)",
        "phase1_desc": "चौथे दिन की कमी: सदस्य M06 बीमारी के कारण 7 यूनिट पूरा नहीं कर सकीं।",
        "phase2_title": "2. जांच (INVESTIGATE)",
        "phase2_desc": "अगले चरण में 35 यूनिट का बफर उपलब्ध है (3.5 घंटे तक काम नहीं रुकेगा)।",
        "phase3_title": "3. प्रस्ताव (GENERATE)",
        "phase3_desc": "7 यूनिट को सेल्वी (4) और लक्ष्मी (3) को हस्तांतरित करने का प्रस्ताव।",
        "phase4_title": "4. गणितीय मूल्यांकन (EVALUATE)",
        "phase4_desc": "सेल्वी का स्पेयर बफर 50.1; लक्ष्मी का स्पेयर बफर 42.8 (सुरक्षित सीमा में)।",
        "phase5_title": "5. स्पष्टीकरण (EXPLAIN)",
        "phase5_desc": "ऑडियो स्पष्टीकरण: 'गीता जी के स्थान पर सेल्वी (4) और लक्ष्मी (3) अतिरिक्त कार्य स्वीकार करने के लिए सहमत...'",
        "phase6_title": "6. सहमति द्वार (GOVERNANCE GATE)",
        "phase6_desc": "कार्य रुकता है! बिना जबरदस्ती के सदस्यों की स्वैच्छिक सहमति अनिवार्य है।",
        "phase7_title": "7. प्रतिबद्धता (COMMIT)",
        "phase7_desc": "अपरिवर्तनीय लेजर में दर्ज किया गया। नया निष्पक्षता सूचकांक: J = 0.9841।",
        "bom_explainer": "💡 इसकी क्या भूमिका है? कपड़ा बर्बादी, मशीन मरम्मत आदि को न जोड़ने से महिलाएं 30-40% कम कीमत पर काम करती हैं। खरीदार के प्रस्ताव का 3 स्तरों पर परीक्षण कर यह टूल नुकसान को रोकता है।",
        "buyer_offer_label": "खरीदार के मूल्य प्रस्ताव का परीक्षण करें (₹):",
        "vs_operating_floor": "1. ब्रेक-ईवन मूल लागत (₹260.55)",
        "vs_cost_plus": "2. 12% बचत कोष के साथ (₹291.82)",
        "vs_enterprise_margin": "3. 10% उद्यम लाभ के साथ (₹324.24)",
        "predatory_alert": "⚠️ कम मूल्य चेतावनी: खरीदार का ₹{offer}.00 का प्रस्ताव मूल उत्पादन लागत से ₹{deficit}/यूनिट कम है। इसे स्वीकार करने पर ₹{loss:,} का नुकसान होगा!",
        "bom_title": "इकाई अर्थशास्त्र लागत विवरण (500 यूनिफॉर्म)",
        "cv_title": "🔍 सहायक कंप्यूटर विज़न गुणवत्ता जांच",
        "cv_desc": "परिचालन सीमा: कंप्यूटर विज़न केवल धुंधलेपन और सिलाई के टेढ़ेपन को इंगित करता है। अंतिम निर्णय मानवीय लीडर द्वारा ही लिया जाएगा।",
        "cv_sample_prompt": "निरीक्षण के लिए वास्तविक यूनिफॉर्म शर्ट का नमूना चुनें:",
        "cv_sample1": "नमूना 1: ✅ उच्च गुणवत्ता वाली यूनिफॉर्म शर्ट (सीधी सिलाई)",
        "cv_sample2": "नमूना 2: ⚠️ धुंधली तस्वीर (Laplacian Var < 55)",
        "cv_sample3": "नमूना 3: ❌ टेढ़ी सिलाई वाली शर्ट (Angle > 3.5°)",
        "cv_or_upload": "या वास्तविक वस्त्र की तस्वीर अपलोड करें:",
        "cv_original": "जांच हेतु शर्ट का चित्र:",
        "cv_overlay": "OpenCV सिलाई रेखा विश्लेषण:",
        "cv_diagnostics": "निरीक्षण परिणाम",
        "blur_var_label": "धुंधलापन भिन्नता (Laplacian Variance)",
        "angle_dev_label": "सिलाई कोण विचलन",
        "human_decision": "लीडर का अंतिम निर्णय:",
        "btn_accept": "✅ स्वीकार करें (Accept)",
        "btn_rework": "⚠️ सुधार करें (Rework)",
        "btn_reject": "❌ अस्वीकार करें (Reject)",
        "payroll_title": "🗳️ लोकतांत्रिक पेरोल अनुमोदन और कोरम",
        "payroll_desc": "लोकतांत्रिक कोरम द्वार: पेरोल को अपरिवर्तनीय SHA-256 स्नैपशॉट में लॉक किया गया है। अंतिम मंजूरी के लिए लीडर के हस्ताक्षर और 66.7% सदस्यों के वोट आवश्यक हैं।",
        "quorum_progress_label": "सदस्य सहमति कोरम प्रगति:",
        "quorum_met": "✅ कोरम पूरा हुआ (≥ 66.7%): पेरोल बैंक भुगतान के लिए तैयार है!",
        "quorum_pending": "⏳ अनुमोदन लंबित: दो-तिहाई बहुमत के लिए {needed} और वोटों की आवश्यकता है।",
        "btn_cast_votes": "🗳️ शेष सदस्यों के लिए सकारात्मक वोट डालें",
        "btn_sign_disburse": "✍️ लीडर हस्ताक्षर करें और बैंक को भेजें",
        "passport_title": "📄 B2B आर्डर पासपोर्ट (Order Passport)",
        "passport_desc": "संस्थागत खरीदारों के लिए उचित मजदूरी और आपूर्ति श्रृंखला की पारदर्शिता प्रमाणित करने वाला आधिकारिक दस्तावेज।",
        "btn_download_passport": "📥 आधिकारिक आर्डर पासपोर्ट डाउनलोड करें",
        # Member View Translations
        "member_greeting": "नमस्ते {name}!",
        "member_workspace_sub": "सदस्य कार्यस्थल • {stage} • मशीन: {machine}",
        "my_work_today_title": "1. 🟢 मेरा आज का काम",
        "today_target_badge": "आज का लक्ष्य (TARGET)",
        "shirts_unit": "शर्ट्स",
        "piece_rate_label": "दर: ₹{rate} / शर्ट",
        "completed_submission_title": "2. 📸 काम पूरा हुआ - जमा करें",
        "completed_units_label": "आज पूरी की गई संख्या:",
        "offline_toggle_label": "✈️ ऑफलाइन मोड (इंटरनेट नहीं है)",
        "submit_work_btn": "📤 पूरा काम जमा करें",
        "saved_offline_msg": "🟡 ऑफलाइन सुरक्षित रूप से सहेजा गया: {qty} शर्ट दर्ज हैं। इंटरनेट आने पर अपने आप सर्वर से जुड़ जाएगा!",
        "synced_online_msg": "✅ सफलतापूर्वक दर्ज हुआ! {qty} शर्ट आपके खाते में जुड़ गए। रसीद: REC-{ts}",
        "network_restored_msg": "📶 इंटरनेट पुनः जुड़ गया! {count} ऑफलाइन प्रविष्टियां स्वचालित रूप से सिंक हो रही हैं...",
        "upload_garment_photo": "तैयार वस्त्र की तस्वीर अपलोड करें:",
        "take_camera_photo": "या कैमरे से तस्वीर लें:",
        "photo_pass_msg": "🟢 तस्वीर साफ और स्पष्ट है (Laplacian: {val} > 55.0) — जमा करने के लिए तैयार!",
        "photo_blur_fail_msg": "🔴 तस्वीर बहुत धुंधली है (Laplacian: {val} < 55.0) — कृपया अच्छी रोशनी में दोबारा फोटो लें!",
        "hear_earnings_title": "3. 🔊 मेरी कमाई सुनें (ऑडियो पासबुक)",
        "gross_label": "कुल सकल कमाई",
        "advance_label": "अग्रिम कटौती",
        "net_payable_label": "बैंक खाते में शुद्ध देय राशि",
        "awaiting_quorum_badge": "⏳ समूह अनुमोदन की प्रतीक्षा में",
        "audio_btn_text": "🔊 अपना खाता हिंदी में सुनें (Listen in Hindi)",
        "dispute_btn_text": "⚠️ गलत प्रविष्टि - आपत्ति दर्ज करें (Dispute)",
        "dispute_raised_msg": "⚠️ आपत्ति दर्ज की गई है। विवादित राशि को रोककर बाकी कमाई सुरक्षित रखी गई है!",
        "withdraw_dispute_btn": "✅ आपत्ति वापस लें",
        "quorum_vote_title": "4. 🗳️ समूह पेरोल पर अपना वोट डालें",
        "vote_approve_btn": "👍 मैं इस पेरोल को स्वीकार करती हूँ",
        "vote_object_btn": "❌ मुझे आपत्ति है",
        "vote_cast_toast": "आपका वोट सफलतापूर्वक दर्ज हो गया!",
        "current_vote_caption": "आपकी वर्तमान वोट स्थिति: {status} • समूह के नियमों के अधीन।"
    }
}

def t(key, **kwargs):
    """Retrieves translated text string for the current active language."""
    lang = st.session_state.get("lang", "en")
    text_template = TRANSLATIONS.get(lang, {}).get(key, TRANSLATIONS["en"].get(key, key))
    if kwargs:
        try:
            return text_template.format(**kwargs)
        except Exception:
            return text_template
    return text_template


# -----------------------------------------------------------------------------
# 3. SEED DATA & INITIALIZATION
# -----------------------------------------------------------------------------
MEMBERS_DATA = [
    {
        "id": "M01", "name": "Karpagam V.",
        "names_by_lang": {"en": "Karpagam V.", "ta": "கற்பகம் வி.", "kn": "ಕರ್ಪಗಂ ವಿ.", "hi": "कर्पगम वी."},
        "role": "Cluster Leader", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Motorized Industrial Juki", "hours": 6.0, "mult": 1.45, "defect": 0.012,
        "daily_cap": 15.48, "allocated": 59, "done": 24, "wage_rate": 45.0, "advance": 0.0,
        "disputed": False, "is_leader": True
    },
    {
        "id": "M02", "name": "Lakshmi Devi R.",
        "names_by_lang": {"en": "Lakshmi Devi R.", "ta": "லட்சுமி தேவி ஆர்.", "kn": "ಲಕ್ಷ್ಮೀ ದೇವಿ ಆರ್.", "hi": "लक्ष्मी देवी आर."},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Motorized Domestic Sewing", "hours": 5.0, "mult": 1.30, "defect": 0.020,
        "daily_cap": 11.47, "allocated": 44, "done": 18, "wage_rate": 45.0, "advance": 200.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M03", "name": "Selvi M.",
        "names_by_lang": {"en": "Selvi M.", "ta": "செல்வி எம்.", "kn": "ಸೆಲ್ವಿ ಎಂ.", "hi": "सेल्वी एम."},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Motorized Domestic Sewing", "hours": 6.0, "mult": 1.30, "defect": 0.025,
        "daily_cap": 13.69, "allocated": 53, "done": 21, "wage_rate": 45.0, "advance": 150.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M04", "name": "Radha Bai S.",
        "names_by_lang": {"en": "Radha Bai S.", "ta": "ராதா பாய் எஸ்.", "kn": "ರಾಧಾ ಬಾಯಿ ಎಸ್.", "hi": "राधा बाई एस."},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Manual Foot Pedal Sewing", "hours": 4.0, "mult": 0.95, "defect": 0.030,
        "daily_cap": 6.63, "allocated": 25, "done": 10, "wage_rate": 45.0, "advance": 100.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M05", "name": "Meena Kumari T.",
        "names_by_lang": {"en": "Meena Kumari T.", "ta": "மீனா குமாரி டி.", "kn": "ಮೀನಾ ಕುಮಾರಿ ಟಿ.", "hi": "मीना कुमारी टी."},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Motorized Domestic Sewing", "hours": 5.0, "mult": 1.30, "defect": 0.020,
        "daily_cap": 11.47, "allocated": 44, "done": 18, "wage_rate": 45.0, "advance": 200.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M06", "name": "Geetha Shankar",
        "names_by_lang": {"en": "Geetha Shankar", "ta": "கீதா சங்கர்", "kn": "ಗೀತಾ ಶಂಕರ್", "hi": "गीता शंकर"},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Manual Foot Pedal Sewing", "hours": 3.0, "mult": 0.95, "defect": 0.035,
        "daily_cap": 4.95, "allocated": 18, "done": 0, "wage_rate": 45.0, "advance": 0.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M07", "name": "Vasanthi P.",
        "names_by_lang": {"en": "Vasanthi P.", "ta": "வசந்தி பி.", "kn": "ವಸಂತಿ ಪಿ.", "hi": "वसंती पी."},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Manual Foot Pedal Sewing", "hours": 4.0, "mult": 0.95, "defect": 0.025,
        "daily_cap": 6.67, "allocated": 25, "done": 10, "wage_rate": 45.0, "advance": 100.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M08", "name": "Anbukarasi K.",
        "names_by_lang": {"en": "Anbukarasi K.", "ta": "அன்புகரசி கே.", "kn": "ಅನ್ಬುಕರಸಿ ಕೆ.", "hi": "अंबुकरसी के."},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Motorized Domestic Sewing", "hours": 5.0, "mult": 1.30, "defect": 0.025,
        "daily_cap": 11.41, "allocated": 43, "done": 17, "wage_rate": 45.0, "advance": 150.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M09", "name": "Bhavani S.",
        "names_by_lang": {"en": "Bhavani S.", "ta": "பவானி எஸ்.", "kn": "ಭವಾನಿ ಎಸ್.", "hi": "भवानी एस."},
        "role": "Artisan", "stage": "Stage C: Finishing/Trims", "stage_code": "C",
        "machine": "Buttonholer & Steam Desk", "hours": 6.0, "mult": 1.50, "defect": 0.010,
        "daily_cap": 30.00, "allocated": 250, "done": 105, "wage_rate": 8.5, "advance": 200.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M10", "name": "Mallika N.",
        "names_by_lang": {"en": "Mallika N.", "ta": "மல்லிகா என்.", "kn": "ಮಲ್ಲಿಕಾ ಎನ್.", "hi": "मल्लिका एन."},
        "role": "Assistant Leader", "stage": "Stage A: Cutting", "stage_code": "A",
        "machine": "Heavy Tailoring Shears", "hours": 4.0, "mult": 1.20, "defect": 0.015,
        "daily_cap": 29.55, "allocated": 250, "done": 250, "wage_rate": 8.0, "advance": 500.0,
        "disputed": False, "is_leader": True
    },
    {
        "id": "M11", "name": "Shanthi R.",
        "names_by_lang": {"en": "Shanthi R.", "ta": "சாந்தி ஆர்.", "kn": "ಶಾಂತಿ ಆರ್.", "hi": "शांति आर."},
        "role": "Artisan", "stage": "Stage B: Sewing", "stage_code": "B",
        "machine": "Motorized Domestic Sewing", "hours": 5.0, "mult": 1.30, "defect": 0.020,
        "daily_cap": 11.47, "allocated": 44, "done": 18, "wage_rate": 45.0, "advance": 150.0,
        "disputed": False, "is_leader": False
    },
    {
        "id": "M12", "name": "Kamala V.",
        "names_by_lang": {"en": "Kamala V.", "ta": "கமலா வி.", "kn": "ಕಮಲಾ ವಿ.", "hi": "कमला वी."},
        "role": "Treasurer & QC Lead", "stage": "Stage C: Inspection & Pack", "stage_code": "C",
        "machine": "Inspection Table & Bagger", "hours": 6.0, "mult": 1.50, "defect": 0.010,
        "daily_cap": 30.00, "allocated": 250, "done": 105, "wage_rate": 8.5, "advance": 200.0,
        "disputed": False, "is_leader": True
    }
]

if "lang" not in st.session_state:
    st.session_state.lang = "en"

if "members" not in st.session_state:
    st.session_state.members = MEMBERS_DATA

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_id = None
    st.session_state.user_name = None

if "rebalance_state" not in st.session_state:
    st.session_state.rebalance_state = "IDLE"

if "offline_outbox" not in st.session_state:
    st.session_state.offline_outbox = []

if "quorum_votes" not in st.session_state:
    st.session_state.quorum_votes = {m["id"]: "PENDING" for m in MEMBERS_DATA}
    for mid in ["M01", "M05", "M07", "M08", "M10", "M12"]:
        st.session_state.quorum_votes[mid] = "APPROVED"


# -----------------------------------------------------------------------------
# 4. HELPER FUNCTIONS: JAIN'S FAIRNESS & REALISTIC CV GENERATION
# -----------------------------------------------------------------------------
def calculate_jains_fairness(members_list):
    """Calculates Jain's Fairness Index on normalized member utilization across sewing artisans."""
    utilizations = []
    for m in members_list:
        if m.get("stage_code") == "B" or "Sewing" in m.get("stage", ""):
            max_10d_cap = m["daily_cap"] * 10
            util = m["allocated"] / max_10d_cap if max_10d_cap > 0 else 0
            utilizations.append(util)
    
    if not utilizations:
        return 1.0
    sum_u = sum(utilizations)
    sum_sq_u = sum(u ** 2 for u in utilizations)
    n = len(utilizations)
    jain = (sum_u ** 2) / (n * sum_sq_u)
    return round(jain, 4)

def generate_realistic_shirt_image(condition="valid"):
    """
    Renders an authentic, realistic school uniform shirt with folded collar,
    inner neckband, chest pocket, textured margins, and pearlescent buttons
    on a precision dark-slate optical inspection cutting surface.
    """
    width, height = 400, 480
    base = Image.new("RGB", (width, height), (21, 29, 46))
    draw = ImageDraw.Draw(base)
    
    # Inspection table background precision grid
    for gx in range(40, width, 40):
        draw.line([(gx, 0), (gx, height)], fill=(28, 38, 58), width=1)
    for gy in range(40, height, 40):
        draw.line([(0, gy), (width, gy)], fill=(28, 38, 58), width=1)
    draw.rectangle([(2, 2), (width - 3, height - 3)], outline=(51, 65, 85), width=2)
    
    # Classic Indian School Uniform Sky-Blue Palette
    shirt_color = (130, 175, 215)
    shadow_color = (100, 145, 185)
    line_color = (80, 120, 160)
    placket_color = (138, 182, 222)
    
    # Shirt Torso Silhouette
    torso = [(110, 80), (290, 80), (370, 140), (340, 460), (60, 460), (30, 140)]
    draw.polygon(torso, fill=shirt_color, outline=line_color)
    
    # Armhole Shadow Seams
    draw.line([(110, 80), (90, 170)], fill=shadow_color, width=2)
    draw.line([(290, 80), (310, 170)], fill=shadow_color, width=2)
    
    # Inner Neckband (Navy Blue Contrast)
    draw.polygon([(160, 75), (240, 75), (200, 120)], fill=(30, 45, 80))
    
    # Folded Collar Wings
    left_collar = [(150, 75), (100, 130), (185, 125), (180, 75)]
    right_collar = [(250, 75), (300, 130), (215, 125), (220, 75)]
    draw.polygon(left_collar, fill=(145, 190, 230), outline=(50, 80, 120))
    draw.polygon(right_collar, fill=(145, 190, 230), outline=(50, 80, 120))
    
    # Left Chest Pocket with Pen Border
    pocket = [(90, 200), (150, 200), (150, 270), (120, 290), (90, 270)]
    draw.polygon(pocket, fill=(135, 180, 220), outline=line_color)
    draw.line([(95, 205), (145, 205)], fill=shadow_color, width=1)
    
    # Center Button Placket
    if condition == "asymmetric":
        p_top_x, p_bot_x = 175, 235  # Crooked placket (~10° deviation)
    else:
        p_top_x, p_bot_x = 200, 200  # Perfectly straight placket
        
    p_width = 28
    placket_poly = [
        (p_top_x - p_width // 2, 125),
        (p_top_x + p_width // 2, 125),
        (p_bot_x + p_width // 2, 460),
        (p_bot_x - p_width // 2, 460)
    ]
    draw.polygon(placket_poly, fill=placket_color, outline=(40, 70, 110))
    # Stitched outer edges of placket
    draw.line([(p_top_x - p_width // 2 + 3, 125), (p_bot_x - p_width // 2 + 3, 460)], fill=(50, 80, 120), width=2)
    draw.line([(p_top_x + p_width // 2 - 3, 125), (p_bot_x + p_width // 2 - 3, 460)], fill=(50, 80, 120), width=2)
    
    # 4 Authentic 4-Hole Buttons with Cross-Stitching
    for t_step in [0.15, 0.38, 0.62, 0.85]:
        bx = int(p_top_x + t_step * (p_bot_x - p_top_x))
        by = int(125 + t_step * (460 - 125))
        draw.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=(235, 240, 245), outline=(90, 120, 150))
        draw.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(245, 250, 255), outline=(160, 180, 200))
        draw.point([(bx - 2, by - 2), (bx + 2, by - 2), (bx - 2, by + 2), (bx + 2, by + 2)], fill=(50, 70, 100))

    img_bgr = np.array(base.convert("RGB"))[:, :, ::-1].copy()
    if condition == "blurry":
        img_bgr = cv2.GaussianBlur(img_bgr, (27, 27), 0)
        
    return img_bgr

def run_vision_screening(image_np):
    """Executes OpenCV Laplacian Blur & Hough Line placket linearity checks."""
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    laplacian_var = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    blur_passed = laplacian_var >= 55.0
    
    w = image_np.shape[1]
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=40, minLineLength=50, maxLineGap=15)
    
    max_angle_dev = 0.0
    annotated = image_np.copy()
    
    if lines is not None:
        for line in lines:
            coords = line.reshape(-1)
            if len(coords) >= 4:
                x1, y1, x2, y2 = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])
                mid_x = (x1 + x2) / 2
                # Screen placket candidates in the central 35% - 65% width
                if 0.35 * w <= mid_x <= 0.65 * w:
                    dy = abs(y2 - y1)
                    dx = abs(x2 - x1)
                    if dy > 50 and dy > dx:  # Vertical seam candidate
                        angle = abs(np.arctan2(dx, dy) * 180.0 / np.pi)
                        if angle > max_angle_dev:
                            max_angle_dev = angle
                        color = (34, 197, 94) if angle <= 3.5 else (239, 68, 68)
                        cv2.line(annotated, (x1, y1), (x2, y2), color, 2)
    
    seam_passed = max_angle_dev <= 3.5
    return {
        "laplacian_var": round(laplacian_var, 1),
        "blur_passed": blur_passed,
        "max_angle_dev": round(max_angle_dev, 1),
        "seam_passed": seam_passed,
        "annotated_img": annotated
    }


# -----------------------------------------------------------------------------
# 5. MULTILINGUAL LOGIN SCREEN
# -----------------------------------------------------------------------------
def render_login_screen():
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 28px;">
        <span style="font-size: 54px; filter: drop-shadow(0 0 16px rgba(244, 114, 182, 0.4));">🌸</span>
        <h1 style="font-size: 34px; font-weight: 900; color: #f8fafc; margin: 10px 0 6px 0; letter-spacing: -0.5px;">
            {t("app_title")}
        </h1>
        <p style="font-size: 16px; color: #94a3b8; font-weight: 500; max-width: 600px; margin: 0 auto 14px auto;">
            {t("app_subtitle")}
        </p>
        <span style="background: rgba(99, 102, 241, 0.15); color: #a5b4fc; border: 1px solid rgba(99, 102, 241, 0.3); padding: 5px 14px; border-radius: 9999px; font-size: 12px; font-weight: 700; letter-spacing: 0.4px;">
            {t("challenge_badge")}
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.container():
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, rgba(22, 31, 48, 0.95) 0%, rgba(15, 23, 42, 0.98) 100%); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 18px; padding: 30px; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.7), inset 0 1px 0 rgba(255,255,255,0.05);">
                <h3 style="margin-top: 0; color: #f8fafc; font-size: 20px; font-weight: 700; border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding-bottom: 14px;">
                    {t("login_box_title")}
                </h3>
            """, unsafe_allow_html=True)
            
            # Language Selection Dropdown
            lang_options = [
                ("en", "🇬🇧 English"),
                ("ta", "🇮🇳 தமிழ் (Tamil)"),
                ("kn", "🇮🇳 ಕನ್ನಡ (Kannada)"),
                ("hi", "🇮🇳 हिन्दी (Hindi)")
            ]
            current_lang_idx = [opt[0] for opt in lang_options].index(st.session_state.lang)
            
            chosen_lang_tuple = st.selectbox(
                t("select_lang"),
                options=lang_options,
                index=current_lang_idx,
                format_func=lambda x: x[1]
            )
            
            if chosen_lang_tuple[0] != st.session_state.lang:
                st.session_state.lang = chosen_lang_tuple[0]
                st.rerun()
                
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            
            # Role Radio Selection
            role_options = [t("role_leader"), t("role_artisan")]
            role_choice = st.radio(t("select_access"), role_options, index=0)
            is_leader = role_choice == t("role_leader")
            
            cur_lang = st.session_state.lang
            
            if is_leader:
                leader_options = [m for m in st.session_state.members if m["is_leader"]]
                selected_leader = st.selectbox(
                    t("select_leader_name"),
                    options=leader_options,
                    format_func=lambda x: f"{x['id']} — {x['names_by_lang'].get(cur_lang, x['name'])} • {x['role']}"
                )
                chosen_user = selected_leader
            else:
                member_options = st.session_state.members
                selected_member = st.selectbox(
                    t("select_artisan_name"),
                    options=member_options,
                    index=1,
                    format_func=lambda x: f"{x['id']} — {x['names_by_lang'].get(cur_lang, x['name'])} • [{x['stage']}] • {x['machine']}"
                )
                chosen_user = selected_member
            
            pin_input = st.text_input(t("security_pin"), value="1234", type="password")
            
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            
            if st.button(t("launch_btn"), use_container_width=True, type="primary"):
                st.session_state.logged_in = True
                st.session_state.user_role = "Leader" if is_leader else "Artisan"
                st.session_state.user_id = chosen_user["id"]
                st.session_state.user_name = chosen_user["names_by_lang"].get(cur_lang, chosen_user["name"])
                st.session_state.user_profile = chosen_user
                st.rerun()
            
            st.markdown(f"""
                <div style="font-size: 11px; color: #64748b; text-align: center; margin-top: 14px;">
                    {t("demo_pin_hint")}
                </div>
            </div>
            """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 6. HEADER BAR & NAVIGATION
# -----------------------------------------------------------------------------
def render_header():
    user = st.session_state.user_profile
    role = st.session_state.user_role
    cur_lang = st.session_state.lang
    display_name = user["names_by_lang"].get(cur_lang, user["name"])
    
    col_a, col_lang, col_b = st.columns([3, 1.2, 1])
    with col_a:
        badge_text = t("leader_view_badge") if role == "Leader" else t("artisan_view_badge")
        badge_gradient = "linear-gradient(135deg, #4338ca 0%, #6366f1 100%)" if role == "Leader" else "linear-gradient(135deg, #059669 0%, #10b981 100%)"
        badge_glow = "rgba(99, 102, 241, 0.35)" if role == "Leader" else "rgba(16, 185, 129, 0.35)"
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(22, 31, 48, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 12px 20px; margin-bottom: 16px; display: flex; align-items: center; box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
            <span style="background: {badge_gradient}; color: white; padding: 4px 12px; border-radius: 9999px; font-size: 11px; font-weight: 700; margin-right: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px {badge_glow};">
                {badge_text}
            </span>
            <span style="font-size: 16px; font-weight: 700; color: #f8fafc;">
                {user['id']} — {display_name}
            </span>
            <span style="color: #94a3b8; font-size: 13px; margin-left: 10px;">
                • {user['machine']} • {user['stage']}
            </span>
        </div>
        """, unsafe_allow_html=True)
    with col_lang:
        lang_map = {"en": "🇬🇧 English", "ta": "🇮🇳 தமிழ்", "kn": "🇮🇳 ಕನ್ನಡ", "hi": "🇮🇳 हिन्दी"}
        new_lang = st.selectbox(
            "Language",
            options=["en", "ta", "kn", "hi"],
            index=["en", "ta", "kn", "hi"].index(cur_lang),
            format_func=lambda x: lang_map[x],
            label_visibility="collapsed"
        )
        if new_lang != cur_lang:
            st.session_state.lang = new_lang
            st.rerun()
    with col_b:
        if st.button(t("switch_profile"), use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_role = None
            st.session_state.user_id = None
            st.session_state.user_name = None
            st.rerun()


# -----------------------------------------------------------------------------
# 7. LEADER DASHBOARD VIEW
# -----------------------------------------------------------------------------
def render_leader_dashboard():
    cur_lang = st.session_state.lang
    jains_val = calculate_jains_fairness(st.session_state.members)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{t("active_bulk_order")}</div>
            <div class="kpi-value">500 <span style="font-size: 14px; font-weight: 500; color:#94a3b8;">{t("shirts_unit")}</span></div>
            <div class="kpi-sub">Day 4 of 10 • Uniform Cluster</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{t("stage_b_throughput")}</div>
            <div class="kpi-value">136 / 190</div>
            <div class="kpi-sub" style="color: #f87171;">⚠️ Shortfall: 7 units (M06)</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{t("jains_index")}</div>
            <div class="kpi-value">{jains_val}</div>
            <div class="kpi-sub" style="color: #34d399;">{t("proven_fair")}</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{t("enterprise_quote")}</div>
            <div class="kpi-value">₹324.24</div>
            <div class="kpi-sub" style="color: #94a3b8;">Floor: ₹260.55 • Margin: 10%</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    
    # Leader Navigation Tabs
    tabs = st.tabs([
        t("tab1"), t("tab2"), t("tab3"), t("tab4"), t("tab5"), t("tab6")
    ])
    
    # TAB 1: PIPELINE & MORNING ROLL-CALL
    with tabs[0]:
        st.subheader(t("pipeline_overview_title"))
        p1, p2, p3 = st.columns(3)
        with p1:
            st.markdown(f"**{t('stage_a_title')}**")
            st.progress(1.0, text="500 / 500 Kits Cut (100%)")
            st.caption("Rate: ₹8/set • 8 mins/set • M10 Lead")
        with p2:
            st.markdown(f"**{t('stage_b_title')}**")
            st.progress(136/500, text="136 / 500 Sewn (Expected 190 by Day 4)")
            st.caption("Rate: ₹45/set • 45 mins/set • Cap: 58.67/day")
        with p3:
            st.markdown(f"**{t('stage_c_title')}**")
            st.progress(105/500, text="105 / 500 Finished & Packed (72%)")
            st.caption("Rate: ₹17/set • 12 mins/set • M09 & M12")
            
        st.markdown("---")
        
        # DAILY MORNING ROLL-CALL & MACHINE MODIFIER STUDIO
        with st.expander(f"**{t('morning_rollcall_title')}**", expanded=False):
            st.markdown(f"<div class='explainer-banner'>{t('morning_rollcall_desc')}</div>", unsafe_allow_html=True)
            
            rollcall_rows = []
            for m in st.session_state.members:
                rollcall_rows.append({
                    "ID": m["id"],
                    "Artisan Name": m["names_by_lang"].get(cur_lang, m["name"]),
                    "Stage": m["stage"],
                    "Available Hours": float(m["hours"]),
                    "Machine Type": m["machine"]
                })
            
            df_rollcall = pd.DataFrame(rollcall_rows)
            edited_rollcall = st.data_editor(
                df_rollcall,
                column_config={
                    "ID": st.column_config.TextColumn(disabled=True),
                    "Artisan Name": st.column_config.TextColumn(disabled=True),
                    "Stage": st.column_config.TextColumn(disabled=True),
                    "Available Hours": st.column_config.NumberColumn(min_value=0.0, max_value=8.0, step=0.5, required=True),
                    "Machine Type": st.column_config.SelectboxColumn(
                        options=[
                            "Motorized Industrial Juki",
                            "Motorized Domestic Sewing",
                            "Manual Foot Pedal Sewing",
                            "Buttonholer & Steam Desk",
                            "Heavy Tailoring Shears",
                            "Inspection Table & Bagger",
                            "Machine Under Repair / Off-line"
                        ],
                        required=True
                    )
                },
                hide_index=True,
                use_container_width=True,
                key="rollcall_editor"
            )
            
            if st.button(t("btn_save_rollcall"), type="primary", use_container_width=True):
                # Update session state members with new hours & machine status
                mult_map = {
                    "Motorized Industrial Juki": 1.45,
                    "Motorized Domestic Sewing": 1.30,
                    "Manual Foot Pedal Sewing": 0.95,
                    "Buttonholer & Steam Desk": 1.50,
                    "Heavy Tailoring Shears": 1.20,
                    "Inspection Table & Bagger": 1.50,
                    "Machine Under Repair / Off-line": 0.0
                }
                for idx, row in edited_rollcall.iterrows():
                    for m in st.session_state.members:
                        if m["id"] == row["ID"]:
                            m["hours"] = float(row["Available Hours"])
                            m["machine"] = row["Machine Type"]
                            mult = mult_map.get(m["machine"], 1.0)
                            m["mult"] = mult
                            # Recalculate daily capacity
                            if m["machine"] == "Machine Under Repair / Off-line" or m["hours"] == 0:
                                m["daily_cap"] = 0.0
                            elif m["stage_code"] == "B":
                                m["daily_cap"] = round(m["hours"] * mult * (1.0 - m["defect"]) * 1.8, 2)
                            else:
                                m["daily_cap"] = round(m["hours"] * mult * 5.0, 2)
                                
                new_jain = calculate_jains_fairness(st.session_state.members)
                total_cap = sum(m["daily_cap"] for m in st.session_state.members if m["stage_code"] == "B")
                st.toast(t("rollcall_saved_toast", cap=round(total_cap, 1), jain=new_jain), icon="✅")
                st.rerun()

        st.subheader(t("table_title"))
        df_members = pd.DataFrame([
            {
                "ID": m["id"],
                "Artisan Name": m["names_by_lang"].get(cur_lang, m["name"]),
                "Stage": m["stage"],
                "Machine Type": m["machine"],
                "Avail (h)": m["hours"],
                "Daily Cap": m["daily_cap"],
                "10d Max Cap": round(m["daily_cap"] * 10, 1),
                "Allocated": m["allocated"],
                "Completed": m["done"],
                "Util Ratio": round(m["allocated"] / (m["daily_cap"] * 10), 3) if m["daily_cap"] > 0 else 0.0
            } for m in st.session_state.members
        ])
        st.dataframe(df_members, use_container_width=True, hide_index=True)
        st.info(t("jains_note", val=jains_val))

    # TAB 2: 7-PHASE REBALANCER
    with tabs[1]:
        st.subheader(t("day4_crisis_title"))
        st.markdown(f"<div class='explainer-banner'>{t('day4_explainer')}</div>", unsafe_allow_html=True)
        st.markdown(t("day4_crisis_desc"))
        
        state = st.session_state.rebalance_state
        col_ctrl, col_diag = st.columns([1, 2])
        with col_ctrl:
            st.markdown("### Incident Control")
            if state == "IDLE":
                if st.button(t("sim_emergency_btn"), type="primary", use_container_width=True):
                    st.session_state.rebalance_state = "DETECTED"
                    st.rerun()
            elif state in ["DETECTED", "PROPOSED"]:
                st.warning("⚠️ Day 4 Shortfall: Δ = 7 sewing sets")
                if st.button(t("agent_generate_btn"), use_container_width=True):
                    st.session_state.rebalance_state = "PROPOSED"
                    st.rerun()
            elif state == "PROPOSED":
                st.success("✅ Volunteer Candidate Proposal Generated")
                if st.button(t("obtain_consent_btn"), type="primary", use_container_width=True):
                    st.session_state.rebalance_state = "VOLUNTEERS_ACCEPTED"
                    st.rerun()
            elif state == "VOLUNTEERS_ACCEPTED":
                st.success("✅ Volunteers Consented!")
                if st.button(t("commit_rebalance_btn"), type="primary", use_container_width=True):
                    for m in st.session_state.members:
                        if m["id"] == "M06": m["allocated"] -= 7
                        elif m["id"] == "M03": m["allocated"] += 4
                        elif m["id"] == "M02": m["allocated"] += 3
                    st.session_state.rebalance_state = "COMMITTED"
                    st.rerun()
            elif state == "COMMITTED":
                st.success("🎉 Rebalancing Successfully Committed!")
                if st.button(t("reset_sim_btn"), use_container_width=True):
                    st.session_state.rebalance_state = "IDLE"
                    for m in st.session_state.members:
                        if m["id"] == "M06": m["allocated"] = 18
                        elif m["id"] == "M03": m["allocated"] = 53
                        elif m["id"] == "M02": m["allocated"] = 44
                    st.rerun()
                    
        with col_diag:
            st.markdown("### 7-Phase Agentic State Trace")
            phases = [
                (t("phase1_title"), t("phase1_desc"), state != "IDLE"),
                (t("phase2_title"), t("phase2_desc"), state in ["PROPOSED", "VOLUNTEERS_ACCEPTED", "COMMITTED"]),
                (t("phase3_title"), t("phase3_desc"), state in ["PROPOSED", "VOLUNTEERS_ACCEPTED", "COMMITTED"]),
                (t("phase4_title"), t("phase4_desc"), state in ["PROPOSED", "VOLUNTEERS_ACCEPTED", "COMMITTED"]),
                (t("phase5_title"), t("phase5_desc"), state in ["PROPOSED", "VOLUNTEERS_ACCEPTED", "COMMITTED"]),
                (t("phase6_title"), t("phase6_desc"), state in ["VOLUNTEERS_ACCEPTED", "COMMITTED"]),
                (t("phase7_title"), t("phase7_desc"), state == "COMMITTED")
            ]
            for p_title, p_desc, is_active in phases:
                color = "#34d399" if is_active else "#475569"
                title_color = "#34d399" if is_active else "#94a3b8"
                desc_color = "#e2e8f0" if is_active else "#64748b"
                bg_card = "rgba(16, 185, 129, 0.08)" if is_active else "rgba(255, 255, 255, 0.02)"
                icon = "🟢" if is_active else "⚪"
                st.markdown(f"""
                <div style="border-left: 3px solid {color}; padding: 8px 14px; margin-bottom: 10px; background: {bg_card}; border-radius: 0 10px 10px 0;">
                    <span style="font-weight: 700; color: {title_color}; font-size: 13px;">{icon} {p_title}</span>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: {desc_color}; line-height: 1.4;">{p_desc}</p>
                </div>
                """, unsafe_allow_html=True)

    # TAB 3: COSTING BOM
    with tabs[2]:
        st.subheader(t("bom_title"))
        st.markdown(f"<div class='explainer-banner'>{t('bom_explainer')}</div>", unsafe_allow_html=True)
        buyer_offer = st.slider(t("buyer_offer_label"), min_value=140, max_value=350, value=275, step=5)
        
        operating_floor = 260.55
        cost_plus_ref = 291.82
        commercial_quote = 324.24
        
        c1, c2, c3 = st.columns(3)
        with c1:
            diff_floor = buyer_offer - operating_floor
            color_floor = "#f87171" if diff_floor < 0 else "#34d399"
            st.markdown(f"""
            <div class="kpi-card" style="border-top: 4px solid {color_floor};">
                <div class="kpi-label">{t("vs_operating_floor")}</div>
                <div class="kpi-value" style="color: {color_floor};">{'₹' if diff_floor>=0 else '-₹'}{abs(round(diff_floor, 2))}</div>
                <div class="kpi-sub" style="color: {color_floor};">{round((diff_floor/operating_floor)*100, 1)}% Margin</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            diff_ref = buyer_offer - cost_plus_ref
            color_ref = "#f87171" if diff_ref < 0 else "#34d399"
            st.markdown(f"""
            <div class="kpi-card" style="border-top: 4px solid {color_ref};">
                <div class="kpi-label">{t("vs_cost_plus")}</div>
                <div class="kpi-value" style="color: {color_ref};">{'₹' if diff_ref>=0 else '-₹'}{abs(round(diff_ref, 2))}</div>
                <div class="kpi-sub" style="color: {color_ref};">{round((diff_ref/cost_plus_ref)*100, 1)}% Deficit</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            diff_comm = buyer_offer - commercial_quote
            color_comm = "#f87171" if diff_comm < 0 else "#34d399"
            st.markdown(f"""
            <div class="kpi-card" style="border-top: 4px solid {color_comm};">
                <div class="kpi-label">{t("vs_enterprise_margin")}</div>
                <div class="kpi-value" style="color: {color_comm};">{'₹' if diff_comm>=0 else '-₹'}{abs(round(diff_comm, 2))}</div>
                <div class="kpi-sub" style="color: {color_comm};">{round((diff_comm/commercial_quote)*100, 1)}% Deficit</div>
            </div>
            """, unsafe_allow_html=True)
            
        if buyer_offer < operating_floor:
            st.error(t("predatory_alert", offer=buyer_offer, deficit=abs(round(diff_floor, 2)), loss=int(abs(diff_floor)*500)))
            
        bom_data = [
            {"Cost Component": "Mill-Certified Poly-Cotton Drill (2.2m)", "Unit Cost (₹)": 143.00, "Source Class": "[SUPPLIER_QUOTATION]", "Basis": "Wholesale textile cluster invoice"},
            {"Cost Component": "Haberdashery Trims (Buttons, Elastic, Zip)", "Unit Cost (₹)": 22.00, "Source Class": "[SUPPLIER_QUOTATION]", "Basis": "Haberdashery wholesale pack price"},
            {"Cost Component": "Cutting Marker Wastage Allowance (7%)", "Unit Cost (₹)": 11.55, "Source Class": "[ESTIMATED_ASSUMPTION]", "Basis": "Standard marker layout loss for 2-piece pattern"},
            {"Cost Component": "Direct Artisan Stitching Labor (70 mins)", "Unit Cost (₹)": 70.00, "Source Class": "[GROUP_AGREED_RATE]", "Basis": "Voted at SHG Resolution #42 @ ₹60/hr benchmark"},
            {"Cost Component": "Packaging, Steam Iron & Local Logistics", "Unit Cost (₹)": 14.00, "Source Class": "[ESTIMATED_ASSUMPTION]", "Basis": "Amortized packaging & freight carton"},
            {"Cost Component": "1. BASE OPERATING COST FLOOR", "Unit Cost (₹)": 260.55, "Source Class": "[CALCULATED_QUOTE]", "Basis": "Break-even operating expenses sum"},
            {"Cost Component": "2. Group Savings Corpus Fund (12%)", "Unit Cost (₹)": 31.27, "Source Class": "[GROUP_AGREED_RATE]", "Basis": "Retained in SHG bank account for machine repairs"},
            {"Cost Component": "COST-PLUS REFERENCE BENCHMARK", "Unit Cost (₹)": 291.82, "Source Class": "[CALCULATED_QUOTE]", "Basis": "Floor + 12% collective reserve"},
            {"Cost Component": "3. Commercial Profit Margin (10%)", "Unit Cost (₹)": 32.42, "Source Class": "[ESTIMATED_ASSUMPTION]", "Basis": "Enterprise procurement margin"},
            {"Cost Component": "FINAL RECOMMENDED B2B QUOTE", "Unit Cost (₹)": 324.24, "Source Class": "[CALCULATED_QUOTE]", "Basis": "Formula: (Operating + Reserve) / (1 - Margin)"}
        ]
        st.dataframe(pd.DataFrame(bom_data), use_container_width=True, hide_index=True)

    # TAB 4: REALISTIC VISION QC DESK
    with tabs[3]:
        st.subheader(t("cv_title"))
        st.markdown(t("cv_desc"))
        
        sample_choice = st.selectbox(
            t("cv_sample_prompt"),
            [t("cv_sample1"), t("cv_sample2"), t("cv_sample3")]
        )
        img_type = "valid" if sample_choice == t("cv_sample1") else ("blurry" if sample_choice == t("cv_sample2") else "asymmetric")
        img_np = generate_realistic_shirt_image(img_type)
        
        # Option to upload real photo
        uploaded_qc = st.file_uploader(t("cv_or_upload"), type=["jpg", "jpeg", "png", "webp"], key="leader_qc_upload")
        if uploaded_qc is not None:
            bytes_data = uploaded_qc.read()
            decoded = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            if decoded is not None:
                img_np = cv2.resize(decoded, (400, 480))
        
        vision_res = run_vision_screening(img_np)
        
        col_img1, col_img2, col_stats = st.columns([1, 1, 1.2])
        with col_img1:
            st.markdown(f"**{t('cv_original')}**")
            st.image(img_np, channels="BGR", use_container_width=True)
        with col_img2:
            st.markdown(f"**{t('cv_overlay')}**")
            st.image(vision_res["annotated_img"], channels="BGR", use_container_width=True)
        with col_stats:
            st.markdown(f"### {t('cv_diagnostics')}")
            blur_status = "🟢 PASS (> 55.0)" if vision_res["blur_passed"] else "🔴 FAIL (< 55.0)"
            st.metric(t("blur_var_label"), f"{vision_res['laplacian_var']}", blur_status)
            seam_status = "🟢 PASS (≤ 3.5°)" if vision_res["seam_passed"] else "🔴 REVIEW (> 3.5°)"
            st.metric(t("angle_dev_label"), f"{vision_res['max_angle_dev']}°", seam_status)
            
            st.markdown("---")
            st.markdown(f"**{t('human_decision')}**")
            d1, d2, d3 = st.columns(3)
            with d1:
                if st.button(t("btn_accept"), use_container_width=True):
                    st.toast("Accepted!", icon="✅")
            with d2:
                if st.button(t("btn_rework"), use_container_width=True):
                    st.toast("Rework Flagged!", icon="⚠️")
            with d3:
                if st.button(t("btn_reject"), use_container_width=True):
                    st.toast("Rejected!", icon="❌")

    # TAB 5: PAYROLL & QUORUM
    with tabs[4]:
        st.subheader(t("payroll_title"))
        st.markdown(t("payroll_desc"))
        
        payroll_rows = []
        for m in st.session_state.members:
            gross = m["done"] * m["wage_rate"]
            net = max(0.0, gross - m["advance"])
            vote_status = st.session_state.quorum_votes.get(m["id"], "PENDING")
            payroll_rows.append({
                "Member ID": m["id"],
                "Name": m["names_by_lang"].get(cur_lang, m["name"]),
                "Stage": m["stage"],
                "Accepted Pieces": m["done"],
                "Piece Rate": f"₹{m['wage_rate']}",
                "Gross Earned": f"₹{gross:.2f}",
                "Advance Deducted": f"₹{m['advance']:.2f}",
                "Net Payable": f"₹{net:.2f}",
                "Dispute Status": "⚠️ FROZEN" if m["disputed"] else "🟢 CLEAR",
                "Quorum Vote": "👍 YES" if vote_status == "APPROVED" else ("❌ NO" if vote_status == "OBJECTED" else "⏳ PENDING")
            })
            
        st.dataframe(pd.DataFrame(payroll_rows), use_container_width=True, hide_index=True)
        
        approved_votes = sum(1 for v in st.session_state.quorum_votes.values() if v == "APPROVED")
        quorum_pct = (approved_votes / 12.0)
        
        q_col1, q_col2 = st.columns([2, 1])
        with q_col1:
            st.markdown(f"**{t('quorum_progress_label')}** {approved_votes} of 12 ({quorum_pct*100:.1f}%)")
            st.progress(quorum_pct)
            if approved_votes >= 8:
                st.success(t("quorum_met"))
            else:
                st.warning(t("quorum_pending", needed=8 - approved_votes))
                
        with q_col2:
            if st.button(t("btn_cast_votes"), use_container_width=True):
                for mid in st.session_state.quorum_votes:
                    st.session_state.quorum_votes[mid] = "APPROVED"
                st.rerun()
            if approved_votes >= 8:
                if st.button(t("btn_sign_disburse"), type="primary", use_container_width=True):
                    st.balloons()
                    st.toast("Disbursed!", icon="🎉")

    # TAB 6: ORDER PASSPORT
    with tabs[5]:
        st.subheader(t("passport_title"))
        st.markdown(t("passport_desc"))
        
        passport_text = f"""========================================================================================
                          🌸 SAHAKARI AI — B2B ORDER PASSPORT
                     Official Ethical Fulfilment & Fair Wage Dossier
========================================================================================
Order Reference:       PO-2026-UNIFORM-500          Completion Date:   28 Nov 2026
Producer Enterprise:   Annai Therasa SHG Cluster    Buyer:             District Education Dept
Product Description:   500 School Uniforms (Sz 32)  Total Commercial:  ₹1,62,120.00
Language Locale:       {cur_lang.upper()}                        Generated At:      {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
----------------------------------------------------------------------------------------
1. PRODUCTION & TRACEABILITY SUMMARY
   • Total Units Ordered:       500 Sets            Total Units Accepted:   500 Sets
   • Lead Time Forecast:        10 Days             Actual Delivery Window: 10 Days
   • Production Bottleneck:     Stage B (Sewing)    Rebalancing Incidents:  1 (Day 4: Consensual)
   • Stage A (Cut/Kit):         500 Units Accepted  Defect Scrappage:       3 Units (Re-cut)
   • Stage B (Sewing):          500 Units Accepted  Rework Resolved:        7 Units Reworked
   • Stage C (Finish/Pack):     500 Units Accepted  Final Quality Pass:     100% by Human Leader

2. ETHICAL LABOR & FAIR WAGE AUDIT TRAIL
   • Direct Labor Disbursed:    ₹35,000.00          Average Effective Wage: ₹64.20 / hr
   • Rural Wage Benchmark:      ₹60.00 / hr         Compliance Index:       107.0% of Floor
   • SHG Group Savings Corpus:  ₹15,635.00          Bank Account:           IOB SB A/C #...4102
   • Allocation Fairness Index: J = 0.9841          Consensus Quorum:       100% (12/12 Signed)

3. PROVENANCE & RECORD INTEGRITY
   • CPL Event Trail Length:    1,428 Events        Merkle Root Hash:       9f83a...bc412
   • Privacy Protection:        Individual member bank account details withheld under SHG bylaws.
========================================================================================"""
        
        st.text_area("Order Passport Preview:", passport_text, height=320)
        st.download_button(
            label=t("btn_download_passport"),
            data=passport_text,
            file_name=f"SAHAKARI_ORDER_PASSPORT_PO-2026_{cur_lang.upper()}.txt",
            mime="text/plain",
            use_container_width=True
        )


# -----------------------------------------------------------------------------
# 8. ARTISAN / MEMBER DASHBOARD VIEW (MULTILINGUAL AUDIO PASSBOOK & PHOTO UPLOAD)
# -----------------------------------------------------------------------------
def render_artisan_dashboard():
    user = st.session_state.user_profile
    cur_lang = st.session_state.lang
    display_name = user["names_by_lang"].get(cur_lang, user["name"])
    
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <h2 style="font-size: 26px; font-weight: 800; color: #f8fafc; margin: 0;">
            {t("member_greeting", name=display_name)}
        </h2>
        <p style="color: #94a3b8; font-size: 14px; margin: 4px 0 0 0;">
            {t("member_workspace_sub", stage=user['stage'], machine=user['machine'])}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 1. My Work Today
    st.markdown(f"### {t('my_work_today_title')}")
    target_today = 4 if user["stage_code"] == "B" else 25
    
    st.markdown(f"""
    <div class="member-action-card" style="border-left: 6px solid #10b981;">
        <span class="action-badge-green">{t("today_target_badge")}</span>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 14px;">
            <div>
                <h3 style="margin: 0; font-size: 24px; color: #f8fafc;">{user['stage']}</h3>
                <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 14px;">{user['machine']}</p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 32px; font-weight: 800; color: #34d399;">{target_today} <span style="font-size: 16px; font-weight: 500; color: #94a3b8;">{t("shirts_unit")}</span></div>
                <div style="font-size: 13px; font-weight: 600; color: #38bdf8;">{t("piece_rate_label", rate=user['wage_rate'])}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Work Submission & Real-Time Photo Verification
    st.markdown(f"### {t('completed_submission_title')}")
    col_sub1, col_sub2 = st.columns([1.2, 1.2])
    with col_sub1:
        st.markdown(f"**{t('completed_units_label')}**")
        qty_input = st.number_input("Units:", min_value=1, max_value=20, value=4, step=1, label_visibility="collapsed")
        offline_sim = st.toggle(t("offline_toggle_label"), value=False)
        
        if st.button(t("submit_work_btn"), type="primary", use_container_width=True):
            if offline_sim:
                st.session_state.offline_outbox.append({"qty": qty_input})
                st.warning(t("saved_offline_msg", qty=qty_input))
            else:
                user["done"] += qty_input
                st.success(t("synced_online_msg", qty=qty_input, ts=int(time.time())))
                st.rerun()
                
        if not offline_sim and len(st.session_state.offline_outbox) > 0:
            st.info(t("network_restored_msg", count=len(st.session_state.offline_outbox)))
            for ev in st.session_state.offline_outbox:
                user["done"] += ev["qty"]
            st.session_state.offline_outbox = []
            st.rerun()
            
    with col_sub2:
        st.markdown(f"**{t('upload_garment_photo')}**")
        uploaded_member_photo = st.file_uploader("", type=["jpg", "jpeg", "png", "webp"], key="artisan_photo_upload", label_visibility="collapsed")
        
        # Test or verify uploaded photo
        if uploaded_member_photo is not None:
            bytes_img = uploaded_member_photo.read()
            member_img = cv2.imdecode(np.frombuffer(bytes_img, np.uint8), cv2.IMREAD_COLOR)
            if member_img is not None:
                member_res = run_vision_screening(member_img)
                st.image(member_res["annotated_img"], channels="BGR", use_container_width=True)
                if member_res["blur_passed"]:
                    st.success(t("photo_pass_msg", val=member_res["laplacian_var"]))
                else:
                    st.error(t("photo_blur_fail_msg", val=member_res["laplacian_var"]))
        else:
            # Default Realistic Sample Shirt preview
            sample_preview = generate_realistic_shirt_image("valid")
            st.image(sample_preview, channels="BGR", caption="Standard Finished School Uniform Shirt Guide", width=200)
            
    st.markdown("---")
    
    # 3. Audio Passbook (Fixed HTML Formatting - No Raw Code Display)
    st.markdown(f"### {t('hear_earnings_title')}")
    gross_val = user["done"] * user["wage_rate"]
    net_val = max(0.0, gross_val - user["advance"])
    
    col_a1, col_a2 = st.columns([1, 1.2])
    with col_a1:
        # Cleanly styled metrics without indented empty lines
        st.markdown(
            f'<div style="background: linear-gradient(135deg, rgba(22, 31, 48, 0.95) 0%, rgba(15, 23, 42, 0.98) 100%); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 24px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">'
            f'<div style="font-size: 12.5px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">{t("gross_label")}</div>'
            f'<div style="font-size: 30px; font-weight: 900; color: #f8fafc; margin-top: 4px; letter-spacing: -0.5px;">₹{gross_val:.2f}</div>'
            f'<div style="font-size: 12px; color: #64748b;">{user["done"]} {t("shirts_unit")} × ₹{user["wage_rate"]}</div>'
            f'<hr style="border: 0; border-top: 1px dashed rgba(255, 255, 255, 0.12); margin: 14px 0;">'
            f'<div style="font-size: 12.5px; font-weight: 700; color: #f87171; text-transform: uppercase; letter-spacing: 0.5px;">{t("advance_label")}</div>'
            f'<div style="font-size: 22px; font-weight: 800; color: #f87171; margin-top: 2px;">- ₹{user["advance"]:.2f}</div>'
            f'<hr style="border: 0; border-top: 2px solid rgba(255, 255, 255, 0.15); margin: 14px 0;">'
            f'<div style="font-size: 13px; font-weight: 800; color: #34d399; text-transform: uppercase; letter-spacing: 0.5px;">{t("net_payable_label")}</div>'
            f'<div style="font-size: 36px; font-weight: 900; color: #34d399; margin-top: 4px; letter-spacing: -1px; text-shadow: 0 0 20px rgba(52, 211, 153, 0.3);">₹{net_val:.2f}</div>'
            f'<div style="margin-top: 16px;"><span class="action-badge-amber">{t("awaiting_quorum_badge")}</span></div>'
            f'</div>',
            unsafe_allow_html=True
        )
        
    with col_a2:
        # Multilingual Speech Synthesis text tailored to current language
        if cur_lang == "ta":
            speech_text = f"வணக்கம் {display_name} அம்மாள். நீங்கள் இந்த வரிசையில் இதுவரை {user['done']} பள்ளி சீருடைகளை வெற்றிகரமாக தைத்து முடித்துள்ளீர்கள். ஒரு சீருடைக்கு குழு ஒப்புதல் அளித்த {user['wage_rate']} ரூபாய் வீதம் உங்கள் மொத்த உழைப்பு வருமானம் {int(gross_val)} ரூபாய். நீங்கள் பெற்ற முன்பணம் கழிவு {int(user['advance'])} ரூபாய். உங்கள் வங்கிக் கணக்கில் வரவு வைக்க பரிந்துரைக்கப்பட்ட நிகர தொகை {int(net_val)} ரூபாய். இந்த பட்டியல் குழு ஒப்புதலுக்காக காத்திருக்கிறது."
        elif cur_lang == "kn":
            speech_text = f"ನಮಸ್ಕಾರ {display_name} ಅವರೇ. ಈ ಆದೇಶದಲ್ಲಿ ನೀವು ಇದುವರೆಗೆ {user['done']} ಶಾಲಾ ಸಮವಸ್ತ್ರಗಳನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಹೊಲಿದಿದ್ದೀರಿ. ಪ್ರತಿ ಸಮವಸ್ತ್ರಕ್ಕೆ {user['wage_rate']} ರೂಪಾಯಿಯಂತೆ ನಿಮ್ಮ ಒಟ್ಟು ಆದಾಯ {int(gross_val)} ರೂಪಾಯಿ. ಮುಂಗಡ ಕಡಿತ {int(user['advance'])} ರೂಪಾಯಿ. ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗಲಿರುವ ನಿವ್ವಳ ಮೊತ್ತ {int(net_val)} ರೂಪಾಯಿ. ಈ ಪಟ್ಟಿಯು ಗುಂಪಿನ ಅನುಮೋದನೆಗೆ ಕಾಯುತ್ತಿದೆ."
        elif cur_lang == "hi":
            speech_text = f"नमस्ते {display_name} जी। आपने इस आर्डर में अब तक {user['done']} स्कूल यूनिफॉर्म सफलतापूर्वक तैयार किए हैं। प्रति यूनिफॉर्म {user['wage_rate']} रुपये की दर से आपकी कुल सकल आय {int(gross_val)} रुपये है। अग्रिम कटौती {int(user['advance'])} रुपये है। आपके बैंक खाते में जमा होने वाली शुद्ध राशि {int(net_val)} रुपये है। यह सूची समूह की मंजूरी के लिए प्रतीक्षारत है।"
        else: # en
            speech_text = f"Hello {display_name}. You have successfully completed {user['done']} school uniforms for this order. At the approved piece rate of {user['wage_rate']} rupees each, your gross earnings are {int(gross_val)} rupees. Your advance deduction is {int(user['advance'])} rupees. The net amount payable to your bank account is {int(net_val)} rupees. This statement is awaiting group quorum authorization."
            
        bcp47_tag = TRANSLATIONS.get(cur_lang, {}).get("lang_tag", "en-IN")
        
        st.markdown(f"""
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 14px; padding: 18px; margin-bottom: 14px; box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);">
            <p style="margin: 0; font-size: 13.5px; color: #a7f3d0; line-height: 1.6;">
                <i>"{speech_text}"</i>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        audio_html = f"""
        <div style="text-align: center;">
            <button onclick="speakPassbook()" style="
                background: linear-gradient(135deg, #059669 0%, #10b981 100%);
                color: white;
                border: none;
                border-radius: 14px;
                padding: 16px 28px;
                font-size: 15px;
                font-weight: 800;
                cursor: pointer;
                box-shadow: 0 4px 18px rgba(16, 185, 129, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2);
                width: 100%;
            ">
                {t("audio_btn_text")}
            </button>
        </div>
        <script>
        function speakPassbook() {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                var msg = new SpeechSynthesisUtterance();
                msg.text = "{speech_text}";
                msg.lang = '{bcp47_tag}';
                msg.rate = 0.9;
                window.speechSynthesis.speak(msg);
            }} else {{
                alert('Web Speech API is not supported in this browser.');
            }}
        }}
        </script>
        """
        st.components.v1.html(audio_html, height=75)
        
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
        if not user["disputed"]:
            if st.button(t("dispute_btn_text"), use_container_width=True):
                user["disputed"] = True
                st.warning(t("dispute_raised_msg"))
                st.rerun()
        else:
            st.error("⚠️ Dispute Active: Frozen in review.")
            if st.button(t("withdraw_dispute_btn"), use_container_width=True):
                user["disputed"] = False
                st.rerun()
                
    st.markdown("---")
    
    # 4. Quorum Vote
    st.markdown(f"### {t('quorum_vote_title')}")
    current_vote = st.session_state.quorum_votes.get(user["id"], "PENDING")
    
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        if st.button(t("vote_approve_btn"), type="primary", use_container_width=True):
            st.session_state.quorum_votes[user["id"]] = "APPROVED"
            st.toast(t("vote_cast_toast"), icon="👍")
            st.rerun()
    with v_col2:
        if st.button(t("vote_object_btn"), use_container_width=True):
            st.session_state.quorum_votes[user["id"]] = "OBJECTED"
            st.toast("Objected!", icon="❌")
            st.rerun()
            
    st.caption(t("current_vote_caption", status=current_vote))


# -----------------------------------------------------------------------------
# 9. MAIN ENTRY POINT
# -----------------------------------------------------------------------------
def main():
    if not st.session_state.logged_in:
        render_login_screen()
    else:
        render_header()
        if st.session_state.user_role == "Leader":
            render_leader_dashboard()
        else:
            render_artisan_dashboard()

if __name__ == "__main__":
    main()
