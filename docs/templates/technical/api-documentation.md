# API Documentation Template

## API Overview
- **API Name:** [Name]
- **Version:** [Version]
- **Base URL:** [URL]
- **Description:** [Brief description]

## Authentication
- **Method:** [OAuth2/Basic Auth/API Key]
- **Required Headers:** [List]
- **Token Format:** [Format]
- **Expiration:** [Duration]

## Endpoints

### [Endpoint 1]
- **Path:** `/path/to/endpoint`
- **Method:** [GET/POST/PUT/DELETE]
- **Description:** [Description]

#### Request
- **Headers:**
  ```
  Content-Type: application/json
  Authorization: Bearer <token>
  ```
- **Parameters:**
  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | [Param 1] | [Type] | [Yes/No] | [Description] |
  | [Param 2] | [Type] | [Yes/No] | [Description] |

#### Response
- **Status Codes:**
  - 200: Success
  - 400: Bad Request
  - 401: Unauthorized
  - 404: Not Found
  - 500: Server Error

- **Response Body:**
  ```json
  {
    "field1": "value1",
    "field2": "value2"
  }
  ```

#### Example
```bash
curl -X GET \
  'https://api.example.com/endpoint' \
  -H 'Authorization: Bearer <token>'
```

### [Endpoint 2]
- **Path:** `/path/to/endpoint`
- **Method:** [GET/POST/PUT/DELETE]
- **Description:** [Description]

#### Request
- **Headers:**
  ```
  Content-Type: application/json
  Authorization: Bearer <token>
  ```
- **Parameters:**
  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | [Param 1] | [Type] | [Yes/No] | [Description] |
  | [Param 2] | [Type] | [Yes/No] | [Description] |

#### Response
- **Status Codes:**
  - 200: Success
  - 400: Bad Request
  - 401: Unauthorized
  - 404: Not Found
  - 500: Server Error

- **Response Body:**
  ```json
  {
    "field1": "value1",
    "field2": "value2"
  }
  ```

#### Example
```bash
curl -X POST \
  'https://api.example.com/endpoint' \
  -H 'Authorization: Bearer <token>' \
  -d '{
    "field1": "value1",
    "field2": "value2"
  }'
```

## Rate Limiting
- **Requests per minute:** [Number]
- **Requests per hour:** [Number]
- **Requests per day:** [Number]

## Error Handling
- **Error Format:**
  ```json
  {
    "error": {
      "code": "ERROR_CODE",
      "message": "Error message",
      "details": {}
    }
  }
  ```

## Versioning
- **Current Version:** [Version]
- **Deprecated Versions:** [List]
- **Version Policy:** [Policy]

## Changelog
| Version | Date | Changes |
|---------|------|---------|
| [Version] | [Date] | [Changes] |
| [Version] | [Date] | [Changes] |

## Support
- **Contact:** [Email]
- **Documentation:** [URL]
- **Status Page:** [URL]

---
*This template should be updated whenever the API changes.* 