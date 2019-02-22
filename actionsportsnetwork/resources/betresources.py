from beckett import resources

class PickResource(resources.BaseResource):
    class Meta:
        name = 'Pick'
        resource_name = 'picks'
        identifier = 'id'
        attributes = (
                'id',
                'league_name',
                'play',
                'game_id',
                'competition_id',
                'competitor_id',
                'user_id',
                'type',
                'period',
                'side_id',
                'value',
                'odds',
                'units',
                'units_net',
                'units_type',
                'result',
                'status',
                'group_pick_id',
                "updated_at",
                "created_at",
                "verified",
                "tag",
                "custom_pick_type",
                "custom_pick_name",
                "settled_at",
                "starts_at",
                "ends_at",
                "player_id"
        )



class GameSubResource(resources.SubResource):
    class Meta:
        name = "Game"
        identifier = "id"
        attributes = (
                        "id",
                        "status",
                        "status_display",
                        "start_time",
                        "away_team_id",
                        "home_team_id",
                        "league_name",
                        "season",
                        "attendance",
                        "coverage",
                        "is_free",
                        "trending"
        )