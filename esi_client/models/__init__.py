# coding: utf-8

# flake8: noqa
"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from esi_client.models.bad_request import BadRequest
from esi_client.models.delete_characters_character_id_mail_labels_label_id_unprocessable_entity import DeleteCharactersCharacterIdMailLabelsLabelIdUnprocessableEntity
from esi_client.models.delete_fleets_fleet_id_members_member_id_not_found import DeleteFleetsFleetIdMembersMemberIdNotFound
from esi_client.models.delete_fleets_fleet_id_squads_squad_id_not_found import DeleteFleetsFleetIdSquadsSquadIdNotFound
from esi_client.models.delete_fleets_fleet_id_wings_wing_id_not_found import DeleteFleetsFleetIdWingsWingIdNotFound
from esi_client.models.error_limited import ErrorLimited
from esi_client.models.forbidden import Forbidden
from esi_client.models.gateway_timeout import GatewayTimeout
from esi_client.models.get_alliances_alliance_id_contacts200_ok import GetAlliancesAllianceIdContacts200Ok
from esi_client.models.get_alliances_alliance_id_contacts_labels200_ok import GetAlliancesAllianceIdContactsLabels200Ok
from esi_client.models.get_alliances_alliance_id_icons_not_found import GetAlliancesAllianceIdIconsNotFound
from esi_client.models.get_alliances_alliance_id_icons_ok import GetAlliancesAllianceIdIconsOk
from esi_client.models.get_alliances_alliance_id_not_found import GetAlliancesAllianceIdNotFound
from esi_client.models.get_alliances_alliance_id_ok import GetAlliancesAllianceIdOk
from esi_client.models.get_characters_character_id_agents_research200_ok import GetCharactersCharacterIdAgentsResearch200Ok
from esi_client.models.get_characters_character_id_assets200_ok import GetCharactersCharacterIdAssets200Ok
from esi_client.models.get_characters_character_id_assets_not_found import GetCharactersCharacterIdAssetsNotFound
from esi_client.models.get_characters_character_id_attributes_ok import GetCharactersCharacterIdAttributesOk
from esi_client.models.get_characters_character_id_blueprints200_ok import GetCharactersCharacterIdBlueprints200Ok
from esi_client.models.get_characters_character_id_bookmarks200_ok import GetCharactersCharacterIdBookmarks200Ok
from esi_client.models.get_characters_character_id_bookmarks_coordinates import GetCharactersCharacterIdBookmarksCoordinates
from esi_client.models.get_characters_character_id_bookmarks_folders200_ok import GetCharactersCharacterIdBookmarksFolders200Ok
from esi_client.models.get_characters_character_id_bookmarks_item import GetCharactersCharacterIdBookmarksItem
from esi_client.models.get_characters_character_id_calendar200_ok import GetCharactersCharacterIdCalendar200Ok
from esi_client.models.get_characters_character_id_calendar_event_id_attendees200_ok import GetCharactersCharacterIdCalendarEventIdAttendees200Ok
from esi_client.models.get_characters_character_id_calendar_event_id_attendees_not_found import GetCharactersCharacterIdCalendarEventIdAttendeesNotFound
from esi_client.models.get_characters_character_id_calendar_event_id_not_found import GetCharactersCharacterIdCalendarEventIdNotFound
from esi_client.models.get_characters_character_id_calendar_event_id_ok import GetCharactersCharacterIdCalendarEventIdOk
from esi_client.models.get_characters_character_id_clones_home_location import GetCharactersCharacterIdClonesHomeLocation
from esi_client.models.get_characters_character_id_clones_jump_clone import GetCharactersCharacterIdClonesJumpClone
from esi_client.models.get_characters_character_id_clones_ok import GetCharactersCharacterIdClonesOk
from esi_client.models.get_characters_character_id_contacts200_ok import GetCharactersCharacterIdContacts200Ok
from esi_client.models.get_characters_character_id_contacts_labels200_ok import GetCharactersCharacterIdContactsLabels200Ok
from esi_client.models.get_characters_character_id_contracts200_ok import GetCharactersCharacterIdContracts200Ok
from esi_client.models.get_characters_character_id_contracts_contract_id_bids200_ok import GetCharactersCharacterIdContractsContractIdBids200Ok
from esi_client.models.get_characters_character_id_contracts_contract_id_bids_not_found import GetCharactersCharacterIdContractsContractIdBidsNotFound
from esi_client.models.get_characters_character_id_contracts_contract_id_items200_ok import GetCharactersCharacterIdContractsContractIdItems200Ok
from esi_client.models.get_characters_character_id_contracts_contract_id_items_not_found import GetCharactersCharacterIdContractsContractIdItemsNotFound
from esi_client.models.get_characters_character_id_corporationhistory200_ok import GetCharactersCharacterIdCorporationhistory200Ok
from esi_client.models.get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk
from esi_client.models.get_characters_character_id_fittings200_ok import GetCharactersCharacterIdFittings200Ok
from esi_client.models.get_characters_character_id_fittings_item import GetCharactersCharacterIdFittingsItem
from esi_client.models.get_characters_character_id_fleet_not_found import GetCharactersCharacterIdFleetNotFound
from esi_client.models.get_characters_character_id_fleet_ok import GetCharactersCharacterIdFleetOk
from esi_client.models.get_characters_character_id_fw_stats_kills import GetCharactersCharacterIdFwStatsKills
from esi_client.models.get_characters_character_id_fw_stats_ok import GetCharactersCharacterIdFwStatsOk
from esi_client.models.get_characters_character_id_fw_stats_victory_points import GetCharactersCharacterIdFwStatsVictoryPoints
from esi_client.models.get_characters_character_id_industry_jobs200_ok import GetCharactersCharacterIdIndustryJobs200Ok
from esi_client.models.get_characters_character_id_killmails_recent200_ok import GetCharactersCharacterIdKillmailsRecent200Ok
from esi_client.models.get_characters_character_id_location_ok import GetCharactersCharacterIdLocationOk
from esi_client.models.get_characters_character_id_loyalty_points200_ok import GetCharactersCharacterIdLoyaltyPoints200Ok
from esi_client.models.get_characters_character_id_mail200_ok import GetCharactersCharacterIdMail200Ok
from esi_client.models.get_characters_character_id_mail_labels_label import GetCharactersCharacterIdMailLabelsLabel
from esi_client.models.get_characters_character_id_mail_labels_ok import GetCharactersCharacterIdMailLabelsOk
from esi_client.models.get_characters_character_id_mail_lists200_ok import GetCharactersCharacterIdMailLists200Ok
from esi_client.models.get_characters_character_id_mail_mail_id_not_found import GetCharactersCharacterIdMailMailIdNotFound
from esi_client.models.get_characters_character_id_mail_mail_id_ok import GetCharactersCharacterIdMailMailIdOk
from esi_client.models.get_characters_character_id_mail_mail_id_recipient import GetCharactersCharacterIdMailMailIdRecipient
from esi_client.models.get_characters_character_id_mail_recipient import GetCharactersCharacterIdMailRecipient
from esi_client.models.get_characters_character_id_medals200_ok import GetCharactersCharacterIdMedals200Ok
from esi_client.models.get_characters_character_id_medals_graphic import GetCharactersCharacterIdMedalsGraphic
from esi_client.models.get_characters_character_id_mining200_ok import GetCharactersCharacterIdMining200Ok
from esi_client.models.get_characters_character_id_not_found import GetCharactersCharacterIdNotFound
from esi_client.models.get_characters_character_id_notifications200_ok import GetCharactersCharacterIdNotifications200Ok
from esi_client.models.get_characters_character_id_notifications_contacts200_ok import GetCharactersCharacterIdNotificationsContacts200Ok
from esi_client.models.get_characters_character_id_ok import GetCharactersCharacterIdOk
from esi_client.models.get_characters_character_id_online_ok import GetCharactersCharacterIdOnlineOk
from esi_client.models.get_characters_character_id_opportunities200_ok import GetCharactersCharacterIdOpportunities200Ok
from esi_client.models.get_characters_character_id_orders200_ok import GetCharactersCharacterIdOrders200Ok
from esi_client.models.get_characters_character_id_orders_history200_ok import GetCharactersCharacterIdOrdersHistory200Ok
from esi_client.models.get_characters_character_id_planets200_ok import GetCharactersCharacterIdPlanets200Ok
from esi_client.models.get_characters_character_id_planets_planet_id_content import GetCharactersCharacterIdPlanetsPlanetIdContent
from esi_client.models.get_characters_character_id_planets_planet_id_extractor_details import GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails
from esi_client.models.get_characters_character_id_planets_planet_id_factory_details import GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails
from esi_client.models.get_characters_character_id_planets_planet_id_head import GetCharactersCharacterIdPlanetsPlanetIdHead
from esi_client.models.get_characters_character_id_planets_planet_id_link import GetCharactersCharacterIdPlanetsPlanetIdLink
from esi_client.models.get_characters_character_id_planets_planet_id_not_found import GetCharactersCharacterIdPlanetsPlanetIdNotFound
from esi_client.models.get_characters_character_id_planets_planet_id_ok import GetCharactersCharacterIdPlanetsPlanetIdOk
from esi_client.models.get_characters_character_id_planets_planet_id_pin import GetCharactersCharacterIdPlanetsPlanetIdPin
from esi_client.models.get_characters_character_id_planets_planet_id_route import GetCharactersCharacterIdPlanetsPlanetIdRoute
from esi_client.models.get_characters_character_id_portrait_not_found import GetCharactersCharacterIdPortraitNotFound
from esi_client.models.get_characters_character_id_portrait_ok import GetCharactersCharacterIdPortraitOk
from esi_client.models.get_characters_character_id_roles_ok import GetCharactersCharacterIdRolesOk
from esi_client.models.get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk
from esi_client.models.get_characters_character_id_ship_ok import GetCharactersCharacterIdShipOk
from esi_client.models.get_characters_character_id_skillqueue200_ok import GetCharactersCharacterIdSkillqueue200Ok
from esi_client.models.get_characters_character_id_skills_ok import GetCharactersCharacterIdSkillsOk
from esi_client.models.get_characters_character_id_skills_skill import GetCharactersCharacterIdSkillsSkill
from esi_client.models.get_characters_character_id_standings200_ok import GetCharactersCharacterIdStandings200Ok
from esi_client.models.get_characters_character_id_titles200_ok import GetCharactersCharacterIdTitles200Ok
from esi_client.models.get_characters_character_id_wallet_journal200_ok import GetCharactersCharacterIdWalletJournal200Ok
from esi_client.models.get_characters_character_id_wallet_transactions200_ok import GetCharactersCharacterIdWalletTransactions200Ok
from esi_client.models.get_contracts_public_bids_contract_id200_ok import GetContractsPublicBidsContractId200Ok
from esi_client.models.get_contracts_public_bids_contract_id_forbidden import GetContractsPublicBidsContractIdForbidden
from esi_client.models.get_contracts_public_bids_contract_id_not_found import GetContractsPublicBidsContractIdNotFound
from esi_client.models.get_contracts_public_items_contract_id200_ok import GetContractsPublicItemsContractId200Ok
from esi_client.models.get_contracts_public_items_contract_id_forbidden import GetContractsPublicItemsContractIdForbidden
from esi_client.models.get_contracts_public_items_contract_id_not_found import GetContractsPublicItemsContractIdNotFound
from esi_client.models.get_contracts_public_region_id200_ok import GetContractsPublicRegionId200Ok
from esi_client.models.get_contracts_public_region_id_not_found import GetContractsPublicRegionIdNotFound
from esi_client.models.get_corporation_corporation_id_mining_extractions200_ok import GetCorporationCorporationIdMiningExtractions200Ok
from esi_client.models.get_corporation_corporation_id_mining_observers200_ok import GetCorporationCorporationIdMiningObservers200Ok
from esi_client.models.get_corporation_corporation_id_mining_observers_observer_id200_ok import GetCorporationCorporationIdMiningObserversObserverId200Ok
from esi_client.models.get_corporations_corporation_id_alliancehistory200_ok import GetCorporationsCorporationIdAlliancehistory200Ok
from esi_client.models.get_corporations_corporation_id_assets200_ok import GetCorporationsCorporationIdAssets200Ok
from esi_client.models.get_corporations_corporation_id_blueprints200_ok import GetCorporationsCorporationIdBlueprints200Ok
from esi_client.models.get_corporations_corporation_id_bookmarks200_ok import GetCorporationsCorporationIdBookmarks200Ok
from esi_client.models.get_corporations_corporation_id_bookmarks_coordinates import GetCorporationsCorporationIdBookmarksCoordinates
from esi_client.models.get_corporations_corporation_id_bookmarks_folders200_ok import GetCorporationsCorporationIdBookmarksFolders200Ok
from esi_client.models.get_corporations_corporation_id_bookmarks_item import GetCorporationsCorporationIdBookmarksItem
from esi_client.models.get_corporations_corporation_id_contacts200_ok import GetCorporationsCorporationIdContacts200Ok
from esi_client.models.get_corporations_corporation_id_contacts_labels200_ok import GetCorporationsCorporationIdContactsLabels200Ok
from esi_client.models.get_corporations_corporation_id_containers_logs200_ok import GetCorporationsCorporationIdContainersLogs200Ok
from esi_client.models.get_corporations_corporation_id_contracts200_ok import GetCorporationsCorporationIdContracts200Ok
from esi_client.models.get_corporations_corporation_id_contracts_contract_id_bids200_ok import GetCorporationsCorporationIdContractsContractIdBids200Ok
from esi_client.models.get_corporations_corporation_id_contracts_contract_id_bids_not_found import GetCorporationsCorporationIdContractsContractIdBidsNotFound
from esi_client.models.get_corporations_corporation_id_contracts_contract_id_items200_ok import GetCorporationsCorporationIdContractsContractIdItems200Ok
from esi_client.models.get_corporations_corporation_id_contracts_contract_id_items_error520 import GetCorporationsCorporationIdContractsContractIdItemsError520
from esi_client.models.get_corporations_corporation_id_contracts_contract_id_items_not_found import GetCorporationsCorporationIdContractsContractIdItemsNotFound
from esi_client.models.get_corporations_corporation_id_customs_offices200_ok import GetCorporationsCorporationIdCustomsOffices200Ok
from esi_client.models.get_corporations_corporation_id_divisions_hangar_hangar import GetCorporationsCorporationIdDivisionsHangarHangar
from esi_client.models.get_corporations_corporation_id_divisions_ok import GetCorporationsCorporationIdDivisionsOk
from esi_client.models.get_corporations_corporation_id_divisions_wallet_wallet import GetCorporationsCorporationIdDivisionsWalletWallet
from esi_client.models.get_corporations_corporation_id_facilities200_ok import GetCorporationsCorporationIdFacilities200Ok
from esi_client.models.get_corporations_corporation_id_fw_stats_kills import GetCorporationsCorporationIdFwStatsKills
from esi_client.models.get_corporations_corporation_id_fw_stats_ok import GetCorporationsCorporationIdFwStatsOk
from esi_client.models.get_corporations_corporation_id_fw_stats_victory_points import GetCorporationsCorporationIdFwStatsVictoryPoints
from esi_client.models.get_corporations_corporation_id_icons_not_found import GetCorporationsCorporationIdIconsNotFound
from esi_client.models.get_corporations_corporation_id_icons_ok import GetCorporationsCorporationIdIconsOk
from esi_client.models.get_corporations_corporation_id_industry_jobs200_ok import GetCorporationsCorporationIdIndustryJobs200Ok
from esi_client.models.get_corporations_corporation_id_killmails_recent200_ok import GetCorporationsCorporationIdKillmailsRecent200Ok
from esi_client.models.get_corporations_corporation_id_medals200_ok import GetCorporationsCorporationIdMedals200Ok
from esi_client.models.get_corporations_corporation_id_medals_issued200_ok import GetCorporationsCorporationIdMedalsIssued200Ok
from esi_client.models.get_corporations_corporation_id_members_titles200_ok import GetCorporationsCorporationIdMembersTitles200Ok
from esi_client.models.get_corporations_corporation_id_membertracking200_ok import GetCorporationsCorporationIdMembertracking200Ok
from esi_client.models.get_corporations_corporation_id_not_found import GetCorporationsCorporationIdNotFound
from esi_client.models.get_corporations_corporation_id_ok import GetCorporationsCorporationIdOk
from esi_client.models.get_corporations_corporation_id_orders200_ok import GetCorporationsCorporationIdOrders200Ok
from esi_client.models.get_corporations_corporation_id_orders_history200_ok import GetCorporationsCorporationIdOrdersHistory200Ok
from esi_client.models.get_corporations_corporation_id_roles200_ok import GetCorporationsCorporationIdRoles200Ok
from esi_client.models.get_corporations_corporation_id_roles_history200_ok import GetCorporationsCorporationIdRolesHistory200Ok
from esi_client.models.get_corporations_corporation_id_shareholders200_ok import GetCorporationsCorporationIdShareholders200Ok
from esi_client.models.get_corporations_corporation_id_standings200_ok import GetCorporationsCorporationIdStandings200Ok
from esi_client.models.get_corporations_corporation_id_starbases200_ok import GetCorporationsCorporationIdStarbases200Ok
from esi_client.models.get_corporations_corporation_id_starbases_starbase_id_fuel import GetCorporationsCorporationIdStarbasesStarbaseIdFuel
from esi_client.models.get_corporations_corporation_id_starbases_starbase_id_ok import GetCorporationsCorporationIdStarbasesStarbaseIdOk
from esi_client.models.get_corporations_corporation_id_structures200_ok import GetCorporationsCorporationIdStructures200Ok
from esi_client.models.get_corporations_corporation_id_structures_service import GetCorporationsCorporationIdStructuresService
from esi_client.models.get_corporations_corporation_id_titles200_ok import GetCorporationsCorporationIdTitles200Ok
from esi_client.models.get_corporations_corporation_id_wallets200_ok import GetCorporationsCorporationIdWallets200Ok
from esi_client.models.get_corporations_corporation_id_wallets_division_journal200_ok import GetCorporationsCorporationIdWalletsDivisionJournal200Ok
from esi_client.models.get_corporations_corporation_id_wallets_division_transactions200_ok import GetCorporationsCorporationIdWalletsDivisionTransactions200Ok
from esi_client.models.get_dogma_attributes_attribute_id_not_found import GetDogmaAttributesAttributeIdNotFound
from esi_client.models.get_dogma_attributes_attribute_id_ok import GetDogmaAttributesAttributeIdOk
from esi_client.models.get_dogma_dynamic_items_type_id_item_id_dogma_attribute import GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute
from esi_client.models.get_dogma_dynamic_items_type_id_item_id_dogma_effect import GetDogmaDynamicItemsTypeIdItemIdDogmaEffect
from esi_client.models.get_dogma_dynamic_items_type_id_item_id_not_found import GetDogmaDynamicItemsTypeIdItemIdNotFound
from esi_client.models.get_dogma_dynamic_items_type_id_item_id_ok import GetDogmaDynamicItemsTypeIdItemIdOk
from esi_client.models.get_dogma_effects_effect_id_modifier import GetDogmaEffectsEffectIdModifier
from esi_client.models.get_dogma_effects_effect_id_not_found import GetDogmaEffectsEffectIdNotFound
from esi_client.models.get_dogma_effects_effect_id_ok import GetDogmaEffectsEffectIdOk
from esi_client.models.get_fleets_fleet_id_members200_ok import GetFleetsFleetIdMembers200Ok
from esi_client.models.get_fleets_fleet_id_members_not_found import GetFleetsFleetIdMembersNotFound
from esi_client.models.get_fleets_fleet_id_not_found import GetFleetsFleetIdNotFound
from esi_client.models.get_fleets_fleet_id_ok import GetFleetsFleetIdOk
from esi_client.models.get_fleets_fleet_id_wings200_ok import GetFleetsFleetIdWings200Ok
from esi_client.models.get_fleets_fleet_id_wings_not_found import GetFleetsFleetIdWingsNotFound
from esi_client.models.get_fleets_fleet_id_wings_squad import GetFleetsFleetIdWingsSquad
from esi_client.models.get_fw_leaderboards_active_total_active_total import GetFwLeaderboardsActiveTotalActiveTotal
from esi_client.models.get_fw_leaderboards_active_total_active_total1 import GetFwLeaderboardsActiveTotalActiveTotal1
from esi_client.models.get_fw_leaderboards_characters_active_total_active_total import GetFwLeaderboardsCharactersActiveTotalActiveTotal
from esi_client.models.get_fw_leaderboards_characters_active_total_active_total1 import GetFwLeaderboardsCharactersActiveTotalActiveTotal1
from esi_client.models.get_fw_leaderboards_characters_kills import GetFwLeaderboardsCharactersKills
from esi_client.models.get_fw_leaderboards_characters_last_week_last_week import GetFwLeaderboardsCharactersLastWeekLastWeek
from esi_client.models.get_fw_leaderboards_characters_last_week_last_week1 import GetFwLeaderboardsCharactersLastWeekLastWeek1
from esi_client.models.get_fw_leaderboards_characters_ok import GetFwLeaderboardsCharactersOk
from esi_client.models.get_fw_leaderboards_characters_victory_points import GetFwLeaderboardsCharactersVictoryPoints
from esi_client.models.get_fw_leaderboards_characters_yesterday_yesterday import GetFwLeaderboardsCharactersYesterdayYesterday
from esi_client.models.get_fw_leaderboards_characters_yesterday_yesterday1 import GetFwLeaderboardsCharactersYesterdayYesterday1
from esi_client.models.get_fw_leaderboards_corporations_active_total_active_total import GetFwLeaderboardsCorporationsActiveTotalActiveTotal
from esi_client.models.get_fw_leaderboards_corporations_active_total_active_total1 import GetFwLeaderboardsCorporationsActiveTotalActiveTotal1
from esi_client.models.get_fw_leaderboards_corporations_kills import GetFwLeaderboardsCorporationsKills
from esi_client.models.get_fw_leaderboards_corporations_last_week_last_week import GetFwLeaderboardsCorporationsLastWeekLastWeek
from esi_client.models.get_fw_leaderboards_corporations_last_week_last_week1 import GetFwLeaderboardsCorporationsLastWeekLastWeek1
from esi_client.models.get_fw_leaderboards_corporations_ok import GetFwLeaderboardsCorporationsOk
from esi_client.models.get_fw_leaderboards_corporations_victory_points import GetFwLeaderboardsCorporationsVictoryPoints
from esi_client.models.get_fw_leaderboards_corporations_yesterday_yesterday import GetFwLeaderboardsCorporationsYesterdayYesterday
from esi_client.models.get_fw_leaderboards_corporations_yesterday_yesterday1 import GetFwLeaderboardsCorporationsYesterdayYesterday1
from esi_client.models.get_fw_leaderboards_kills import GetFwLeaderboardsKills
from esi_client.models.get_fw_leaderboards_last_week_last_week import GetFwLeaderboardsLastWeekLastWeek
from esi_client.models.get_fw_leaderboards_last_week_last_week1 import GetFwLeaderboardsLastWeekLastWeek1
from esi_client.models.get_fw_leaderboards_ok import GetFwLeaderboardsOk
from esi_client.models.get_fw_leaderboards_victory_points import GetFwLeaderboardsVictoryPoints
from esi_client.models.get_fw_leaderboards_yesterday_yesterday import GetFwLeaderboardsYesterdayYesterday
from esi_client.models.get_fw_leaderboards_yesterday_yesterday1 import GetFwLeaderboardsYesterdayYesterday1
from esi_client.models.get_fw_stats200_ok import GetFwStats200Ok
from esi_client.models.get_fw_stats_kills import GetFwStatsKills
from esi_client.models.get_fw_stats_victory_points import GetFwStatsVictoryPoints
from esi_client.models.get_fw_systems200_ok import GetFwSystems200Ok
from esi_client.models.get_fw_wars200_ok import GetFwWars200Ok
from esi_client.models.get_incursions200_ok import GetIncursions200Ok
from esi_client.models.get_industry_facilities200_ok import GetIndustryFacilities200Ok
from esi_client.models.get_industry_systems200_ok import GetIndustrySystems200Ok
from esi_client.models.get_industry_systems_cost_indice import GetIndustrySystemsCostIndice
from esi_client.models.get_insurance_prices200_ok import GetInsurancePrices200Ok
from esi_client.models.get_insurance_prices_level import GetInsurancePricesLevel
from esi_client.models.get_killmails_killmail_id_killmail_hash_attacker import GetKillmailsKillmailIdKillmailHashAttacker
from esi_client.models.get_killmails_killmail_id_killmail_hash_item import GetKillmailsKillmailIdKillmailHashItem
from esi_client.models.get_killmails_killmail_id_killmail_hash_items_item import GetKillmailsKillmailIdKillmailHashItemsItem
from esi_client.models.get_killmails_killmail_id_killmail_hash_ok import GetKillmailsKillmailIdKillmailHashOk
from esi_client.models.get_killmails_killmail_id_killmail_hash_position import GetKillmailsKillmailIdKillmailHashPosition
from esi_client.models.get_killmails_killmail_id_killmail_hash_unprocessable_entity import GetKillmailsKillmailIdKillmailHashUnprocessableEntity
from esi_client.models.get_killmails_killmail_id_killmail_hash_victim import GetKillmailsKillmailIdKillmailHashVictim
from esi_client.models.get_loyalty_stores_corporation_id_offers200_ok import GetLoyaltyStoresCorporationIdOffers200Ok
from esi_client.models.get_loyalty_stores_corporation_id_offers_not_found import GetLoyaltyStoresCorporationIdOffersNotFound
from esi_client.models.get_loyalty_stores_corporation_id_offers_required_item import GetLoyaltyStoresCorporationIdOffersRequiredItem
from esi_client.models.get_markets_groups_market_group_id_not_found import GetMarketsGroupsMarketGroupIdNotFound
from esi_client.models.get_markets_groups_market_group_id_ok import GetMarketsGroupsMarketGroupIdOk
from esi_client.models.get_markets_prices200_ok import GetMarketsPrices200Ok
from esi_client.models.get_markets_region_id_history200_ok import GetMarketsRegionIdHistory200Ok
from esi_client.models.get_markets_region_id_history_error520 import GetMarketsRegionIdHistoryError520
from esi_client.models.get_markets_region_id_history_not_found import GetMarketsRegionIdHistoryNotFound
from esi_client.models.get_markets_region_id_history_unprocessable_entity import GetMarketsRegionIdHistoryUnprocessableEntity
from esi_client.models.get_markets_region_id_orders200_ok import GetMarketsRegionIdOrders200Ok
from esi_client.models.get_markets_region_id_orders_not_found import GetMarketsRegionIdOrdersNotFound
from esi_client.models.get_markets_region_id_orders_unprocessable_entity import GetMarketsRegionIdOrdersUnprocessableEntity
from esi_client.models.get_markets_structures_structure_id200_ok import GetMarketsStructuresStructureId200Ok
from esi_client.models.get_opportunities_groups_group_id_ok import GetOpportunitiesGroupsGroupIdOk
from esi_client.models.get_opportunities_tasks_task_id_ok import GetOpportunitiesTasksTaskIdOk
from esi_client.models.get_route_origin_destination_not_found import GetRouteOriginDestinationNotFound
from esi_client.models.get_sovereignty_campaigns200_ok import GetSovereigntyCampaigns200Ok
from esi_client.models.get_sovereignty_campaigns_participant import GetSovereigntyCampaignsParticipant
from esi_client.models.get_sovereignty_map200_ok import GetSovereigntyMap200Ok
from esi_client.models.get_sovereignty_structures200_ok import GetSovereigntyStructures200Ok
from esi_client.models.get_status_ok import GetStatusOk
from esi_client.models.get_universe_ancestries200_ok import GetUniverseAncestries200Ok
from esi_client.models.get_universe_asteroid_belts_asteroid_belt_id_not_found import GetUniverseAsteroidBeltsAsteroidBeltIdNotFound
from esi_client.models.get_universe_asteroid_belts_asteroid_belt_id_ok import GetUniverseAsteroidBeltsAsteroidBeltIdOk
from esi_client.models.get_universe_asteroid_belts_asteroid_belt_id_position import GetUniverseAsteroidBeltsAsteroidBeltIdPosition
from esi_client.models.get_universe_bloodlines200_ok import GetUniverseBloodlines200Ok
from esi_client.models.get_universe_categories_category_id_not_found import GetUniverseCategoriesCategoryIdNotFound
from esi_client.models.get_universe_categories_category_id_ok import GetUniverseCategoriesCategoryIdOk
from esi_client.models.get_universe_constellations_constellation_id_not_found import GetUniverseConstellationsConstellationIdNotFound
from esi_client.models.get_universe_constellations_constellation_id_ok import GetUniverseConstellationsConstellationIdOk
from esi_client.models.get_universe_constellations_constellation_id_position import GetUniverseConstellationsConstellationIdPosition
from esi_client.models.get_universe_factions200_ok import GetUniverseFactions200Ok
from esi_client.models.get_universe_graphics_graphic_id_not_found import GetUniverseGraphicsGraphicIdNotFound
from esi_client.models.get_universe_graphics_graphic_id_ok import GetUniverseGraphicsGraphicIdOk
from esi_client.models.get_universe_groups_group_id_not_found import GetUniverseGroupsGroupIdNotFound
from esi_client.models.get_universe_groups_group_id_ok import GetUniverseGroupsGroupIdOk
from esi_client.models.get_universe_moons_moon_id_not_found import GetUniverseMoonsMoonIdNotFound
from esi_client.models.get_universe_moons_moon_id_ok import GetUniverseMoonsMoonIdOk
from esi_client.models.get_universe_moons_moon_id_position import GetUniverseMoonsMoonIdPosition
from esi_client.models.get_universe_planets_planet_id_not_found import GetUniversePlanetsPlanetIdNotFound
from esi_client.models.get_universe_planets_planet_id_ok import GetUniversePlanetsPlanetIdOk
from esi_client.models.get_universe_planets_planet_id_position import GetUniversePlanetsPlanetIdPosition
from esi_client.models.get_universe_races200_ok import GetUniverseRaces200Ok
from esi_client.models.get_universe_regions_region_id_not_found import GetUniverseRegionsRegionIdNotFound
from esi_client.models.get_universe_regions_region_id_ok import GetUniverseRegionsRegionIdOk
from esi_client.models.get_universe_schematics_schematic_id_not_found import GetUniverseSchematicsSchematicIdNotFound
from esi_client.models.get_universe_schematics_schematic_id_ok import GetUniverseSchematicsSchematicIdOk
from esi_client.models.get_universe_stargates_stargate_id_destination import GetUniverseStargatesStargateIdDestination
from esi_client.models.get_universe_stargates_stargate_id_not_found import GetUniverseStargatesStargateIdNotFound
from esi_client.models.get_universe_stargates_stargate_id_ok import GetUniverseStargatesStargateIdOk
from esi_client.models.get_universe_stargates_stargate_id_position import GetUniverseStargatesStargateIdPosition
from esi_client.models.get_universe_stars_star_id_ok import GetUniverseStarsStarIdOk
from esi_client.models.get_universe_stations_station_id_not_found import GetUniverseStationsStationIdNotFound
from esi_client.models.get_universe_stations_station_id_ok import GetUniverseStationsStationIdOk
from esi_client.models.get_universe_stations_station_id_position import GetUniverseStationsStationIdPosition
from esi_client.models.get_universe_structures_structure_id_not_found import GetUniverseStructuresStructureIdNotFound
from esi_client.models.get_universe_structures_structure_id_ok import GetUniverseStructuresStructureIdOk
from esi_client.models.get_universe_structures_structure_id_position import GetUniverseStructuresStructureIdPosition
from esi_client.models.get_universe_system_jumps200_ok import GetUniverseSystemJumps200Ok
from esi_client.models.get_universe_system_kills200_ok import GetUniverseSystemKills200Ok
from esi_client.models.get_universe_systems_system_id_not_found import GetUniverseSystemsSystemIdNotFound
from esi_client.models.get_universe_systems_system_id_ok import GetUniverseSystemsSystemIdOk
from esi_client.models.get_universe_systems_system_id_planet import GetUniverseSystemsSystemIdPlanet
from esi_client.models.get_universe_systems_system_id_position import GetUniverseSystemsSystemIdPosition
from esi_client.models.get_universe_types_type_id_dogma_attribute import GetUniverseTypesTypeIdDogmaAttribute
from esi_client.models.get_universe_types_type_id_dogma_effect import GetUniverseTypesTypeIdDogmaEffect
from esi_client.models.get_universe_types_type_id_not_found import GetUniverseTypesTypeIdNotFound
from esi_client.models.get_universe_types_type_id_ok import GetUniverseTypesTypeIdOk
from esi_client.models.get_wars_war_id_aggressor import GetWarsWarIdAggressor
from esi_client.models.get_wars_war_id_ally import GetWarsWarIdAlly
from esi_client.models.get_wars_war_id_defender import GetWarsWarIdDefender
from esi_client.models.get_wars_war_id_killmails200_ok import GetWarsWarIdKillmails200Ok
from esi_client.models.get_wars_war_id_killmails_unprocessable_entity import GetWarsWarIdKillmailsUnprocessableEntity
from esi_client.models.get_wars_war_id_ok import GetWarsWarIdOk
from esi_client.models.get_wars_war_id_unprocessable_entity import GetWarsWarIdUnprocessableEntity
from esi_client.models.internal_server_error import InternalServerError
from esi_client.models.post_characters_affiliation200_ok import PostCharactersAffiliation200Ok
from esi_client.models.post_characters_character_id_assets_locations200_ok import PostCharactersCharacterIdAssetsLocations200Ok
from esi_client.models.post_characters_character_id_assets_locations_position import PostCharactersCharacterIdAssetsLocationsPosition
from esi_client.models.post_characters_character_id_assets_names200_ok import PostCharactersCharacterIdAssetsNames200Ok
from esi_client.models.post_characters_character_id_contacts_error520 import PostCharactersCharacterIdContactsError520
from esi_client.models.post_characters_character_id_fittings_created import PostCharactersCharacterIdFittingsCreated
from esi_client.models.post_characters_character_id_fittings_fitting import PostCharactersCharacterIdFittingsFitting
from esi_client.models.post_characters_character_id_fittings_item import PostCharactersCharacterIdFittingsItem
from esi_client.models.post_characters_character_id_mail_error520 import PostCharactersCharacterIdMailError520
from esi_client.models.post_characters_character_id_mail_labels_label import PostCharactersCharacterIdMailLabelsLabel
from esi_client.models.post_characters_character_id_mail_mail import PostCharactersCharacterIdMailMail
from esi_client.models.post_characters_character_id_mail_recipient import PostCharactersCharacterIdMailRecipient
from esi_client.models.post_corporations_corporation_id_assets_locations200_ok import PostCorporationsCorporationIdAssetsLocations200Ok
from esi_client.models.post_corporations_corporation_id_assets_locations_not_found import PostCorporationsCorporationIdAssetsLocationsNotFound
from esi_client.models.post_corporations_corporation_id_assets_locations_position import PostCorporationsCorporationIdAssetsLocationsPosition
from esi_client.models.post_corporations_corporation_id_assets_names200_ok import PostCorporationsCorporationIdAssetsNames200Ok
from esi_client.models.post_corporations_corporation_id_assets_names_not_found import PostCorporationsCorporationIdAssetsNamesNotFound
from esi_client.models.post_fleets_fleet_id_members_invitation import PostFleetsFleetIdMembersInvitation
from esi_client.models.post_fleets_fleet_id_members_not_found import PostFleetsFleetIdMembersNotFound
from esi_client.models.post_fleets_fleet_id_members_unprocessable_entity import PostFleetsFleetIdMembersUnprocessableEntity
from esi_client.models.post_fleets_fleet_id_wings_created import PostFleetsFleetIdWingsCreated
from esi_client.models.post_fleets_fleet_id_wings_not_found import PostFleetsFleetIdWingsNotFound
from esi_client.models.post_fleets_fleet_id_wings_wing_id_squads_created import PostFleetsFleetIdWingsWingIdSquadsCreated
from esi_client.models.post_fleets_fleet_id_wings_wing_id_squads_not_found import PostFleetsFleetIdWingsWingIdSquadsNotFound
from esi_client.models.post_ui_openwindow_newmail_new_mail import PostUiOpenwindowNewmailNewMail
from esi_client.models.post_ui_openwindow_newmail_unprocessable_entity import PostUiOpenwindowNewmailUnprocessableEntity
from esi_client.models.post_universe_ids_agent import PostUniverseIdsAgent
from esi_client.models.post_universe_ids_alliance import PostUniverseIdsAlliance
from esi_client.models.post_universe_ids_character import PostUniverseIdsCharacter
from esi_client.models.post_universe_ids_constellation import PostUniverseIdsConstellation
from esi_client.models.post_universe_ids_corporation import PostUniverseIdsCorporation
from esi_client.models.post_universe_ids_faction import PostUniverseIdsFaction
from esi_client.models.post_universe_ids_inventory_type import PostUniverseIdsInventoryType
from esi_client.models.post_universe_ids_ok import PostUniverseIdsOk
from esi_client.models.post_universe_ids_region import PostUniverseIdsRegion
from esi_client.models.post_universe_ids_station import PostUniverseIdsStation
from esi_client.models.post_universe_ids_system import PostUniverseIdsSystem
from esi_client.models.post_universe_names200_ok import PostUniverseNames200Ok
from esi_client.models.post_universe_names_not_found import PostUniverseNamesNotFound
from esi_client.models.put_characters_character_id_calendar_event_id_response import PutCharactersCharacterIdCalendarEventIdResponse
from esi_client.models.put_characters_character_id_mail_mail_id_contents import PutCharactersCharacterIdMailMailIdContents
from esi_client.models.put_fleets_fleet_id_members_member_id_movement import PutFleetsFleetIdMembersMemberIdMovement
from esi_client.models.put_fleets_fleet_id_members_member_id_not_found import PutFleetsFleetIdMembersMemberIdNotFound
from esi_client.models.put_fleets_fleet_id_members_member_id_unprocessable_entity import PutFleetsFleetIdMembersMemberIdUnprocessableEntity
from esi_client.models.put_fleets_fleet_id_new_settings import PutFleetsFleetIdNewSettings
from esi_client.models.put_fleets_fleet_id_not_found import PutFleetsFleetIdNotFound
from esi_client.models.put_fleets_fleet_id_squads_squad_id_naming import PutFleetsFleetIdSquadsSquadIdNaming
from esi_client.models.put_fleets_fleet_id_squads_squad_id_not_found import PutFleetsFleetIdSquadsSquadIdNotFound
from esi_client.models.put_fleets_fleet_id_wings_wing_id_naming import PutFleetsFleetIdWingsWingIdNaming
from esi_client.models.put_fleets_fleet_id_wings_wing_id_not_found import PutFleetsFleetIdWingsWingIdNotFound
from esi_client.models.service_unavailable import ServiceUnavailable
from esi_client.models.unauthorized import Unauthorized
