def vision_detection():
    detections = [
        {"object": "box", "confidence": 78, "mode": "infrared", "distance": 2.5},
        {"object": "human", "confidence": 95, "mode": "camera", "distance": 1.2},
        {"object": "ball", "confidence": 82, "mode": "ultrasonic", "distance": 3.0},
        {"object": "human", "confidence": 88, "mode": "camera", "distance": 0.8},
        {"object": "chair", "confidence": 70, "mode": "infrared", "distance": 2.8}
    ]

    # Filter for valid human detections
    valid_humans = list(filter(
        lambda d: d["object"] == "human" and d["mode"] == "camera" and d["confidence"] > 85, 
        detections
    ))
    
    # Map to extract distances
    distances = list(map(lambda d: d["distance"], valid_humans))
    
    print("Valid Human Detections:")
    print(valid_humans)
    print("\nDistances:")
    print(distances)
    print() # newline for spacing
    
    # Check distances for alerts
    for d in distances:
        if d < 1.0:
            print("ALERT: Human very close!")
        else:
            print("Human detected at safe distance")

vision_detection()