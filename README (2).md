# Smart Classroom Monitoring System

## Project Overview

This project implements a comprehensive **Smart Classroom Monitoring System** for automated attendance, environmental monitoring, and energy optimization using IoT technologies. The system provides real-time monitoring of classroom conditions, automatic control of lighting and ventilation systems, and comprehensive data analysis capabilities.

## Project Objectives

- Design and implement a smart classroom monitoring system using IoT concepts and Python
- Integrate multiple environmental sensors for continuous monitoring of classroom conditions
- Develop automated energy optimization logic for efficient resource utilization
- Create comprehensive data logging and analysis mechanisms
- Implement scalable system architecture for multi-classroom deployments
- Support early detection of environmental issues and enable proactive facility management

## System Features

### Core Monitoring Capabilities
- **Automated Attendance**: Simulates realistic attendance recording with present, absent, and late classifications
- **Temperature Monitoring**: Continuous tracking with optimal range 20-26°C
- **Humidity Monitoring**: Real-time humidity levels with optimal range 40-60%
- **CO2 Level Monitoring**: Air quality tracking with acceptable threshold at 1000 PPM
- **Light Intensity Monitoring**: Ambient light measurement with optimal threshold at 300 Lux
- **Occupancy Sensing**: Real-time detection of classroom occupancy

### Environmental Status Classification
- **OPTIMAL**: All vital parameters within safe operating ranges
- **ACCEPTABLE**: Minor deviation from baseline, requires monitoring
- **POOR**: Significant deviation, corrective action recommended
- **CRITICAL**: Severe condition, immediate intervention required

### System Components
- **AttendanceRecorder**: Simulates student attendance tracking
- **TemperatureSensor**: Generates realistic temperature readings with variations
- **HumiditySensor**: Simulates humidity level changes
- **CO2Sensor**: Tracks air quality based on occupancy
- **LightSensor**: Monitors ambient light intensity
- **OccupancySensor**: Detects classroom occupancy
- **EnvironmentalAnalyzer**: Evaluates conditions and generates alerts
- **EnergyOptimizer**: Automatically controls lights and fans
- **SmartClassroomMonitoringSystem**: Central controller orchestrating all components

### Performance Metrics
- **Environmental Quality Score**: 99.7/100
- **Energy Efficiency Score**: 94.06/100
- **System Reliability Score**: 99.91/100

## Simulation Results

### Monitoring Statistics (1000 Cycles)
- **Total Readings**: 1000 continuous monitoring cycles
- **Average Temperature**: 24.03°C (Range: 21.3-26.4°C)
- **Average Humidity**: 49.99% (Range: 43.7-56.5%)
- **Average CO2**: 485 PPM (Range: 381-648 PPM)
- **Average Light**: 507.3 Lux (Range: 376.0-637.1 Lux)
- **Average Occupancy**: 17.68 students (Range: 0-50 students)

### Environmental Status Distribution
- **Optimal**: 997 readings (99.7%)
- **Acceptable**: 3 readings (0.3%)
- **Poor**: 0 readings (0.0%)
- **Critical**: 0 readings (0.0%)
- **Total Alert Events**: 3 (0.3%)

### Energy Consumption
- **Average**: 0.059 kWh per cycle
- **Range**: 0.05 - 0.2 kWh
- **Total**: 59.45 kWh for 1000 cycles

## File Structure

```
smart_classroom_report/
├── smart_classroom_monitoring.py      # Main simulation engine (600+ lines)
├── generate_visualizations.py         # Chart generation script (500+ lines)
├── generate_report.py                 # Word document generator (400+ lines)
├── classroom_readings.csv             # Simulation data (CSV format)
├── classroom_readings.json            # Simulation data (JSON format)
├── environmental_alerts.csv           # Alert event log
├── chart_01_temperature_humidity.png  # Visualization
├── chart_02_co2_light.png             # Visualization
├── chart_03_occupancy_energy.png      # Visualization
├── chart_04_environmental_status.png  # Visualization
├── chart_05_device_control.png        # Visualization
├── chart_06_conditions_distribution.png # Visualization
├── chart_07_comprehensive_dashboard.png # Visualization
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
└── IoT_Smart_Classroom_Internship_Report.docx # Final report (30+ pages)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Extract the project files**:
   ```bash
   unzip iot_smart_classroom_code.zip
   cd smart_classroom_report
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install python-docx matplotlib numpy
   ```

## Usage

### Run the Complete Simulation

Execute the main simulation to generate classroom monitoring data:
```bash
python3 smart_classroom_monitoring.py
```

This will:
- Run 1000 monitoring cycles
- Generate 1000 environmental readings
- Create attendance records
- Generate environmental alerts
- Export data to CSV and JSON formats
- Display comprehensive statistics

### Generate Visualizations

Create professional charts from the simulation data:
```bash
python3 generate_visualizations.py
```

This will generate 7 high-resolution visualization files:
1. Temperature and Humidity Trend Chart
2. CO2 Level and Light Intensity Chart
3. Occupancy and Energy Consumption Chart
4. Environmental Status Distribution
5. Device Control Status (Lights and Fans)
6. Environmental Conditions Distribution Histograms
7. Comprehensive Classroom Monitoring Dashboard

### Generate the Report

Create the final Word document report:
```bash
python3 generate_report.py
```

This will generate `IoT_Smart_Classroom_Internship_Report.docx` containing:
- Executive Summary
- Organization Overview
- IoT and Smart Education Systems
- Problem Assessment and Requirements
- Solution Design and Implementation Plan
- Solution Development and Testing
- Results and Performance Evaluation
- Conclusion and Future Scope
- All 7 embedded visualizations
- References

## System Architecture

### Monitoring Loop
```
Read Sensors → Analyze Environment → Optimize Energy → Log Data → Export Results
```

### Data Flow
```
Sensors → EnvironmentalAnalyzer → EnergyOptimizer → Data Logger → Visualization
```

### Control Logic
```
Occupancy + Light Level → Lights Control
Occupancy + Temperature → Fan Control
```

## Environmental Thresholds

### Temperature (°C)
- Optimal: 20-26°C
- Acceptable: 18-28°C
- Poor: <18 or >28°C
- Critical: <18 or >28°C

### Humidity (%)
- Optimal: 40-60%
- Acceptable: 30-70%
- Poor: <30 or >70%
- Critical: <30 or >70%

### CO2 Level (PPM)
- Optimal: <1000 PPM
- Acceptable: 1000-1500 PPM
- Poor: >1500 PPM
- Critical: >1500 PPM

### Light Intensity (Lux)
- Optimal: >300 Lux
- Acceptable: 200-300 Lux
- Poor: <200 Lux

## Configuration

### Modifying Environmental Thresholds

Edit `smart_classroom_monitoring.py` to adjust alert thresholds:

```python
analyzer = EnvironmentalAnalyzer(
    temp_optimal_low=20.0,
    temp_optimal_high=26.0,
    humidity_optimal_low=40.0,
    humidity_optimal_high=60.0,
    co2_acceptable=1000,
    co2_poor=1500,
    light_optimal=300.0
)
```

### Adjusting Simulation Parameters

Modify the number of monitoring cycles:

```python
system = SmartClassroomMonitoringSystem(classroom_id="CLASSROOM_001", total_students=50)
readings = system.run_simulation(num_cycles=2000)  # Change cycle count
```

## Output Files

### Data Files
- **classroom_readings.csv**: All readings with timestamps and status
- **classroom_readings.json**: Complete simulation data with statistics and alert history
- **environmental_alerts.csv**: Detailed log of all generated environmental alerts

### Visualization Files
- **chart_*.png**: High-resolution (300 DPI) professional charts

### Report File
- **IoT_Smart_Classroom_Internship_Report.docx**: Comprehensive 30+ page internship report

## Performance Metrics Explained

### Environmental Quality Score (99.7/100)
Measures the percentage of time the classroom maintained optimal environmental conditions. Higher scores indicate better overall environmental management.

### Energy Efficiency Score (94.06/100)
Evaluates the system's ability to minimize energy consumption. Calculated based on average power usage per monitoring cycle.

### System Reliability Score (99.91/100)
Measures the frequency of environmental alerts. Higher scores indicate stable, reliable operation with minimal disruptions.

## Real-World Deployment Considerations

### Hardware Integration
- **Microcontroller**: Raspberry Pi 4 or ESP32 for processing and connectivity
- **Sensors**: DHT22 (temperature/humidity), MQ-135 (CO2), BH1750 (light), PIR (occupancy)
- **Communication**: Wi-Fi or Zigbee for data transmission
- **Power**: Mains-powered with battery backup for critical functions

### Cloud Platform
- Real-time data ingestion via MQTT or REST APIs
- Secure data storage with encryption
- Machine learning for predictive analytics
- Mobile and web dashboards for stakeholders

### Security Measures
- End-to-end encryption for all communications
- Secure authentication and authorization
- Regular security audits and updates
- Compliance with educational data protection standards

## Future Enhancements

1. **Machine Learning Integration**: Predictive occupancy and energy forecasting
2. **Advanced Sensors**: CO2 sensors, air quality monitoring, noise level detection
3. **Mobile Applications**: Native iOS and Android apps for teachers and administrators
4. **Cloud Integration**: Real-time data sync with institutional management systems
5. **Blockchain Security**: Immutable audit logs for facility management
6. **Telemedicine**: Integration with healthcare systems for student wellness monitoring
7. **Multi-Classroom Management**: Centralized control and monitoring of multiple classrooms
8. **Predictive Maintenance**: Alerts for equipment maintenance based on usage patterns

## Troubleshooting

### Issue: ImportError for matplotlib or numpy
**Solution**: Install missing packages:
```bash
pip install matplotlib numpy python-docx
```

### Issue: CSV or JSON files not found
**Solution**: Ensure you've run the main simulation first:
```bash
python3 smart_classroom_monitoring.py
```

### Issue: Charts not generating
**Solution**: Verify matplotlib installation and check file permissions:
```bash
pip install --upgrade matplotlib
```

## Performance Optimization Tips

1. **For Large Datasets**: Increase simulation cycles for more comprehensive analysis
2. **For Real-time Processing**: Implement streaming data processing with message queues
3. **For Cloud Deployment**: Use containerization (Docker) and orchestration (Kubernetes)
4. **For ML Integration**: Prepare data in batches for model training

## References

- Python Documentation: https://docs.python.org/3/
- Matplotlib Documentation: https://matplotlib.org/
- IoT in Smart Buildings: https://ieeexplore.ieee.org/
- Smart Classroom Technologies: https://www.researchgate.net/
- Energy Optimization: https://www.sciencedirect.com/

## Support and Contact

For questions, issues, or suggestions regarding this project, please refer to the comprehensive documentation in the internship report or contact the development team.

## License

This project is provided for educational and research purposes as part of an internship program.

## Acknowledgments

This project was developed as part of an internship program focused on IoT technologies and intelligent facility management. The work demonstrates the practical application of IoT principles in solving real-world educational and environmental challenges.

---

**Project Status**: Completed ✓
**Last Updated**: July 13, 2026
**Version**: 1.0
**Total Lines of Code**: 1500+
**Simulation Cycles**: 1000
**Data Points**: 1000+
**Visualizations**: 7 professional charts
**Report Pages**: 30+
