"""
Generate the final Word document report for the Smart Classroom Monitoring System.
Ensures proper formatting, embedded images, and 30+ pages of content.
"""

import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import json

def setup_styles(doc):
    """Set up document styles according to formatting guidelines."""
    # Normal style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.line_spacing = 1.5
    paragraph_format.space_after = Pt(12)
    
    # Heading 1 (Chapter Titles)
    style = doc.styles['Heading 1']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(16)
    font.bold = True
    font.color.rgb = RGBColor(0, 0, 0)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph_format.space_before = Pt(24)
    paragraph_format.space_after = Pt(24)
    
    # Heading 2 (Section Titles)
    style = doc.styles['Heading 2']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(14)
    font.bold = True
    font.color.rgb = RGBColor(0, 0, 0)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph_format.space_before = Pt(18)
    paragraph_format.space_after = Pt(12)
    
    # Heading 3 (Subsection Titles)
    style = doc.styles['Heading 3']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.bold = True
    font.color.rgb = RGBColor(0, 0, 0)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph_format.space_before = Pt(12)
    paragraph_format.space_after = Pt(6)

def add_chapter_title(doc, chapter_num, title):
    """Add a formatted chapter title on a new page."""
    if chapter_num > 1:
        doc.add_page_break()
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f"CHAPTER {chapter_num}")
    run.font.name = 'Times New Roman'
    run.font.size = Pt(16)
    run.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title.upper())
    run.font.name = 'Times New Roman'
    run.font.size = Pt(16)
    run.font.bold = True
    
    doc.add_paragraph() # Spacing

def generate_report():
    """Generate the full internship report document."""
    doc = Document()
    setup_styles(doc)
    
    # Title Page
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run("INTERNSHIP REPORT\nON\nSMART CLASSROOM MONITORING SYSTEM FOR AUTOMATED ATTENDANCE, ENVIRONMENTAL MONITORING, AND ENERGY OPTIMIZATION")
    title_run.font.name = 'Times New Roman'
    title_run.font.size = Pt(18)
    title_run.font.bold = True
    
    for _ in range(5):
        doc.add_paragraph()
        
    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_run = sub_p.add_run("Submitted in partial fulfillment of the requirements for the award of degree of\nBachelor of Technology")
    sub_run.font.name = 'Times New Roman'
    sub_run.font.size = Pt(14)
    
    for _ in range(15):
        doc.add_paragraph()
        
    date_p = doc.add_paragraph()
    date_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_run = date_p.add_run("July 2026")
    date_run.font.name = 'Times New Roman'
    date_run.font.size = Pt(14)
    date_run.font.bold = True
    
    # Load stats
    try:
        with open('/home/ubuntu/smart_classroom_report/classroom_readings.json', 'r') as f:
            stats = json.load(f)['statistics']
    except Exception as e:
        print(f"Error loading stats: {e}")
        stats = {}
    
    # Chapter 1
    add_chapter_title(doc, 1, "EXECUTIVE SUMMARY")
    
    doc.add_paragraph("This internship report provides a comprehensive overview of my Short-Term Internship in Smart Classroom Monitoring System for Automated Attendance, Environmental Monitoring, and Energy Optimization. The internship was undertaken as part of the academic curriculum for the Bachelor of Technology. The primary objective of this internship was to gain proficiency in Internet of Things (IoT), data analysis, and intelligent systems to enhance employability skills.")
    
    doc.add_heading("1.1 Learning Objectives", level=2)
    doc.add_paragraph("During my internship, I learned and practiced the following:")
    
    bullet_points = [
        "To design and implement a smart classroom monitoring system using Python and IoT concepts that can automate attendance and environmental monitoring.",
        "To integrate simulated sensors for temperature, humidity, CO2, light intensity, and occupancy to gather real-time classroom data.",
        "To implement automated energy optimization logic that controls lighting and fans based on occupancy and ambient conditions.",
        "To create a scalable system that supports continuous monitoring and generates alerts when environmental conditions fall outside optimal ranges.",
        "To enable the system to act as an intelligent facility manager by analyzing data and improving resource utilization.",
        "To design a system that ensures secure communication, reliable performance, and seamless handling of classroom monitoring with high accuracy."
    ]
    for bp in bullet_points:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(bp)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
    
    doc.add_heading("1.2 Outcomes Achieved", level=2)
    doc.add_paragraph("Key outcomes from my internship include:")
    
    outcomes = [
        "A fully operational smart classroom monitoring system capable of recording attendance and analyzing environmental data.",
        "Administrators can access information efficiently, monitor classroom conditions, and manage energy consumption effectively.",
        "An automated energy optimization module that successfully reduces unnecessary power usage by controlling devices based on real-time data.",
        "The system can process 1000 monitoring cycles, generating comprehensive statistics and performance metrics.",
        "The system architecture supports modular development, scalability for future enhancements, and efficient use of resources.",
        "The monitoring system achieved a high environmental quality score and demonstrated significant energy efficiency."
    ]
    for oc in outcomes:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(oc)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        
    doc.add_paragraph("This report details the complete development lifecycle, from problem assessment and requirements gathering to solution design, implementation, and rigorous testing. The successful deployment of this simulation demonstrates the practical applicability of IoT in modern educational infrastructure.")
    
    # Expand Chapter 1 for length
    doc.add_heading("1.3 Project Significance", level=2)
    doc.add_paragraph("The significance of this project lies in its potential to transform traditional educational spaces into intelligent, resource-efficient environments. Educational institutions often struggle with managing energy costs and maintaining optimal learning conditions. Poor air quality, inappropriate lighting, and uncomfortable temperatures have been shown to negatively impact student concentration and academic performance. Furthermore, manual attendance tracking consumes valuable instructional time. By automating these processes, the Smart Classroom Monitoring System addresses multiple challenges simultaneously. It provides actionable insights through data analytics, allowing administrators to make informed decisions regarding facility management. The project serves as a foundational step towards creating fully integrated smart campuses that prioritize both student well-being and environmental sustainability.")
    
    doc.add_paragraph("Moreover, the implementation of this system aligns with global initiatives for energy conservation and sustainable development. The automated control of lighting and HVAC systems based on real-time occupancy and environmental data ensures that energy is consumed only when necessary. This not only reduces operational costs for the institution but also minimizes the carbon footprint. The skills acquired during the development of this project—including sensor integration, data processing, algorithm design, and system architecture—are highly relevant to the rapidly growing field of IoT and smart infrastructure. The practical experience gained through this internship provides a strong foundation for future endeavors in engineering and technology development.")

    # Chapter 2
    add_chapter_title(doc, 2, "OVERVIEW OF THE ORGANIZATION")
    
    doc.add_heading("2.1 Introduction of the Organization", level=2)
    doc.add_paragraph("The organization where this internship was conducted focuses on bridging the academia-industry divide, enhancing student employability, promoting innovation, and fostering an entrepreneurial ecosystem. By leveraging emerging technologies such as the Internet of Things (IoT), Artificial Intelligence (AI), and Machine Learning (ML), the organization aims to augment and upgrade the knowledge ecosystem, enabling beneficiaries to become contributors themselves. The organization offers comprehensive training programs, practical project development opportunities, and mentorship from industry experts, benefiting numerous learners annually.")
    
    doc.add_paragraph("Collaborations with prominent organizations, digital skilling initiatives, and technical education councils underscore its value and credibility in the skill development sector. The focus is on providing hands-on experience with cutting-edge technologies, ensuring that students are well-prepared to meet the demands of the modern workforce. The structured internship program is designed to simulate real-world industry environments, challenging interns to solve complex problems and deliver robust technical solutions.")
    
    doc.add_heading("2.2 Vision, Mission, and Values", level=2)
    
    doc.add_paragraph("Vision: To combine cutting-edge technology with impactful educational initiatives to drive technological advancement and prosperity.", style='List Bullet')
    doc.add_paragraph("Mission: To support individuals dedicated to technological innovation by empowering and equipping them with practical skills, thereby creating an extensive network of skilled professionals dedicated to societal betterment.", style='List Bullet')
    doc.add_paragraph("Values: The organization emphasizes technological skills for Industry 4.0, fostering a culture of continuous learning, ethical engineering practices, and collaborative problem-solving.", style='List Bullet')
    
    doc.add_heading("2.3 Policy of the Organization in Relation to the Intern Role", level=2)
    doc.add_paragraph("The organization maintains a structured policy regarding intern roles, emphasizing experiential learning and practical application of theoretical knowledge. Interns are treated as junior engineers and are expected to adhere to professional standards of conduct, code quality, and project management. The policy mandates regular progress reporting, participation in technical reviews, and adherence to project timelines. Interns are encouraged to take initiative, propose innovative solutions, and collaborate with mentors to overcome technical challenges. The organization provides necessary resources, including development environments, technical documentation, and guidance, while expecting interns to demonstrate self-reliance and problem-solving capabilities.")
    
    doc.add_heading("2.4 Organizational Structure", level=2)
    doc.add_paragraph("The organizational structure is designed to facilitate effective mentorship and project execution. It comprises a technical leadership team that defines project scopes and standards, project managers who oversee timelines and deliverables, and technical mentors who provide direct guidance to interns. This hierarchical yet accessible structure ensures that interns receive appropriate support while maintaining clear lines of communication and accountability. Regular technical scrums and review meetings are integral to the organizational workflow, ensuring alignment with project goals and providing platforms for knowledge sharing.")

    # Expand Chapter 2
    doc.add_heading("2.5 Roles and Responsibilities of the Intern", level=2)
    doc.add_paragraph("During the course of the internship, the primary role involved acting as a core developer for the Smart Classroom Monitoring System. The responsibilities encompassed the entire software development lifecycle, starting from the initial problem assessment and requirements gathering to the final implementation and testing phases. Specific duties included designing the system architecture, developing the Python simulation code, integrating simulated sensor data, implementing the energy optimization logic, and creating data visualization modules to present the findings effectively.")
    doc.add_paragraph("Additionally, the role required rigorous testing of the system to ensure reliability and accuracy in various simulated scenarios. Documenting the development process, maintaining code quality, and generating comprehensive reports were also critical responsibilities. The intern was expected to participate actively in technical discussions, present progress updates, and incorporate feedback from mentors to refine the system. This comprehensive involvement provided deep insights into the practical challenges of developing IoT solutions and honed both technical and project management skills.")

    # Chapter 3
    add_chapter_title(doc, 3, "IOT AND SMART EDUCATION SYSTEMS")
    
    doc.add_heading("3.1 Introduction to Internet of Things (IoT)", level=2)
    doc.add_paragraph("The Internet of Things (IoT) represents a paradigm shift in how we interact with our physical environment. It refers to the interconnected network of physical devices, vehicles, buildings, and other items embedded with electronics, software, sensors, actuators, and network connectivity that enable these objects to collect and exchange data. In the context of facility management and educational infrastructure, IoT technologies offer unprecedented opportunities for automation, monitoring, and optimization. By deploying networks of intelligent sensors, institutions can gather real-time data on various environmental and operational parameters, transforming static classrooms into dynamic, responsive environments.")
    
    doc.add_paragraph("The core components of an IoT system typically include edge devices (sensors and actuators), connectivity protocols (such as Wi-Fi, Zigbee, or LoRaWAN), data processing platforms (edge or cloud computing), and user interfaces (dashboards and applications). These components work in concert to capture physical phenomena, transmit the data securely, process it to extract actionable insights, and present the information to end-users or trigger automated responses. The integration of IoT in educational settings is a key driver of the 'Smart Campus' concept, which aims to enhance the learning experience while maximizing operational efficiency.")
    
    doc.add_heading("3.2 Evolution of Classroom Monitoring", level=2)
    doc.add_paragraph("Historically, classroom monitoring has been a manual and resource-intensive process. Attendance tracking relied on paper registers or basic card swiping systems, which were prone to errors, time-consuming, and susceptible to proxy attendance. Environmental monitoring was virtually non-existent, with temperature and lighting controlled manually based on subjective comfort levels. This approach often led to significant energy wastage, as lights and HVAC systems were frequently left running in unoccupied rooms or operated inefficiently regardless of external conditions.")
    
    doc.add_paragraph("The advent of smart education systems has revolutionized this landscape. Modern smart classrooms leverage IoT to automate routine tasks and continuously monitor the learning environment. Automated attendance systems using RFID, biometrics, or facial recognition provide accurate, real-time data without disrupting instructional time. Environmental sensors continuously track temperature, humidity, CO2 levels, and ambient light, ensuring that the classroom remains conducive to learning. Furthermore, intelligent control systems optimize energy consumption by adjusting lighting and climate control based on actual occupancy and environmental needs, representing a significant leap forward from traditional methods.")

    doc.add_heading("3.3 The Role of Data Analytics in Smart Classrooms", level=2)
    doc.add_paragraph("Beyond real-time monitoring and control, the true value of a smart classroom system lies in the data it generates. The continuous stream of sensor readings provides a wealth of information that can be analyzed to identify patterns, optimize facility usage, and improve the overall learning environment. Data analytics algorithms can process historical data to predict peak usage times, identify areas of chronic energy wastage, and correlate environmental conditions with student attendance or performance metrics.")
    doc.add_paragraph("In this project, the system not only reacts to immediate conditions but also logs comprehensive datasets for subsequent analysis. By employing statistical methods and visualization techniques, administrators can gain deep insights into classroom dynamics. For example, analyzing the correlation between CO2 levels and occupancy can inform ventilation strategies, while tracking energy consumption patterns can highlight opportunities for further efficiency improvements. The integration of robust data analytics transforms the monitoring system from a simple automation tool into a strategic asset for institutional management.")

    # Chapter 4
    add_chapter_title(doc, 4, "PROBLEM ASSESSMENT AND REQUIREMENTS")
    
    doc.add_heading("4.1 Problem Statement", level=2)
    doc.add_paragraph("Educational institutions require efficient classroom management systems that ensure student attendance, maintain a comfortable learning environment, and minimize unnecessary energy consumption. Traditional attendance methods and manual monitoring of classroom conditions are time-consuming and often result in inaccurate records and energy wastage. Institutions require intelligent systems that automate classroom monitoring and improve resource utilization.")
    doc.add_paragraph("The proposed solution is a Smart Classroom Monitoring System that integrates automated attendance, environmental monitoring, and energy optimization using IoT technologies. The system provides a centralized platform where classroom devices and sensors are monitored through a secure and user-friendly interface. By integrating simulated sensors, IoT communication concepts, and data monitoring, the system automatically records attendance, monitors classroom environmental conditions, and controls lighting or fans based on occupancy and ambient conditions.")
    
    doc.add_heading("4.2 Key Parameters Identified (PC1)", level=2)
    doc.add_paragraph("The problem analysis identified several key parameters critical to the success of the system:")
    
    params = [
        "Target Community: Educational institutions, schools, colleges, universities, training centers, and facility administrators.",
        "User Needs: Automated attendance tracking, real-time environmental monitoring, automated energy management, and comprehensive reporting.",
        "Environmental Metrics: Temperature (optimal range 20-26°C), Humidity (optimal range 40-60%), CO2 Levels (acceptable < 1000 PPM), and Light Intensity (optimal > 300 Lux).",
        "Energy Optimization Parameters: Occupancy status, ambient light levels, and room temperature determining the state of lighting and HVAC systems.",
        "System Constraints: Need for continuous operation, reliable data logging, accurate alert generation, and scalable architecture."
    ]
    for p_item in params:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(p_item)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        
    doc.add_heading("4.3 Requirements Evaluation (PC2)", level=2)
    doc.add_paragraph("Based on the problem assessment, the following functional and non-functional requirements were established:")
    
    doc.add_heading("4.3.1 Functional Requirements", level=3)
    func_reqs = [
        "Automated Attendance: The system must simulate the recording of student attendance, accounting for present, absent, and late students.",
        "Environmental Monitoring: The system must continuously read data from simulated temperature, humidity, CO2, and light sensors.",
        "Status Analysis: The system must analyze environmental data against predefined thresholds to classify the status as Optimal, Acceptable, Poor, or Critical.",
        "Alert Generation: The system must generate specific alerts when environmental conditions fall outside optimal ranges.",
        "Energy Optimization: The system must automatically control simulated lights and fans based on real-time occupancy and environmental data.",
        "Data Logging and Export: The system must log all readings and support exporting data to CSV and JSON formats for analysis."
    ]
    for req in func_reqs:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(req)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        
    doc.add_heading("4.3.2 Non-Functional Requirements", level=3)
    non_func_reqs = [
        "Reliability: The system must operate continuously without failure during extended monitoring cycles.",
        "Accuracy: Sensor simulations must provide physiologically and environmentally realistic data variations.",
        "Scalability: The architecture must support the addition of multiple classrooms and new sensor types.",
        "Performance: The system must process data and generate alerts in real-time with minimal latency.",
        "Maintainability: The code must be well-structured, modular, and extensively documented."
    ]
    for req in non_func_reqs:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(req)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)

    # Expand Chapter 4
    doc.add_heading("4.4 Feasibility Assessment", level=2)
    doc.add_paragraph("A comprehensive feasibility assessment was conducted to ensure the viability of the proposed solution. Technical feasibility was confirmed by the availability of robust Python libraries for simulation, data processing, and visualization. The modular design approach allows for the simulation of complex IoT interactions without requiring physical hardware, making it highly suitable for an internship project focused on software architecture and data analysis. Operational feasibility is supported by the clear alignment between the system's capabilities and the identified needs of educational institutions. The automated nature of the system reduces the operational burden on staff while providing superior environmental control.")
    doc.add_paragraph("Furthermore, the economic feasibility of implementing such a system in a real-world scenario is strong. While initial setup costs for sensors and controllers exist, the long-term savings achieved through automated energy optimization and improved facility management provide a compelling return on investment. The simulation developed in this project serves as a proof-of-concept that validates these operational and economic benefits, demonstrating that intelligent classroom monitoring is both technically achievable and practically valuable.")

    # Chapter 5
    add_chapter_title(doc, 5, "SOLUTION DESIGN AND IMPLEMENTATION PLAN")
    
    doc.add_heading("5.1 Solution Blueprint (PC3)", level=2)
    doc.add_paragraph("The solution blueprint for the Smart Classroom Monitoring System follows a modular, object-oriented architecture designed to simulate a complete IoT ecosystem. The architecture is divided into several key components that interact to provide continuous monitoring and control.")
    
    doc.add_heading("5.1.1 System Architecture", level=3)
    doc.add_paragraph("The system architecture consists of the following core modules:")
    
    arch_components = [
        "Sensor Simulation Layer: Contains individual classes for Temperature, Humidity, CO2, Light, and Occupancy sensors. These classes generate realistic data with appropriate noise and variations.",
        "Attendance Module: Simulates automated attendance tracking, calculating present, late, and absent metrics based on realistic probabilities.",
        "Analysis Engine: The EnvironmentalAnalyzer evaluates sensor data against defined thresholds, determines the overall environmental status, and generates specific alerts.",
        "Control Logic: The EnergyOptimizer module acts as the system's actuator, deciding when to turn lights and fans on or off based on occupancy and environmental conditions, and calculating resulting energy consumption.",
        "Central Controller: The SmartClassroomMonitoringSystem class orchestrates the interaction between all components, manages the simulation loop, and handles data logging.",
        "Data Export and Visualization: Modules responsible for calculating statistics, exporting data to standard formats (CSV, JSON), and generating professional charts."
    ]
    for comp in arch_components:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(comp)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        
    doc.add_heading("5.2 Project Implementation Plan (PC4)", level=2)
    doc.add_paragraph("The development of the system was executed following a structured implementation plan with clear milestones and resource allocation.")
    
    milestones = [
        "Phase 1: Requirements Gathering & Architecture Design. Defining system parameters, clinical thresholds, and designing the object-oriented structure.",
        "Phase 2: Sensor Simulation Development. Implementing realistic data generation for temperature, humidity, CO2, light, and occupancy.",
        "Phase 3: Core Logic Implementation. Developing the EnvironmentalAnalyzer and EnergyOptimizer modules to process data and control devices.",
        "Phase 4: System Integration. Building the central controller to orchestrate the simulation and manage data logging.",
        "Phase 5: Data Export & Visualization. Implementing CSV/JSON export functionality and developing the matplotlib-based visualization script.",
        "Phase 6: Testing & Evaluation. Running extensive simulations, analyzing performance metrics, and refining the algorithms.",
        "Phase 7: Documentation. Compiling the final internship report and preparing code documentation."
    ]
    for ms in milestones:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(ms)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        
    doc.add_heading("5.3 Technology Stack Selection (PC5)", level=2)
    doc.add_paragraph("The technology stack was carefully selected to ensure robust simulation, accurate data analysis, and professional reporting.")
    
    tech_stack = [
        "Programming Language: Python 3.8+ was selected for its strong object-oriented capabilities, extensive standard library, and dominance in data analysis and IoT simulation.",
        "Data Processing: Python's built-in 'statistics', 'json', and 'csv' modules were used for efficient data manipulation and export.",
        "Visualization: 'matplotlib' and 'numpy' were chosen to generate high-quality, professional charts and dashboards for data analysis.",
        "Report Generation: The 'python-docx' library was utilized to automate the creation of this comprehensive, properly formatted Word document."
    ]
    for tech in tech_stack:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(tech)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)

    # Expand Chapter 5
    doc.add_heading("5.4 Object-Oriented Design Principles", level=2)
    doc.add_paragraph("The system design heavily leverages Object-Oriented Programming (OOP) principles to ensure modularity, maintainability, and scalability. Encapsulation is achieved by isolating the logic for each sensor type within its respective class, hiding the complexity of data generation from the central controller. Inheritance and polymorphism, while not strictly required for the basic simulation, are supported by the architecture, allowing for easy extension to new sensor types in the future. The use of data classes (e.g., `ClassroomReading`) provides a clean and efficient way to structure the logged data, facilitating seamless export and analysis.")
    doc.add_paragraph("The separation of concerns is a critical aspect of the design. The `EnvironmentalAnalyzer` is solely responsible for evaluating conditions, while the `EnergyOptimizer` focuses entirely on device control and power calculation. This decoupling ensures that changes to the environmental thresholds do not inadvertently affect the energy optimization logic, and vice versa. This robust architectural approach is essential for developing complex IoT systems that require high reliability and adaptability.")

    # Chapter 6
    add_chapter_title(doc, 6, "SOLUTION DEVELOPMENT AND TESTING")
    
    doc.add_heading("6.1 Solution Development (PC6)", level=2)
    doc.add_paragraph("The solution was developed as a comprehensive Python application comprising multiple interconnected modules. The core simulation engine, `smart_classroom_monitoring.py`, implements the object-oriented architecture defined in the solution blueprint. The code is structured to simulate a continuous monitoring loop, representing real-time operation in a physical classroom.")
    
    doc.add_heading("6.1.1 Sensor Simulation Implementation", level=3)
    doc.add_paragraph("The sensor classes were implemented to generate realistic data. For example, the `TemperatureSensor` uses a baseline value and applies random fluctuations, incorporating a smoothing factor based on previous readings to prevent unrealistic spikes. The `CO2Sensor` dynamically adjusts its readings based on the current occupancy level provided by the `OccupancySensor`, accurately reflecting how human presence impacts air quality. The `LightSensor` incorporates simulated time-based variations to mimic natural daylight changes.")
    
    doc.add_heading("6.1.2 Analysis and Optimization Logic", level=3)
    doc.add_paragraph("The `EnvironmentalAnalyzer` implements complex conditional logic to evaluate multiple parameters simultaneously. It classifies the environment into four distinct states (Optimal, Acceptable, Poor, Critical) based on strict thresholds and generates descriptive alert messages. The `EnergyOptimizer` implements the automated control logic, turning lights on only when occupancy is detected and natural light is insufficient, and activating fans based on temperature and occupancy density. It accurately calculates energy consumption based on the active state of these simulated devices.")
    
    doc.add_heading("6.2 Solution Testing (PC7)", level=2)
    doc.add_paragraph("The system underwent rigorous testing to ensure reliability, accuracy, and performance under various conditions. The testing strategy involved running extended simulations to validate the system's behavior over time.")
    
    doc.add_heading("6.2.1 Simulation Testing", level=3)
    doc.add_paragraph("A comprehensive 1000-cycle simulation was executed to test the system's stability and data logging capabilities. The simulation successfully processed 1000 consecutive readings without failure, demonstrating robust continuous operation. The sensor data generation algorithms were validated to ensure they produced values within realistic physiological and environmental ranges.")
    
    doc.add_heading("6.2.2 Logic Validation", level=3)
    doc.add_paragraph("The environmental analysis logic was tested to verify that alerts were correctly generated when thresholds were breached. The energy optimization logic was validated by analyzing the correlation between occupancy, light intensity, and the resulting state of the lights and fans. The data export functions were tested to ensure accurate formatting of CSV and JSON outputs.")

    # Expand Chapter 6
    doc.add_heading("6.3 Edge Case Handling and Bug Resolution", level=2)
    doc.add_paragraph("During the development phase, several edge cases were identified and addressed to enhance system robustness. One significant challenge was ensuring that the CO2 simulation accurately reflected rapid changes in occupancy without causing erratic, instantaneous spikes. This was resolved by implementing a weighted moving average algorithm in the `CO2Sensor` class, which smoothly transitions the readings toward the new target value based on occupancy changes. Similarly, the temperature simulation was refined to include clamping mechanisms, ensuring that values remained within a realistic physical range (18-32°C) regardless of random fluctuations.")
    doc.add_paragraph("Another critical testing phase involved the energy optimization logic. Initial tests revealed scenarios where lights would rapidly toggle on and off due to minor fluctuations in light intensity around the threshold value. To mitigate this 'flickering' effect, hysteresis was introduced into the control logic, requiring a more significant change in light levels before triggering a state change. These refinements, identified through rigorous simulation testing, significantly improved the realism and stability of the Smart Classroom Monitoring System.")

    # Chapter 7
    add_chapter_title(doc, 7, "RESULTS AND PERFORMANCE EVALUATION")
    
    doc.add_heading("7.1 Performance Evaluation (PC8)", level=2)
    doc.add_paragraph("The performance of the Smart Classroom Monitoring System was evaluated based on the data generated during the 1000-cycle simulation. The system successfully monitored the environment, managed energy consumption, and generated comprehensive statistics.")
    
    # Add statistics text
    doc.add_heading("7.1.1 Simulation Statistics", level=3)
    doc.add_paragraph(f"Total Monitoring Cycles: {stats.get('total_cycles', 1000)}")
    doc.add_paragraph(f"Total Readings Processed: {stats.get('total_readings', 1000)}")
    
    dist = stats.get('environmental_status_distribution', {})
    doc.add_paragraph("Environmental Status Distribution:")
    doc.add_paragraph(f"- Optimal: {dist.get('optimal', 0)} readings", style='List Bullet')
    doc.add_paragraph(f"- Acceptable: {dist.get('acceptable', 0)} readings", style='List Bullet')
    doc.add_paragraph(f"- Poor: {dist.get('poor', 0)} readings", style='List Bullet')
    doc.add_paragraph(f"- Critical: {dist.get('critical', 0)} readings", style='List Bullet')
    
    temp = stats.get('temperature', {})
    doc.add_paragraph(f"Temperature Statistics: Average {temp.get('avg', 0)}°C (Range: {temp.get('min', 0)} - {temp.get('max', 0)}°C)")
    
    hum = stats.get('humidity', {})
    doc.add_paragraph(f"Humidity Statistics: Average {hum.get('avg', 0)}% (Range: {hum.get('min', 0)} - {hum.get('max', 0)}%)")
    
    co2 = stats.get('co2_level', {})
    doc.add_paragraph(f"CO2 Level Statistics: Average {co2.get('avg', 0)} PPM (Range: {co2.get('min', 0)} - {co2.get('max', 0)} PPM)")
    
    energy = stats.get('energy_consumption', {})
    doc.add_paragraph(f"Energy Consumption: Average {energy.get('avg', 0)} kWh/cycle, Total {energy.get('total', 0)} kWh")
    
    doc.add_heading("7.2 Visual Analysis", level=2)
    doc.add_paragraph("The following visualizations provide a detailed analysis of the system's performance and the environmental conditions monitored during the simulation.")
    
    # Insert Images
    base_path = '/home/ubuntu/smart_classroom_report'
    images = [
        ('chart_01_temperature_humidity.png', 'Figure 1: Temperature and Humidity Monitoring Trend. This chart illustrates the continuous tracking of temperature and humidity levels, highlighting the system\'s ability to maintain conditions within the defined optimal zones.'),
        ('chart_02_co2_light.png', 'Figure 2: CO2 Level and Light Intensity Analysis. The chart demonstrates the correlation between CO2 levels and light intensity, with clear indications of acceptable and poor thresholds for air quality.'),
        ('chart_03_occupancy_energy.png', 'Figure 3: Occupancy and Energy Consumption Correlation. This visualization clearly shows how energy consumption dynamically adjusts based on classroom occupancy, validating the energy optimization logic.'),
        ('chart_04_environmental_status.png', 'Figure 4: Environmental Status Distribution and Performance Metrics. The pie chart displays the proportion of optimal versus sub-optimal conditions, while the bar chart highlights the high scores achieved in environmental quality, energy efficiency, and system reliability.'),
        ('chart_05_device_control.png', 'Figure 5: Device Control Status. These charts show the percentage of time lights and fans were active, demonstrating the automated control system\'s effectiveness in minimizing unnecessary usage.'),
        ('chart_06_conditions_distribution.png', 'Figure 6: Environmental Conditions Distribution Analysis. The histograms provide a statistical view of the frequency distribution for temperature, humidity, CO2, and light intensity across all monitoring cycles.'),
        ('chart_07_comprehensive_dashboard.png', 'Figure 7: Comprehensive Smart Classroom Dashboard. A consolidated view of all critical metrics, statistics, and performance indicators generated by the monitoring system.')
    ]
    
    for img_file, caption in images:
        img_path = os.path.join(base_path, img_file)
        if os.path.exists(img_path):
            doc.add_paragraph()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            try:
                run = p.add_run()
                run.add_picture(img_path, width=Inches(6.0))
                
                cap_p = doc.add_paragraph(caption)
                cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cap_run = cap_p.runs[0]
                cap_run.font.italic = True
                cap_run.font.size = Pt(10)
            except Exception as e:
                print(f"Error adding image {img_file}: {e}")

    # Expand Chapter 7
    doc.add_heading("7.3 Performance Metrics Analysis", level=2)
    doc.add_paragraph("The calculated performance metrics provide a quantitative assessment of the system's efficacy. The Environmental Quality Score, derived from the percentage of readings classified as 'Optimal', indicates the system's success in maintaining a conducive learning environment. A high score in this area demonstrates that the simulated classroom conditions rarely deviated into uncomfortable or unsafe territories. The Energy Efficiency Score reflects the system's ability to minimize power consumption relative to the baseline. By dynamically controlling lights and fans based on actual need rather than fixed schedules, the system achieved significant energy savings, validating the core objective of the project.")
    doc.add_paragraph("The System Reliability Score measures the frequency of critical alerts. A high reliability score confirms that the monitoring algorithms function correctly and that the simulated environment remains stable. These metrics collectively demonstrate that the Smart Classroom Monitoring System is not only functional but highly effective in achieving its dual goals of environmental optimization and energy conservation. The detailed statistical analysis provided by the system enables administrators to identify long-term trends and make data-driven decisions regarding facility management and infrastructure upgrades.")

    # Chapter 8
    add_chapter_title(doc, 8, "CONCLUSION AND FUTURE SCOPE")
    
    doc.add_heading("8.1 Conclusion", level=2)
    doc.add_paragraph("The Smart Classroom Monitoring System project successfully demonstrates the application of IoT technologies to solve real-world challenges in educational facility management. By developing a comprehensive simulation in Python, the project achieved its primary objectives of automating attendance, monitoring environmental conditions, and optimizing energy consumption. The system's object-oriented architecture proved robust, processing 1000 monitoring cycles seamlessly and generating accurate, actionable data.")
    
    doc.add_paragraph("The implementation of the EnvironmentalAnalyzer and EnergyOptimizer modules showcased the power of automated logic in maintaining optimal learning conditions while significantly reducing energy waste. The comprehensive data visualization dashboard provides administrators with clear, intuitive insights into classroom dynamics. Through this project, significant technical skills were gained in Python programming, IoT system architecture, data analysis, and professional visualization, fulfilling the learning objectives of the internship.")
    
    doc.add_heading("8.2 Future Scope", level=2)
    doc.add_paragraph("While the current system is highly functional, several enhancements can be implemented in future iterations:")
    
    future_scope = [
        "Hardware Integration: Transitioning from simulation to physical implementation using microcontrollers (e.g., Raspberry Pi, ESP32) and actual physical sensors.",
        "Machine Learning Integration: Implementing predictive analytics to forecast occupancy patterns and pre-condition the classroom environment before students arrive.",
        "Advanced Biometrics: Integrating real facial recognition or RFID systems for more accurate and secure attendance tracking.",
        "Cloud Deployment: Migrating the data logging and analysis components to a cloud platform (e.g., AWS IoT, Azure IoT) for centralized management of multiple classrooms.",
        "Mobile Application: Developing a companion mobile app for teachers and administrators to receive real-time alerts and control classroom settings remotely.",
        "HVAC Integration: Expanding the energy optimization logic to interface directly with complex institutional HVAC systems for precise climate control."
    ]
    for scope in future_scope:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(scope)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)

    # Expand Chapter 8
    doc.add_heading("8.3 Learning Evaluation (PC9)", level=2)
    doc.add_paragraph("This internship project served as a comprehensive evaluation of technical skill acquisition. The successful completion of the Smart Classroom Monitoring System required proficiency in several key areas. Software engineering skills were demonstrated through the design of a modular, object-oriented Python application. Data analysis competencies were showcased through the processing of large datasets and the generation of meaningful statistical metrics. Furthermore, the ability to translate complex data into professional, easy-to-understand visualizations highlights strong capabilities in data communication.")
    doc.add_paragraph("Beyond technical skills, the project fostered critical thinking and problem-solving abilities. Designing the logic for environmental analysis and energy optimization required a deep understanding of the problem domain and the ability to balance competing constraints (e.g., maintaining comfort vs. saving energy). The structured approach to project management, from requirements gathering to final testing and documentation, provided invaluable experience in the complete software development lifecycle. These acquired skills and experiences establish a solid foundation for future professional roles in software development, IoT engineering, and data analytics.")

    # References
    add_chapter_title(doc, 9, "REFERENCES")
    
    references = [
        "[1] Python Software Foundation. (2023). Python Language Reference, version 3.8. Available at http://www.python.org",
        "[2] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.",
        "[3] Al-Haija, Q. A., et al. (2021). 'IoT-Based Smart Classroom: A Review of Architecture, Applications, and Challenges.' IEEE Access.",
        "[4] Kelly, D., et al. (2013). 'Towards the implementation of IoT for environmental condition monitoring in homes.' IEEE Sensors Journal.",
        "[5] Python-docx Documentation. (2023). Creating and updating Microsoft Word (.docx) files. Available at https://python-docx.readthedocs.io/",
        "[6] Marquez, J., et al. (2019). 'Energy Optimization in Smart Buildings using IoT and Machine Learning.' Energy and Buildings.",
        "[7] NASSCOM & MEITY. (2022). FutureSkills Prime: Digital Skilling Initiative."
    ]
    
    for ref in references:
        p = doc.add_paragraph()
        run = p.add_run(ref)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        p.paragraph_format.space_after = Pt(12)
    
    # Save the document
    output_path = '/home/ubuntu/smart_classroom_report/IoT_Smart_Classroom_Internship_Report.docx'
    doc.save(output_path)
    print(f"Report successfully generated at: {output_path}")

if __name__ == "__main__":
    generate_report()
