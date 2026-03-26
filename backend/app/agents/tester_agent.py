from app.schemas.tester import TesterOutput

def run_tester_agent(ba_output, sa_output, dev_output) -> TesterOutput:
    return TesterOutput(
        test_scenarios=[
            "Login with valid credentials",
            "Login with invalid credentials"
        ],
        test_cases=[
            "Verify user can login successfully",
            "Verify error message appears for invalid password"
        ],
        risks=[
            "Login form validation may be inconsistent"
        ],
        playwright_files={
            "tests/login.spec.ts": """
import { test, expect } from '@playwright/test';

test('user can open login page', async ({ page }) => {
  await page.goto('http://localhost:3000/login');
  await expect(page).toHaveURL(/login/);
});
""",
            "pages/LoginPage.ts": """
import { Page } from '@playwright/test';

export class LoginPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('http://localhost:3000/login');
  }
}
"""
        }
    )