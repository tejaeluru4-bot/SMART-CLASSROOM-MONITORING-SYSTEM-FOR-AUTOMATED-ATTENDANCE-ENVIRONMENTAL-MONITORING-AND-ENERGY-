"""
Smart Classroom Monitoring System
Automated attendance, environmental monitoring, and energy optimization

This module simulates a comprehensive smart classroom monitoring system that tracks
attendance, monitors environmental conditions, and optimizes energy consumption.
"""

import random
import datetime
import json
import csv
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
import statistics
from enum import Enum


class AttendanceStatus(Enum):
    """Attendance status classification."""
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    LATE = "LATE"


class EnvironmentalStatus(Enum):
    """Environmental condition status."""
    OPTIMAL = "OPTIMAL"
    ACCEPTABLE = "ACCEPTABLE"
    POOR = "POOR"
    CRITICAL = "CRITICAL"


class EnergyLevel(Enum):
    """Energy consumption level."""
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    EXCESSIVE = "EXCESSIVE"


@dataclass
class ClassroomReading:
    """Represents a single classroom monitoring reading."""
    timestamp: str
    classroom_id: str
    occupancy_count: int              # Number of students present
    temperature: float                # Celsius
    humidity: float                   # Percentage
    co2_level: int                    # PPM (parts per million)
    light_intensity: float            # Lux
    attendance_recorded: int          # Number of attendance records
    lights_status: str                # ON/OFF
    fan_status: str                   # ON/OFF
    energy_consumption: float         # kWh
    environmental_status: str         # OPTIMAL, ACCEPTABLE, POOR, CRITICAL
    energy_level: str                 # LOW, MODERATE, HIGH, EXCESSIVE
    alert_message: str


class AttendanceRecorder:
    """Records and manages student attendance."""
    
    def __init__(self, total_students: int = 50):
        """
        Initialize the attendance recorder.
        
        Args:
            total_students: Total number of students in the class
        """
        self.total_students = total_students
        self.attendance_records = []
    
    def record_attendance(self) -> int:
        """
        Record attendance for the class session.
        
        Returns:
            Number of students present
        """
        # Simulate attendance (typically 85-95% attendance rate)
        attendance_rate = random.uniform(0.85, 0.95)
        present_count = int(self.total_students * attendance_rate)
        
        # Simulate some late arrivals (5-10% of present students)
        late_count = int(present_count * random.uniform(0.05, 0.10))
        
        record = {
            'timestamp': datetime.datetime.now().isoformat(),
            'total_students': self.total_students,
            'present': present_count - late_count,
            'late': late_count,
            'absent': self.total_students - present_count
        }
        
        self.attendance_records.append(record)
        return present_count


class TemperatureSensor:
    """Simulates a temperature sensor for classroom monitoring."""
    
    def __init__(self, baseline_temp: float = 24.0):
        """
        Initialize the temperature sensor.
        
        Args:
            baseline_temp: Baseline classroom temperature in Celsius
        """
        self.baseline_temp = baseline_temp
        self.last_reading = None
    
    def read_temperature(self) -> float:
        """
        Read classroom temperature with realistic variations.
        
        Returns:
            Temperature in Celsius
        """
        # Simulate occasional temperature fluctuations
        if random.random() < 0.1:  # 10% chance of significant change
            fluctuation = random.uniform(-2, 2)
        else:
            fluctuation = random.uniform(-0.5, 0.5)
        
        if self.last_reading is None:
            reading = self.baseline_temp + fluctuation
        else:
            reading = self.last_reading * 0.8 + self.baseline_temp * 0.2 + fluctuation
        
        reading = max(18, min(32, round(reading, 1)))  # Clamp between 18-32°C
        self.last_reading = reading
        return reading


class HumiditySensor:
    """Simulates a humidity sensor."""
    
    def __init__(self, baseline_humidity: float = 50.0):
        """
        Initialize the humidity sensor.
        
        Args:
            baseline_humidity: Baseline humidity percentage
        """
        self.baseline_humidity = baseline_humidity
        self.last_reading = None
    
    def read_humidity(self) -> float:
        """
        Read humidity level.
        
        Returns:
            Humidity percentage (0-100%)
        """
        if self.last_reading is None:
            reading = self.baseline_humidity + random.uniform(-5, 5)
        else:
            reading = self.last_reading * 0.85 + self.baseline_humidity * 0.15
            reading += random.uniform(-2, 2)
        
        reading = max(20, min(80, round(reading, 1)))
        self.last_reading = reading
        return reading


class CO2Sensor:
    """Simulates a CO2 level sensor."""
    
    def __init__(self, baseline_co2: int = 400):
        """
        Initialize the CO2 sensor.
        
        Args:
            baseline_co2: Baseline CO2 level in PPM
        """
        self.baseline_co2 = baseline_co2
        self.last_reading = None
    
    def read_co2_level(self, occupancy: int) -> int:
        """
        Read CO2 level based on occupancy.
        
        Args:
            occupancy: Number of people in the classroom
            
        Returns:
            CO2 level in PPM
        """
        # CO2 increases with occupancy
        occupancy_effect = occupancy * 5  # ~5 PPM per person
        
        if self.last_reading is None:
            reading = self.baseline_co2 + occupancy_effect + random.uniform(-20, 20)
        else:
            reading = self.last_reading * 0.7 + (self.baseline_co2 + occupancy_effect) * 0.3
            reading += random.uniform(-10, 10)
        
        reading = int(max(350, min(2000, reading)))
        self.last_reading = reading
        return reading


class LightSensor:
    """Simulates a light intensity sensor."""
    
    def __init__(self, baseline_light: float = 500.0):
        """
        Initialize the light sensor.
        
        Args:
            baseline_light: Baseline light intensity in Lux
        """
        self.baseline_light = baseline_light
        self.last_reading = None
    
    def read_light_intensity(self, occupancy: int) -> float:
        """
        Read light intensity.
        
        Returns:
            Light intensity in Lux
        """
        # Simulate time-based variations (day/night cycle)
        time_factor = random.uniform(0.5, 1.5)
        
        if self.last_reading is None:
            reading = self.baseline_light * time_factor + random.uniform(-50, 50)
        else:
            reading = self.last_reading * 0.9 + self.baseline_light * time_factor * 0.1
            reading += random.uniform(-20, 20)
        
        reading = max(100, min(1000, round(reading, 1)))
        self.last_reading = reading
        return reading


class OccupancySensor:
    """Simulates an occupancy sensor."""
    
    def __init__(self, classroom_capacity: int = 50):
        """
        Initialize the occupancy sensor.
        
        Args:
            classroom_capacity: Maximum classroom capacity
        """
        self.classroom_capacity = classroom_capacity
        self.last_occupancy = 0
    
    def read_occupancy(self) -> int:
        """
        Read current occupancy.
        
        Returns:
            Number of people in the classroom
        """
        # Simulate occupancy changes throughout the day
        if random.random() < 0.3:  # 30% chance of significant change
            change = random.randint(-10, 10)
        else:
            change = random.randint(-2, 2)
        
        occupancy = max(0, min(self.classroom_capacity, self.last_occupancy + change))
        self.last_occupancy = occupancy
        return occupancy


class EnvironmentalAnalyzer:
    """Analyzes environmental conditions and generates alerts."""
    
    def __init__(self,
                 temp_optimal_low: float = 20.0,
                 temp_optimal_high: float = 26.0,
                 humidity_optimal_low: float = 40.0,
                 humidity_optimal_high: float = 60.0,
                 co2_acceptable: int = 1000,
                 co2_poor: int = 1500,
                 light_optimal: float = 300.0):
        """
        Initialize the environmental analyzer.
        
        Args:
            temp_optimal_low/high: Optimal temperature range
            humidity_optimal_low/high: Optimal humidity range
            co2_acceptable: Acceptable CO2 level threshold
            co2_poor: Poor CO2 level threshold
            light_optimal: Optimal light intensity
        """
        self.temp_optimal_low = temp_optimal_low
        self.temp_optimal_high = temp_optimal_high
        self.humidity_optimal_low = humidity_optimal_low
        self.humidity_optimal_high = humidity_optimal_high
        self.co2_acceptable = co2_acceptable
        self.co2_poor = co2_poor
        self.light_optimal = light_optimal
        self.alert_history = []
    
    def analyze_environment(self,
                           temperature: float,
                           humidity: float,
                           co2_level: int,
                           light_intensity: float) -> Tuple[EnvironmentalStatus, str]:
        """
        Analyze environmental conditions.
        
        Returns:
            Tuple of (EnvironmentalStatus, alert_message)
        """
        alerts = []
        
        # Analyze temperature
        if temperature < self.temp_optimal_low or temperature > self.temp_optimal_high:
            if temperature < 18 or temperature > 28:
                alerts.append(f"CRITICAL TEMP: {temperature}°C")
            else:
                alerts.append(f"POOR TEMP: {temperature}°C")
        
        # Analyze humidity
        if humidity < self.humidity_optimal_low or humidity > self.humidity_optimal_high:
            if humidity < 30 or humidity > 70:
                alerts.append(f"CRITICAL HUMIDITY: {humidity}%")
            else:
                alerts.append(f"POOR HUMIDITY: {humidity}%")
        
        # Analyze CO2
        if co2_level > self.co2_poor:
            alerts.append(f"CRITICAL CO2: {co2_level} PPM")
        elif co2_level > self.co2_acceptable:
            alerts.append(f"POOR CO2: {co2_level} PPM")
        
        # Analyze light
        if light_intensity < self.light_optimal * 0.5:
            alerts.append(f"LOW LIGHT: {light_intensity} Lux")
        
        # Determine overall status
        if len(alerts) >= 2:
            status = EnvironmentalStatus.CRITICAL
            message = " | ".join(alerts)
        elif any("CRITICAL" in alert for alert in alerts):
            status = EnvironmentalStatus.POOR
            message = " | ".join(alerts)
        elif any("POOR" in alert for alert in alerts):
            status = EnvironmentalStatus.ACCEPTABLE
            message = " | ".join(alerts)
        else:
            status = EnvironmentalStatus.OPTIMAL
            message = f"All conditions optimal - Temp: {temperature}°C, Humidity: {humidity}%, CO2: {co2_level} PPM"
        
        if status != EnvironmentalStatus.OPTIMAL:
            self.alert_history.append({
                'timestamp': datetime.datetime.now().isoformat(),
                'status': status.value,
                'message': message,
                'temperature': temperature,
                'humidity': humidity,
                'co2': co2_level,
                'light': light_intensity
            })
        
        return status, message


class EnergyOptimizer:
    """Manages energy optimization based on occupancy and conditions."""
    
    def __init__(self):
        self.lights_on = False
        self.fan_on = False
        self.energy_consumption = 0.0
    
    def optimize_energy(self, occupancy: int, light_intensity: float, temperature: float) -> Tuple[str, str, float]:
        """
        Optimize energy consumption based on conditions.
        
        Returns:
            Tuple of (lights_status, fan_status, energy_consumption)
        """
        # Light control based on occupancy and natural light
        if occupancy > 0 and light_intensity < 300:
            self.lights_on = True
        elif occupancy == 0 or light_intensity > 600:
            self.lights_on = False
        
        # Fan control based on temperature and occupancy
        if occupancy > 30 and temperature > 25:
            self.fan_on = True
        elif occupancy < 10 or temperature < 22:
            self.fan_on = False
        
        # Calculate energy consumption
        lights_power = 100 if self.lights_on else 0  # 100W per light fixture
        fan_power = 150 if self.fan_on else 0  # 150W for fan
        base_power = 50  # 50W base consumption (sensors, controllers)
        
        self.energy_consumption = (lights_power + fan_power + base_power) / 1000  # Convert to kW
        
        lights_status = "ON" if self.lights_on else "OFF"
        fan_status = "ON" if self.fan_on else "OFF"
        
        return lights_status, fan_status, self.energy_consumption
    
    def get_energy_level(self) -> EnergyLevel:
        """Classify energy consumption level."""
        if self.energy_consumption < 0.1:
            return EnergyLevel.LOW
        elif self.energy_consumption < 0.2:
            return EnergyLevel.MODERATE
        elif self.energy_consumption < 0.3:
            return EnergyLevel.HIGH
        else:
            return EnergyLevel.EXCESSIVE


class SmartClassroomMonitoringSystem:
    """Main system controller for smart classroom monitoring."""
    
    def __init__(self, classroom_id: str = "CLASSROOM_001", total_students: int = 50):
        """
        Initialize the smart classroom monitoring system.
        
        Args:
            classroom_id: Unique classroom identifier
            total_students: Total number of students
        """
        self.classroom_id = classroom_id
        self.total_students = total_students
        
        # Initialize sensors
        self.attendance_recorder = AttendanceRecorder(total_students)
        self.temperature_sensor = TemperatureSensor(baseline_temp=24.0)
        self.humidity_sensor = HumiditySensor(baseline_humidity=50.0)
        self.co2_sensor = CO2Sensor(baseline_co2=400)
        self.light_sensor = LightSensor(baseline_light=500.0)
        self.occupancy_sensor = OccupancySensor(classroom_capacity=total_students)
        
        # Initialize analyzers
        self.environmental_analyzer = EnvironmentalAnalyzer()
        self.energy_optimizer = EnergyOptimizer()
        
        # Data logging
        self.readings: List[ClassroomReading] = []
        self.optimal_count = 0
        self.acceptable_count = 0
        self.poor_count = 0
        self.critical_count = 0
    
    def read_sensors(self) -> Tuple[int, float, float, int, float]:
        """
        Read all sensors.
        
        Returns:
            Tuple of (occupancy, temperature, humidity, co2, light_intensity)
        """
        occupancy = self.occupancy_sensor.read_occupancy()
        temperature = self.temperature_sensor.read_temperature()
        humidity = self.humidity_sensor.read_humidity()
        co2_level = self.co2_sensor.read_co2_level(occupancy)
        light_intensity = self.light_sensor.read_light_intensity(occupancy)
        
        return occupancy, temperature, humidity, co2_level, light_intensity
    
    def simulate_cycle(self) -> ClassroomReading:
        """
        Simulate one complete monitoring cycle.
        
        Returns:
            ClassroomReading object
        """
        # Read sensors
        occupancy, temperature, humidity, co2_level, light_intensity = self.read_sensors()
        
        # Record attendance
        attendance_recorded = self.attendance_recorder.record_attendance()
        
        # Analyze environment
        env_status, env_alert = self.environmental_analyzer.analyze_environment(
            temperature, humidity, co2_level, light_intensity
        )
        
        # Optimize energy
        lights_status, fan_status, energy_consumption = self.energy_optimizer.optimize_energy(
            occupancy, light_intensity, temperature
        )
        
        energy_level = self.energy_optimizer.get_energy_level()
        
        # Update counters
        if env_status == EnvironmentalStatus.OPTIMAL:
            self.optimal_count += 1
        elif env_status == EnvironmentalStatus.ACCEPTABLE:
            self.acceptable_count += 1
        elif env_status == EnvironmentalStatus.POOR:
            self.poor_count += 1
        elif env_status == EnvironmentalStatus.CRITICAL:
            self.critical_count += 1
        
        # Create reading record
        reading = ClassroomReading(
            timestamp=datetime.datetime.now().isoformat(),
            classroom_id=self.classroom_id,
            occupancy_count=occupancy,
            temperature=temperature,
            humidity=humidity,
            co2_level=co2_level,
            light_intensity=light_intensity,
            attendance_recorded=attendance_recorded,
            lights_status=lights_status,
            fan_status=fan_status,
            energy_consumption=energy_consumption,
            environmental_status=env_status.value,
            energy_level=energy_level.value,
            alert_message=env_alert
        )
        
        self.readings.append(reading)
        return reading
    
    def run_simulation(self, num_cycles: int = 1000) -> List[ClassroomReading]:
        """
        Run the simulation for a specified number of cycles.
        
        Args:
            num_cycles: Number of monitoring cycles to simulate
            
        Returns:
            List of all classroom readings
        """
        for _ in range(num_cycles):
            self.simulate_cycle()
        
        return self.readings
    
    def get_statistics(self) -> Dict:
        """
        Calculate statistics from collected readings.
        
        Returns:
            Dictionary containing various statistics
        """
        if not self.readings:
            return {}
        
        temperatures = [r.temperature for r in self.readings]
        humidities = [r.humidity for r in self.readings]
        co2_levels = [r.co2_level for r in self.readings]
        light_intensities = [r.light_intensity for r in self.readings]
        occupancies = [r.occupancy_count for r in self.readings]
        energy_consumptions = [r.energy_consumption for r in self.readings]
        
        return {
            'total_readings': len(self.readings),
            'total_cycles': len(self.readings),
            'classroom_id': self.classroom_id,
            'total_students': self.total_students,
            'temperature': {
                'avg': round(statistics.mean(temperatures), 2),
                'min': round(min(temperatures), 2),
                'max': round(max(temperatures), 2),
                'std': round(statistics.stdev(temperatures), 2) if len(temperatures) > 1 else 0
            },
            'humidity': {
                'avg': round(statistics.mean(humidities), 2),
                'min': round(min(humidities), 2),
                'max': round(max(humidities), 2),
                'std': round(statistics.stdev(humidities), 2) if len(humidities) > 1 else 0
            },
            'co2_level': {
                'avg': int(statistics.mean(co2_levels)),
                'min': min(co2_levels),
                'max': max(co2_levels),
                'std': round(statistics.stdev(co2_levels), 2) if len(co2_levels) > 1 else 0
            },
            'light_intensity': {
                'avg': round(statistics.mean(light_intensities), 2),
                'min': round(min(light_intensities), 2),
                'max': round(max(light_intensities), 2),
                'std': round(statistics.stdev(light_intensities), 2) if len(light_intensities) > 1 else 0
            },
            'occupancy': {
                'avg': round(statistics.mean(occupancies), 2),
                'min': min(occupancies),
                'max': max(occupancies),
                'std': round(statistics.stdev(occupancies), 2) if len(occupancies) > 1 else 0
            },
            'energy_consumption': {
                'avg': round(statistics.mean(energy_consumptions), 3),
                'min': round(min(energy_consumptions), 3),
                'max': round(max(energy_consumptions), 3),
                'total': round(sum(energy_consumptions), 2)
            },
            'environmental_status_distribution': {
                'optimal': self.optimal_count,
                'acceptable': self.acceptable_count,
                'poor': self.poor_count,
                'critical': self.critical_count
            },
            'alert_percentage': round(((self.acceptable_count + self.poor_count + self.critical_count) / len(self.readings)) * 100, 2)
        }
    
    def export_to_csv(self, filename: str):
        """Export readings to CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'classroom_id', 'occupancy_count', 'temperature', 'humidity',
                         'co2_level', 'light_intensity', 'attendance_recorded', 'lights_status',
                         'fan_status', 'energy_consumption', 'environmental_status', 'energy_level',
                         'alert_message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for reading in self.readings:
                writer.writerow(asdict(reading))
    
    def export_to_json(self, filename: str):
        """Export readings to JSON file."""
        data = {
            'classroom_id': self.classroom_id,
            'metadata': {
                'total_readings': len(self.readings),
                'total_cycles': len(self.readings),
                'monitoring_duration': 'Simulated continuous monitoring'
            },
            'statistics': self.get_statistics(),
            'alert_history': self.environmental_analyzer.alert_history,
            'readings': [asdict(r) for r in self.readings]
        }
        
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)
    
    def export_alerts_to_csv(self, filename: str):
        """Export alert history to CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'status', 'message', 'temperature', 'humidity', 'co2', 'light']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for alert in self.environmental_analyzer.alert_history:
                writer.writerow(alert)


class SystemPerformanceAnalyzer:
    """Analyzes system performance and efficiency metrics."""
    
    @staticmethod
    def calculate_environmental_quality_score(optimal_count: int, total_readings: int) -> float:
        """
        Calculate environmental quality score.
        
        Returns:
            Quality score (0-100)
        """
        if total_readings == 0:
            return 100.0
        quality = (optimal_count / total_readings) * 100
        return round(quality, 2)
    
    @staticmethod
    def calculate_energy_efficiency_score(total_energy: float, total_cycles: int) -> float:
        """
        Calculate energy efficiency score.
        
        Returns:
            Efficiency score (0-100)
        """
        if total_cycles == 0:
            return 100.0
        avg_energy = total_energy / total_cycles
        # Lower average energy consumption = higher efficiency
        efficiency = max(0, 100 - (avg_energy * 100))
        return round(efficiency, 2)
    
    @staticmethod
    def calculate_system_reliability_score(alert_count: int, total_readings: int) -> float:
        """
        Calculate system reliability score.
        
        Returns:
            Reliability score (0-100)
        """
        if total_readings == 0:
            return 100.0
        reliability = max(0, 100 - (alert_count / total_readings) * 30)
        return round(reliability, 2)


def main():
    """Main function to run the simulation."""
    print("=" * 80)
    print("SMART CLASSROOM MONITORING SYSTEM")
    print("Automated Attendance, Environmental Monitoring, and Energy Optimization")
    print("=" * 80)
    print()
    
    # Initialize system
    system = SmartClassroomMonitoringSystem(classroom_id="CLASSROOM_001", total_students=50)
    
    print("Starting simulation with 1000 monitoring cycles...")
    print("(Continuous classroom monitoring with real-time analysis)")
    print()
    
    # Run simulation
    readings = system.run_simulation(num_cycles=1000)
    
    # Get statistics
    stats = system.get_statistics()
    
    # Export data
    system.export_to_csv('/home/ubuntu/smart_classroom_report/classroom_readings.csv')
    system.export_to_json('/home/ubuntu/smart_classroom_report/classroom_readings.json')
    system.export_alerts_to_csv('/home/ubuntu/smart_classroom_report/environmental_alerts.csv')
    
    # Display results
    print("SIMULATION RESULTS")
    print("-" * 80)
    print(f"Total Monitoring Cycles: {stats['total_cycles']}")
    print(f"Total Readings: {stats['total_readings']}")
    print(f"Classroom ID: {stats['classroom_id']}")
    print()
    
    print("ENVIRONMENTAL STATUS DISTRIBUTION")
    print("-" * 80)
    dist = stats['environmental_status_distribution']
    print(f"Optimal: {dist['optimal']} ({(dist['optimal']/stats['total_readings']*100):.1f}%)")
    print(f"Acceptable: {dist['acceptable']} ({(dist['acceptable']/stats['total_readings']*100):.1f}%)")
    print(f"Poor: {dist['poor']} ({(dist['poor']/stats['total_readings']*100):.1f}%)")
    print(f"Critical: {dist['critical']} ({(dist['critical']/stats['total_readings']*100):.1f}%)")
    print(f"Total Alert Events: {dist['acceptable'] + dist['poor'] + dist['critical']} ({stats['alert_percentage']}%)")
    print()
    
    print("TEMPERATURE STATISTICS (°C)")
    print("-" * 80)
    temp = stats['temperature']
    print(f"Average: {temp['avg']}°C")
    print(f"Range: {temp['min']} - {temp['max']}°C")
    print(f"Standard Deviation: {temp['std']}°C")
    print()
    
    print("HUMIDITY STATISTICS (%)")
    print("-" * 80)
    hum = stats['humidity']
    print(f"Average: {hum['avg']}%")
    print(f"Range: {hum['min']} - {hum['max']}%")
    print(f"Standard Deviation: {hum['std']}%")
    print()
    
    print("CO2 LEVEL STATISTICS (PPM)")
    print("-" * 80)
    co2 = stats['co2_level']
    print(f"Average: {co2['avg']} PPM")
    print(f"Range: {co2['min']} - {co2['max']} PPM")
    print(f"Standard Deviation: {co2['std']} PPM")
    print()
    
    print("LIGHT INTENSITY STATISTICS (Lux)")
    print("-" * 80)
    light = stats['light_intensity']
    print(f"Average: {light['avg']} Lux")
    print(f"Range: {light['min']} - {light['max']} Lux")
    print(f"Standard Deviation: {light['std']} Lux")
    print()
    
    print("OCCUPANCY STATISTICS")
    print("-" * 80)
    occ = stats['occupancy']
    print(f"Average Occupancy: {occ['avg']} students")
    print(f"Range: {occ['min']} - {occ['max']} students")
    print(f"Standard Deviation: {occ['std']} students")
    print()
    
    print("ENERGY CONSUMPTION STATISTICS (kWh)")
    print("-" * 80)
    energy = stats['energy_consumption']
    print(f"Average: {energy['avg']} kWh per cycle")
    print(f"Range: {energy['min']} - {energy['max']} kWh")
    print(f"Total Consumption: {energy['total']} kWh")
    print()
    
    # Performance analysis
    analyzer = SystemPerformanceAnalyzer()
    env_quality = analyzer.calculate_environmental_quality_score(
        dist['optimal'], stats['total_readings']
    )
    energy_efficiency = analyzer.calculate_energy_efficiency_score(
        energy['total'], stats['total_cycles']
    )
    reliability = analyzer.calculate_system_reliability_score(
        dist['acceptable'] + dist['poor'] + dist['critical'],
        stats['total_readings']
    )
    
    print("SYSTEM PERFORMANCE METRICS")
    print("-" * 80)
    print(f"Environmental Quality Score: {env_quality}/100")
    print(f"Energy Efficiency Score: {energy_efficiency}/100")
    print(f"System Reliability Score: {reliability}/100")
    print()
    
    print("Data exported to:")
    print("  - /home/ubuntu/smart_classroom_report/classroom_readings.csv")
    print("  - /home/ubuntu/smart_classroom_report/classroom_readings.json")
    print("  - /home/ubuntu/smart_classroom_report/environmental_alerts.csv")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
