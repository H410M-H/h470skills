# Mobile Locators & Framework Patterns

## 1. Dynamic Locators Hierarchy

When writing resilient tests for Android or mobile web:

1. **Accessibility ID / Content Description**: `accessibility_id` or `@content-desc` (most durable across redesigns).
2. **Resource ID**: `@resource-id` (package-scoped, durable within a version).
3. **Exact Visible Text**: `@text` (durable for unique labels/buttons, sensitive to i18n).
4. **XPath with Semantic Predicates**: `//android.widget.Button[contains(@text, 'Submit')]` (use short relative paths, avoid deep absolute paths like `/hierarchy/android.widget.FrameLayout...`).
5. **Absolute Coordinates**: Fallback coordinates discovered during ARTEMIS inspection.

---

## 2. Framework-Specific Fallback Implementations

### Python `uiautomator2`
```python
def resilient_click(d, text=None, resource_id=None, coords=None):
    if resource_id and d(resourceId=resource_id).exists(timeout=3):
        d(resourceId=resource_id).click()
        return
    if text and d(text=text).exists(timeout=3):
        d(text=text).click()
        return
    if coords:
        d.click(coords[0], coords[1])
        return
    raise RuntimeError("Target element could not be found.")
```

### Maestro (`yaml`)
```yaml
appId: com.example.app
---
- launchApp
- runFlow:
    when:
      visible: "Login"
    commands:
      - tapOn: "Login"
- runFlow:
    when:
      notVisible: "Login"
    commands:
      - tapOn:
          point: "50%,80%"
```

### Appium (JavaScript / TypeScript)
```typescript
async function safeClick(driver: WebdriverIO.Browser, selector: string, fallbackPoint?: { x: number; y: number }) {
  try {
    const el = await driver.$(selector);
    if (await el.isDisplayed()) {
      await el.click();
      return;
    }
  } catch (err) {
    if (fallbackPoint) {
      await driver.touchAction({ action: 'tap', x: fallbackPoint.x, y: fallbackPoint.y });
      return;
    }
    throw err;
  }
}
```
