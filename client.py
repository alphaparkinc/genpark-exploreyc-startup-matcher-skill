class ExploreYcMatcherClient:
    def find_startups(self, industry_preference: str, min_funding_stage: str) -> dict:
        # Mock database recall
        all_startups = [
            {"name": "Velo AI", "industry": "video", "stage": "Seed"},
            {"name": "Nile DB", "industry": "database", "stage": "Series A"}
        ]
        matches = [s for s in all_startups if s["industry"] == industry_preference or industry_preference == "all"]
        return {"matched_companies": matches}