package com.f1.formula1_zone.driver;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name="driver_stats")

// Attributes of every driver
public class Driver {
    private String name;
    private String country;
    private Integer age;
}
