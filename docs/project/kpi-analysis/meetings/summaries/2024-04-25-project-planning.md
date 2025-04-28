# Meeting Summary: KPI Analysis Project Planning

## Date
April 25, 2024

## Participants
- Dave Schedin
- Chris 'Tico' Antico
- Mike Cooper
- Arthur Jin

## Key Topics Discussed

### 1. Project Overview and Pain Points
- Current Computrek system issues identified:
  - Manual, time-consuming processes
  - Limited growth and transformation capabilities
  - Difficult to maintain
- Proposed solution: Web-based KPI and analysis platform
  - Cloud-based system with API integration
  - Real-time performance monitoring and analysis
  - AI-enhanced coaching suggestions

### 2. Technical Architecture
- Core Features:
  - Point of sale system integration
  - Real-time interactive dashboards
  - Performance forecasting
  - Multi-location support
  - Data hierarchy: regions → shops → employees
  - Future expansion capabilities for customer segments and vehicle types

### 3. Development Phases
1. **Demo Phase** (2 months):
   - Basic authentication
   - Simple KPI dashboard
   - Manual data entry and basic data storage
   - Sample visualizations
   - Data cube operations
   - Basic responsive web interface
   - Half salary for engineers ($50,000/year rate)

2. **MVP Phase** (3-6 months):
   - Full feature set for core functionality
   - Integration with one shop management system
   - Full salary for engineers
   - Mobile responsiveness consideration

3. **Production Phase** (18 months):
   - Complete UI/UX development
   - Integration with multiple shop management systems
   - Polished, releasable product

### 4. Technical Considerations
- Using Redux for state management
- Data cube implementation for efficient data handling
- Scalability support for hundreds of thousands of users
- Initial local hosting for demo/MVP
- AWS cloud hosting for production

### 5. Implementation Strategy
- Initial focus on Tech-Metrics system
- Test implementation with Smart Service (2 locations)
- Potential second test with Dynamic Diesel (single location)

## Action Items
1. [ ] Dave & Mike to discuss financial sourcing
2. [ ] Create contract for source code ownership
3. [ ] Begin demo phase development
4. [ ] Set up initial meeting with Smart Service for data access
5. [ ] Research AI-assisted contract creation for agreements

## Decisions Made
1. Source code ownership will remain with the development team
2. Initial development will focus on single management system (Tech-Metrics)
3. Smart Service selected as primary test implementation
4. Mobile app development deferred to later phases
5. Development will proceed in phases: Demo → MVP → Production

## Next Steps
1. Finalize contracts and agreements
2. Set up development environment
3. Begin demo phase development
4. Establish data access with Smart Service
5. Plan regular progress check-ins

## Notes
- Initial focus on web platform with mobile-responsive design
- Consideration for future mobile app development
- Demo phase to validate technical approach and capabilities
- MVP to demonstrate full core functionality
- Production phase for complete system rollout

## Related Documents
- [Technical Architecture Documentation](../../../technical/architecture/README.md)
- [Project Timeline](../../../planning/timeline.md)
- [Budget Proposal](../../../planning/budget.md) 