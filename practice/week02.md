<!DOCTYPE html>
<!-- saved from url=(0068)https://github.com/20260160/my-first-game/blob/main/my-first-game.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" class="js-focus-visible" data-js-focus-visible="" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style><style>
:root {
  --fontStack-monospace: "Monaspace Neon", ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace !important;
}
</style>




  
    
  <link rel="dns-prefetch" href="https://github.githubassets.com/">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com/" crossorigin="">
  <link rel="preconnect" href="https://avatars.githubusercontent.com/">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/light-0c8222dcd7a4f9b7.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/dark-fc6eec18532c3ae0.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-51c0c6e0c085cc0f.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-4dd12c5689d6b012.css"><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-dfa0c9e22ba6ba2b.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-9fd9c8859395d1a8.css"><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-9c32304a2a8ac631.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-96d7b2bab5a6ae4e.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-0c6ca283d4d35cea.css"><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-2dc46b4919fae81e.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-271332ec9362e8d3.css"><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-eb5bb84e91d6d553.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-f3aa862f2ac7ead2.css"><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-206b6b93f856629b.css">

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/primer-primitives-10bf9dd67e3d70bd.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/primer-0fcd9af82350aeda.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/global-a40b6ece39d70d4a.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/github-b02a278369fa132e.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/repository-6ec84ae2261fecf8.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/code-2d31826944fd3be8.css">

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","actions_custom_images_storage_billing_ui_visibility","actions_image_version_event","actions_scheduled_workflow_timezone_enabled","actions_workflow_language_service_allow_case_function","alternate_user_config_repo","arianotify_comprehensive_migration","batch_suggested_changes","billing_discount_threshold_notification","billing_ui_budget_pagination_enabled","close_pr_side_panel","codemirror_inp_optimizations","codeowners_validation_in_diff","codespaces_prebuild_region_target_update","coding_agent_model_selection","coding_agent_model_selection_all_skus","comment_viewer_copy_raw_markdown","comments_panel_issue_comments","contentful_primer_code_blocks","copilot_agent_image_upload","copilot_agent_snippy","copilot_api_agentic_issue_marshal_yaml","copilot_ask_mode_dropdown","copilot_chat_attach_multiple_images","copilot_chat_clear_model_selection_for_default_change","copilot_chat_disable_model_picker_while_streaming","copilot_chat_enable_tool_call_logs","copilot_chat_explain_error_user_model","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_repository_picker","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_cli_install_cta","copilot_code_review_batch_apply_suggestions","copilot_coding_agent_free_users_exp","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_sql_server_logo","copilot_features_zed_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_embedded","copilot_immersive_file_block_transition_open","copilot_immersive_file_preview_keep_mounted","copilot_immersive_job_result_preview","copilot_immersive_layout_routes","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_issue_list_show_more","copilot_mc_cli_resume_any_users_task","copilot_mission_control_always_send_integration_id","copilot_mission_control_cli_resume_with_task_id","copilot_mission_control_custom_agent_group","copilot_mission_control_decoupled_mode","copilot_mission_control_decoupled_mode_agent_tooltip","copilot_mission_control_initial_data_spinner","copilot_mission_control_post_session_chat_model_picker","copilot_mission_control_scroll_to_bottom_button","copilot_mission_control_task_alive_updates","copilot_org_policy_page_focus_mode","copilot_premium_request_quotas","copilot_redirect_header_button_to_agents","copilot_resource_panel","copilot_scroll_preview_tabs","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_pagination","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_swe_agent_hide_model_picker_if_only_auto","copilot_swe_agent_pr_comment_model_picker","copilot_swe_agent_use_subagents","copilot_task_api_github_rest_style","copilot_unconfigured_is_inherited","copilot_usage_metrics_ga","copilot_workbench_slim_line_top_tabs","custom_instructions_file_references","custom_properties_consolidate_default_value_input","dashboard_add_updated_desc","dashboard_indexeddb_caching","dashboard_lists_max_age_filter","dashboard_universe_2025","dashboard_universe_2025_feedback_dialog","dead_click_detection","fgpat_permissions_selector_redesign","flex_cta_groups_mvp","github_models_scheduled_hydro_events","global_nav_react","global_nav_unified_payload","hide_groups_list_for_few_groups","hyperspace_2025_logged_out_batch_1","hyperspace_2025_logged_out_batch_2","hyperspace_2025_logged_out_batch_3","ipm_global_transactional_message_agents","ipm_global_transactional_message_copilot","ipm_global_transactional_message_issues","ipm_global_transactional_message_prs","ipm_global_transactional_message_repos","ipm_global_transactional_message_spaces","issue_cca_modal_open","issue_cca_visualization","issue_fields_global_search","issue_fields_visibility_settings","issues_dashboard_inp_optimization","issues_diff_based_label_updates","issues_expanded_file_types","issues_index_semantic_search","issues_lazy_load_comment_box_suggestions","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_include_bots_in_pickers","issues_react_prohibit_title_fallback","issues_react_ui_feedback","issues_search_type_gql","landing_pages_ninetailed","landing_pages_web_vitals_tracking","lifecycle_label_name_updates","load_paginated_threads_on_diff","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_live_update_hovercard","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","merge_status_header_feedback","mission_control_retry_on_401","nux_dashboard_refresh_scoped_portal","oauth_authorize_clickjacking_protection","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","pr_sfv_new_diff_fetch","primer_react_action_menu_display_in_viewport_inside_dialog","primer_react_css_has_selector_perf","primer_react_spinner_synchronize_animations","prs_checks_react","prs_conversations_react","prs_docked_side_panel","prs_live_updates_issue_comments","prx_files","prx_merge_status_button_alt_logic","pull_request_edit_button_redesign","pull_request_files_accurate_size_estimates","pull_request_files_virtualization","pull_request_merge_status_button","react_blob_overlay","repository_suggester_elastic_search","ruleset_deletion_confirmation","sample_network_conn_type","secret_scanning_pattern_alerts_link","session_logs_ungroup_reasoning_text","site_features_copilot_universe","site_homepage_collaborate_video","spark_prompt_secret_scanning","spark_server_connection_status","suppress_automated_browser_vitals","suppress_non_representative_vitals","viewscreen_sandbox","webp_support","workbench_store_readonly"],"login":"20260160","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="module" src="./week02_files/wp-runtime-ed508127a539a20f.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/85924-d72bd3bf2ebf2b33.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/28839-c0b8ec9e4855e70d.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/34646-e2c38a6244e0673e.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/environment-d9bacfd0e507cc58.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/runtime-helpers-9ca289a20b4287f3.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/2966-7fae197fcc122033.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/96232-81264b2e484eeea3.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/41013-98ec62b138074b3c.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/51210-4f6b60f1e56caf0b.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/77313-833d857459e22419.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/23039-9d3ed8a305267b36.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/8601-bd8c9578beeca5fa.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/46740-6ff37d25440dfd5f.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/52375-7184639d75711668.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/github-elements-17007c6e1a0ff4e7.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/element-registry-0b32e5b1d96edd71.js.다운로드" defer="defer"></script>




<script crossorigin="anonymous" type="module" src="./week02_files/61110-91a6e672e6c52371.js.다운로드" defer="defer"></script>

<script crossorigin="anonymous" type="module" src="./week02_files/26533-be3434b1ad736595.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/97745-17bf40209ad1b441.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/89155-cd29998a39b55887.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/50686-203ca12c697307e6.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/46779-a5e6403e1f8c73d8.js.다운로드" defer="defer"></script>


<script crossorigin="anonymous" type="module" src="./week02_files/1108-d04e2e16dc98da37.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/18597-6dc8f1f774696932.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/15625-05373890466bf366.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/48527-5de266b1da5c2e34.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/28703-c1456f1aa61b245d.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/99328-91354dc331fd4cdd.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/37943-3c619d65dd869b67.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/91184-657c34dc2b380c4c.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/97232-829cc8b566d31458.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/87774-cb19ae155ee3c918.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/27493-4c94010ef4ae1e22.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/56889-3812304955862655.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/2013-126bbbb468be7e3b.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/81564-fd44bec50cee3386.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/behaviors-e6ee0d9220c00fe9.js.다운로드" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/react-core.364eade98ee7744f.module.css">
<script crossorigin="anonymous" type="module" src="./week02_files/81863-518132d704f3d667.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/notifications-global-f520baa344c4ccaf.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/34140-23b7e387fad525e7.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/code-menu-967536ac6b424d39.js.다운로드" defer="defer"></script>
  
  




<script crossorigin="anonymous" type="module" src="./week02_files/7463-99acaf07f7d6502a.js.다운로드" defer="defer"></script>

<script crossorigin="anonymous" type="module" src="./week02_files/32769-5b6132406b21f557.js.다운로드" defer="defer"></script>

<script crossorigin="anonymous" type="module" src="./week02_files/50938-14e2342a61983e31.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/13220-130b6ffd242c3cfe.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/76707-4162f37ba2ea87f0.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/90255-d17e0fa6c678f732.js.다운로드" defer="defer"></script>





<script crossorigin="anonymous" type="module" src="./week02_files/36600-cf085c136387bf33.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/18222-4323474564e5aecc.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/4916-4cfd8dd432dcda55.js.다운로드" defer="defer"></script>

<script crossorigin="anonymous" type="module" src="./week02_files/17363-4f4436e161accb3b.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/1097-53c0518f93b2279f.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/13333-e757dcf2a85f7470.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/73061-5015907614c92371.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/32999-1c9f470712601c9e.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/20201-94a027eac40ef4a9.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/65573-7c9c3cc68ec0eb12.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/28599-e61e51a1696740ab.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/49972-75e32f17cfa68bd1.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/96043-5a2ca48072155e28.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/96306-9be591ee0e419d2e.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/26497-5815c1ce9a63d716.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/66205-b737eb30140ad669.js.다운로드" defer="defer"></script>

<script crossorigin="anonymous" type="module" src="./week02_files/43690-bd2a704c24665aee.js.다운로드" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./week02_files/code-view-d603028d70ed8c2b.js.다운로드" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/primer-react-css.da05312be74eac16.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/96043.a4311aaf5caadfff.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/66205.b5045207bd90f6b9.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/43690.74be507a186241b9.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/code-view.c4eb72defe48d8c4.module.css">


  <title>my-first-game/my-first-game.py at main · 20260160/my-first-game</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient="">
  <meta name="route-controller" content="blob" data-turbo-transient="">
  <meta name="route-action" content="show" data-turbo-transient="">
  <meta name="fetch-nonce" content="v2:14aa3a79-a468-98ae-b9a1-435cf737e2dc">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="CDA0:380107:EECB53:14858CA:69C8E443" data-turbo-transient="true"><meta name="html-safe-nonce" content="6994848205bbf7a1f40a2bba927c7e2b8a20d0177b703eef16216864a17d99a1" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS8iLCJyZXF1ZXN0X2lkIjoiQ0RBMDozODAxMDc6RUVDQjUzOjE0ODU4Q0E6NjlDOEU0NDMiLCJ2aXNpdG9yX2lkIjoiOTc4NzM2NjI5NDk1MTkzNjk3IiwicmVnaW9uX2VkZ2UiOiJrb3JlYWNlbnRyYWwiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="564e3d627a0c8e469d774b7788b3cdb703f9845d7dd355e6f757bd1afe5457f0" data-turbo-transient="true">


    <meta name="hovercard-subject-tag" content="repository:1183046968" data-turbo-transient="">


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true">
  

  <meta name="selected-link" value="repo_source" data-turbo-transient="">
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="268550804"><meta name="octolytics-actor-login" content="20260160"><meta name="octolytics-actor-hash" content="38ec46fc66bd0ae2d387447ff3d3d0e6cf7a372c32dcd9a0768bd0466116d586">





  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true">

  




    <meta name="user-login" content="20260160">

  <link rel="sudo-modal" href="https://github.com/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Contribute to 20260160/my-first-game development by creating an account on GitHub.">

      <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/20260160/my-first-game/blob/main/my-first-game.py">

      <meta name="twitter:image" content="https://opengraph.githubassets.com/49f368912ab86cdebbb3526f8a83dd4bf19878dbab248f64330a8fbb7c8859d9/20260160/my-first-game"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="my-first-game/my-first-game.py at main · 20260160/my-first-game"><meta name="twitter:description" content="Contribute to 20260160/my-first-game development by creating an account on GitHub.">
  <meta property="og:image" content="https://opengraph.githubassets.com/49f368912ab86cdebbb3526f8a83dd4bf19878dbab248f64330a8fbb7c8859d9/20260160/my-first-game"><meta property="og:image:alt" content="Contribute to 20260160/my-first-game development by creating an account on GitHub."><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="my-first-game/my-first-game.py at main · 20260160/my-first-game"><meta property="og:url" content="https://github.com/20260160/my-first-game/blob/main/my-first-game.py"><meta property="og:description" content="Contribute to 20260160/my-first-game development by creating an account on GitHub.">
  


      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/268550804/ws?session=eyJ2IjoiVjMiLCJ1IjoyNjg1NTA4MDQsInMiOjIwMjMwMzU2ODgsImMiOjI0OTkzODQ3MjgsInQiOjE3NzQ3NzMzMTV9--2833bef2f3f9996d5f9ab738a8b15df678dfe3a03b094009ea7572c30392e266" data-refresh-url="/_alive" data-session-id="11b03259b766f022b8737043d96d43b64bb71ad21b6e5818efab5dcfb7fab635">
      <link rel="shared-web-socket-src" href="https://github.com/assets-cdn/worker/socket-worker-312129489ba60057.js">

      <link rel="service-worker-src" href="https://github.com/assets-cdn/worker/service-worker-dae625aa82e7855a.js?current_user=20260160&amp;errors_url=https%3A%2F%2Fapi.github.com%2F_private%2Fbrowser%2Ferrors&amp;release=51d2e33e3d1e4839c3ced5f8e35c7a47d3a60f32&amp;actor_id=268550804&amp;is_staff=false&amp;analytics_collector_url=https%3A%2F%2Fcollector.github.com%2Fgithub%2Fcollect">

      <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">
      <meta name="hovercards-preference" content="true">
      <meta name="announcement-preference-hovercard" content="true">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="c1de8ab04ff31336e20ace8fdce64832afe5069bf456045fffd1a5c7e4507a8b" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="568c098497d98702bac1642a2a853732a047a6ced28eabd3e15d50041a890235" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="2a11dc2eae08fab707a6ec4f9b210809c57fcffc99ec34a2e6f0046296cc07e6" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="630d8b00b9650984e288302f44cc14c439058de689aae3efd81309196af4d0a8" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient="">

    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/20260160/my-first-game git https://github.com/20260160/my-first-game.git">

  <meta name="octolytics-dimension-user_id" content="268550804"><meta name="octolytics-dimension-user_login" content="20260160"><meta name="octolytics-dimension-repository_id" content="1183046968"><meta name="octolytics-dimension-repository_nwo" content="20260160/my-first-game"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="1183046968"><meta name="octolytics-dimension-repository_network_root_nwo" content="20260160/my-first-game">



    

    <meta name="turbo-body-classes" content="logged-in env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="51d2e33e3d1e4839c3ced5f8e35c7a47d3a60f32">
  <meta name="ui-target" content="full">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg" data-base-href="https://github.githubassets.com/favicons/favicon">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark">

  <meta name="msapplication-TileImage" content="/windows-tile.png">
  <meta name="msapplication-TileColor" content="#ffffff">

  <link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials">

  <link rel="stylesheet" type="text/css" href="./week02_files/81758.c3d0cf69fea2352a.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./week02_files/38963.f70dfea92b138b01.module.css" crossorigin="anonymous"><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link rel="stylesheet" type="text/css" href="./week02_files/10973.23b6b7b72692bb9f.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./week02_files/53839.52201ac8c146881f.module.css" crossorigin="anonymous"><style data-styled="active" data-styled-version="5.3.11"></style><link rel="stylesheet" type="text/css" href="./week02_files/61975.b129f60ae2849f5b.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./week02_files/26107.41ae2139f7c50636.module.css" crossorigin="anonymous"></head>

  <body class="logged-in env-production page-responsive" style="word-wrap: break-word;" data-dialog-scroll-optimized="">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent=""></div>
      

    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/20260160/my-first-game/blob/main/my-first-game.py#start-of-content" data-skip-target-assigned="false" class="tmp-p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/primer-react-css.da05312be74eac16.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/keyboard-shortcuts-dialog.76a47c12aca9fa78.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA__r_e___">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>





      

          

                  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/primer-react-css.da05312be74eac16.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./week02_files/global-nav-bar.28744a875044f950.module.css">

<react-partial partial-name="global-nav-bar" data-ssr="true" data-attempted-ssr="true" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"contextRegion":{"crumbs":[{"crumb_type":"user","label":"20260160","is_root":false,"href":"/20260160"},{"crumb_type":"repository","label":"my-first-game","is_root":false,"href":"/20260160/my-first-game"}],"localNavigation":[{"id":"code","icon":"code","label":"Code","href":"/20260160/my-first-game","selectedLinks":["repo_source","repo_downloads","repo_commits","repo_releases","repo_tags","repo_branches","repo_packages","repo_deployments","repo_attestations"],"popoverTarget":false,"commandId":"repositories:go-to-code","reactNav":{"appTarget":"code-view","anchor":"code-view-repo-link"},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"issues","icon":"issue-opened","label":"Issues","href":"/20260160/my-first-game/issues","selectedLinks":["repo_issues","repo_labels","repo_milestones"],"count":0,"popoverTarget":false,"commandId":"repositories:go-to-issues","reactNav":{"appTarget":"issues-react","anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"pull-requests","icon":"git-pull-request","label":"Pull requests","href":"/20260160/my-first-game/pulls","selectedLinks":["repo_pulls","checks"],"count":0,"popoverTarget":false,"commandId":"repositories:go-to-pull-requests","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"actions","icon":"play","label":"Actions","href":"/20260160/my-first-game/actions","selectedLinks":["repo_actions"],"popoverTarget":false,"commandId":"repositories:go-to-actions","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"projects","icon":"table","label":"Projects","href":"/20260160/my-first-game/projects","selectedLinks":["repo_projects","new_repo_project","repo_project"],"popoverTarget":false,"commandId":"repositories:go-to-projects","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"wiki","icon":"book","label":"Wiki","href":"/20260160/my-first-game/wiki","selectedLinks":["repo_wiki"],"popoverTarget":false,"commandId":"repositories:go-to-wiki","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"security","icon":"shield","label":"Security","href":"/20260160/my-first-game/security","selectedLinks":["security","overview","alerts","policy","token_scanning","code_scanning"],"count":0,"popoverTarget":false,"commandId":"repositories:go-to-security","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"insights","icon":"graph","label":"Insights","href":"/20260160/my-first-game/pulse","selectedLinks":["repo_graphs","repo_contributors","dependency_graph","dependabot_updates","pulse","people","community"],"popoverTarget":false,"commandId":"repositories:go-to-insights","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"settings","icon":"gear","label":"Settings","href":"/20260160/my-first-game/settings","selectedLinks":["code_review_limits","code_quality","codespaces_repository_settings","collaborators","custom_tabs","github_models_repo_settings","hooks","integration_installations","interaction_limits","issue_template_editor","key_links_settings","license_policy","notifications","repo_announcements","repo_branch_settings","repo_custom_properties","repo_keys_settings","repo_pages_settings","repo_protected_tags_settings","repo_rule_insights","repo_rule_insights_dashboard","repo_rules_bypass_requests","repo_rulesets","repo_settings_copilot_coding_guidelines","repo_settings_copilot_content_exclusion","repo_settings_copilot_swe_agent","repo_settings","reported_content","repository_actions_settings_add_new_runner","repository_actions_settings_general","repository_actions_settings_runner_details","repository_actions_settings_runners","repository_actions_settings","repository_actions_settings_policies","repository_actions_settings_oidc_configuration","repository_environments","role_details","secrets_settings_actions","secrets_settings_agents","secrets_settings_codespaces","secrets_settings_dependabot","secrets","security_analysis","security_products"],"popoverTarget":false,"commandId":"repositories:go-to-settings","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}}],"localNavigationUpdateChannel":"eyJjIjoicmVwbzoxMTgzMDQ2OTY4OnVzZXI6MjY4NTUwODA0OnNldHRpbmdzIiwidCI6MTc3NDc3MzMxNX0=--c96d99be4cee8c203c717ec9267f29d0eac4b1f2681918ffede1862e970be540","selectedLink":"repo_source"},"userMenu":{"owner":{"login":"20260160","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/268550804?v=4"}},"headerLogo":{"href":"/","aria-label":"Homepage "},"notifications":{"indicatorMode":"none","websocketChannel":"eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MjY4NTUwODA0IiwidCI6MTc3NDc3MzMxNX0=--2fe8ed746566712abcc803ef6175453d0c99a80682f648b77824e53bbed0ab32","fetchIndicatorSrc":"/notifications/indicator","fetchIndicatorEnabled":true},"issues":{"href":"/issues"},"pulls":{"href":"/pulls"},"contributedRepos":{"show":true,"href":"/repos"},"copilot":{"show":true,"showAgentsButton":false,"copilotChatUrl":"/github-copilot/chat?skip_anchor=true","copilotApiUrl":"https://api.individual.githubcopilot.com"},"search":{"show":true,"showCommandPalette":false,"isSearchPage":false,"isJumpToSearch":false,"searchContext":{"scope":"repo:20260160/my-first-game","current_repo_name":"my-first-game","current_repo_nwo":"20260160/my-first-game","user_id":"20260160"}},"enterpriseBanner":{"show":false},"globalTransactionalMessage":{"segments":[{"type":"text","content":"On April 24 we'll start using GitHub Copilot interaction data for AI model training unless you opt out. "},{"type":"link","content":"Review this update","href":"https://gh.io/AAzfaht"},{"type":"text","content":" and manage your preferences in your "},{"type":"link","content":"GitHub account settings","href":"https://github.com/settings/copilot/features"},{"type":"text","content":"."}],"dismissPath":"/settings/dismiss-notice/dashboard_jan_2026_privacy_copilot_nudge?nudge=true","analytics":{"category":"copilot_privacy_update_jan_2026","group":"","location":"global"}},"payloadsUrl":"/_global-navigation/payloads.json?current_repo_nwo=20260160%2Fmy-first-game\u0026repository=my-first-game\u0026return_to=https%3A%2F%2Fgithub.com%2F20260160%2Fmy-first-game%2Fblob%2Fmain%2Fmy-first-game.py\u0026user_id=20260160"}}</script>
  <div data-target="react-partial.reactRoot"><link rel="preload" as="image" href="./week02_files/268550804"><header role="banner" aria-label="Global Navigation Menu" class="GlobalNav styles-module__appHeader__YzYWk prc-Stack-Stack-UQ9k6" data-gap="none" data-direction="vertical" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="none"><div class="prc-Stack-Stack-UQ9k6" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="center" data-padding="none"><div data-testid="top-nav-left" class="styles-module__left__Fylw7 styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-loading-wrapper="true"><button data-component="IconButton" type="button" aria-haspopup="dialog" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_apb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-three-bars" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path></svg></button></div><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_apb_" popover="auto">Open menu</span><div class="d-none"></div><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderHome__nkA_U prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_cpb_" href="https://github.com/" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-mark-github" viewBox="0 0 24 24" width="32" height="32" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_R_cpb_">Homepage <span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then d<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">d</span><span aria-hidden="true">D</span></span></kbd></span></span><div class="d-none"></div></div><div data-testid="top-nav-center" class="styles-module__center__R3QRv styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><nav class="styles-module__contextRegion__VbSp2 prc-Breadcrumbs-BreadcrumbsBase-3Gb-B" aria-label="Breadcrumbs" data-overflow="menu" data-variant="normal"><ol class="prc-Breadcrumbs-BreadcrumbsList-BKjpe"><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/20260160" data-discover="true"><span class="">20260160</span></a></li><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/20260160/my-first-game" data-discover="true"><span class="styles-module__contextCrumbLast__tI2e3">my-first-game</span></a></li></ol></nav><div class="Search-module__searchButtonGroup__aetw5 prc-ButtonGroup-ButtonGroup-vFUrY"><div><button type="button" aria-label="Search or jump to…" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__searchButton__aiE0a" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="Search-module__placeholder__p9hbG Search-module__text__veSYi Search-module__value__TFoak">Type <kbd class="Search-module__kbd__WCskr">/</kbd> to search</span></span></span></button></div><div></div></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__smallSearchButton___8Gvn prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_2l9b_"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_R_2l9b_">Search or jump to…<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->forward slash<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">forward slash</span><span aria-hidden="true">/</span></span></kbd></span></span><div class="d-none"></div><div class="d-none"><qbsearch-input class="search-input" data-scope="repo:20260160/my-first-game" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="_M46C2Aiap1ni7P-5Y-95ygmRtrnT1UyJJ7O-6p_j36lQN-U4Y6dTgWzNpv91sOKljq1N5NWyA9dbgXbnzr3PA" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="20260160/my-first-game" data-current-org="" data-current-owner="20260160" data-logged-in="true" data-copilot-chat-enabled="true" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/20260160/my-first-game/blob/main/my-first-game.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-5682498e-e11b-406f-9fb7-88b232fbe355" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span data-target="query-builder.clearButton" hidden="">
            <span class="sr-only" id="query-builder-test-clear">Clear</span>
            <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-action="
                  click:query-builder#clear
                  focus:query-builder#clearButtonFocus
                  blur:query-builder#clearButtonBlur
                " variant="small" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

          </span>
      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-5682498e-e11b-406f-9fb7-88b232fbe355" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted tmp-px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Up4wY7dx4g3iZysvB5BnH0b07ZjQn-cZ-PErbUG1mlvpRVzPiRiqrcc9GCpX9w1xfOIurTPYMJ47M4grLKVH5w">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="F4m3PtnuxH-90so2vKxT5d08SPI8Updhbedz2jw8IiuSLuxt8bEh752FOdMTsIJv4-mkYWiVnCN8xeAFvdjhPw">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="9ngk-Cdqr5izTG4l5juiPIf1DeUL38MVS5VHxFm32KwOLtOJ--A_3l626_XzScnOzIpreRLjy-W4STog-FhqPQ" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="8pUcOaxp9nD4X8bP9cnSkpPXZka79hInxbVLA341eGG9N8s6bLbKnoaVZDD0cTK9i7ucL3iD0mcPkeq4NfVY_g" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf"></div></div><div data-testid="top-nav-right" class="styles-module__right__mlBQg styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-testid="top-bar-actions" class="hide-sm hide-md prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="none"><span><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_2kjpb_" href="https://github.com/copilot" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_2kjpb_" popover="auto">Chat with Copilot</span></div><div><div class="d-none"></div><button type="button" aria-label="Open Copilot…" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ CopilotItems-module__CopilotMenu__DVdfE" data-loading="false" data-size="medium" data-variant="invisible" id="_R_54jpb_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button></div></div></span><div class="styles-module__itemDivider__nunbs"></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk GlobalCreateMenu-module__actionMenuButton__Hj_iB" data-loading="false" data-size="medium" data-variant="invisible" aria-labelledby="global-create-menu-tooltip-_R_1jpb_" id="_R_5jpb_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="global-create-menu-tooltip-_R_1jpb_" popover="auto">Create new...</span><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_m3pb_" href="https://github.com/issues" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_m3pb_" popover="auto">Issues</span><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_q3pb_" href="https://github.com/pulls" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_q3pb_" popover="auto">Pull requests</span><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_u3pb_" href="https://github.com/repos" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-repo" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_u3pb_" popover="auto">Repositories</span><div class="d-none"></div></div><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_lpb_" href="https://github.com/notifications" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-inbox" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_R_lpb_">You have no unread notifications<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then n<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">n</span><span aria-hidden="true">N</span></span></kbd></span></span><div class="d-none"></div><div class="GlobalNavUserMenu-module__container__NaVIt"><button data-component="IconButton" type="button" aria-haspopup="menu" data-login="20260160" class="prc-Button-ButtonBase-9n-Xk GlobalNavUserMenu-module__anchor__Dcej6 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_2npb_"><img data-component="Avatar" class="prc-Avatar-Avatar-0xaUi" alt="User avatar" width="32" height="32" style="--avatarSize-regular:32px" src="./week02_files/268550804" data-testid="github-avatar"></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_2npb_" popover="auto">Open user navigation menu</span></div></div></div><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj LocalNavigation-module__LocalNavigation__b0Xc0" aria-label="Repository" data-variant="inset" data-overflow-measured="true"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game" aria-current="page" data-tab-item="code" data-react-nav="code-view" data-react-nav-anchor="code-view-repo-link" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" data-content="Code">Code</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/issues" data-tab-item="issues" data-react-nav="issues-react" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></span><span data-component="text" data-content="Issues">Issues</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/pulls" data-tab-item="pull-requests" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></span><span data-component="text" data-content="Pull requests">Pull requests</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/actions" data-tab-item="actions" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-play" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg></span><span data-component="text" data-content="Actions">Actions</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/projects" data-tab-item="projects" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-table" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path></svg></span><span data-component="text" data-content="Projects">Projects</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/wiki" data-tab-item="wiki" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-book" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path></svg></span><span data-component="text" data-content="Wiki">Wiki</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/security" data-tab-item="security" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg></span><span data-component="text" data-content="Security">Security</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/pulse" data-tab-item="insights" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-graph" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></span><span data-component="text" data-content="Insights">Insights</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/20260160/my-first-game/settings" data-tab-item="settings" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-gear" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg></span><span data-component="text" data-content="Settings">Settings</span></a></li></ul></nav><div class="d-none"></div></header><div data-hpc="true" data-testid="transactional-message-banner" data-analytics-event="{&quot;category&quot;:&quot;copilot_privacy_update_jan_2026&quot;,&quot;action&quot;:&quot;dismiss&quot;,&quot;label&quot;:&quot;group:;location:global&quot;}" data-analytics-visible="{&quot;category&quot;:&quot;copilot_privacy_update_jan_2026&quot;,&quot;action&quot;:&quot;visible&quot;,&quot;label&quot;:&quot;group:;location:global&quot;}"><section aria-labelledby="_R_2b_" class="TransactionalMessageBanner-module__squareBanner__Pw6Pf prc-Banner-Banner-IPLJ2" data-dismissible="" data-title-hidden="" data-variant="info" data-actions-layout="default" tabindex="-1" data-layout="default"><div class="prc-Banner-BannerIcon-o4ayx"><svg aria-hidden="true" focusable="false" class="octicon octicon-info" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></div><div class="prc-Banner-BannerContainer-T-Siu"><div class="prc-Banner-BannerContent-LraS2"><span class="prc-VisuallyHidden-VisuallyHidden-Q0qSB"><h2 id="_R_2b_" class="prc-Banner-BannerTitle-T4z0L" data-banner-title="">Important update</h2></span><div class="BannerDescription"><span class="text-normal"><span>On April 24 we'll start using GitHub Copilot interaction data for AI model training unless you opt out. </span><a class="prc-Link-Link-9ZwDx" data-inline="true" href="https://gh.io/AAzfaht">Review this update</a><span> and manage your preferences in your </span><a class="prc-Link-Link-9ZwDx" data-inline="true" href="https://github.com/settings/copilot/features">GitHub account settings</a><span>.</span></span></div></div></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk prc-Banner-BannerDismiss-b12FL prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_ub_"><svg aria-hidden="true" focusable="false" class="octicon octicon-x" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_ub_" popover="auto">Dismiss banner</span></section></div><script type="application/json" id="__PRIMER_DATA__R_0___">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>


      <div class="js-global-bar" style="display: none;">
        


<qbsearch-input class="search-input" data-scope="repo:20260160/my-first-game" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="_M46C2Aiap1ni7P-5Y-95ygmRtrnT1UyJJ7O-6p_j36lQN-U4Y6dTgWzNpv91sOKljq1N5NWyA9dbgXbnzr3PA" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="20260160/my-first-game" data-current-org="" data-current-owner="20260160" data-logged-in="true" data-copilot-chat-enabled="true" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/20260160/my-first-game/blob/main/my-first-game.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-5682498e-e11b-406f-9fb7-88b232fbe355" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span data-target="query-builder.clearButton" hidden="">
            <span class="sr-only" id="query-builder-test-clear">Clear</span>
            <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-action="
                  click:query-builder#clear
                  focus:query-builder#clearButtonFocus
                  blur:query-builder#clearButtonBlur
                " variant="small" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

          </span>
      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-5682498e-e11b-406f-9fb7-88b232fbe355" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted tmp-px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Up4wY7dx4g3iZysvB5BnH0b07ZjQn-cZ-PErbUG1mlvpRVzPiRiqrcc9GCpX9w1xfOIurTPYMJ47M4grLKVH5w">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="F4m3PtnuxH-90so2vKxT5d08SPI8Updhbedz2jw8IiuSLuxt8bEh752FOdMTsIJv4-mkYWiVnCN8xeAFvdjhPw">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="9ngk-Cdqr5izTG4l5juiPIf1DeUL38MVS5VHxFm32KwOLtOJ--A_3l626_XzScnOzIpreRLjy-W4STog-FhqPQ" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="8pUcOaxp9nD4X8bP9cnSkpPXZka79hInxbVLA341eGG9N8s6bLbKnoaVZDD0cTK9i7ucL3iD0mcPkeq4NfVY_g" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


      </div>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/20260160/my-first-game/blob/main/my-first-game.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/20260160/my-first-game/blob/main/my-first-game.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/20260160/my-first-game/blob/main/my-first-game.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-cc38eec8-9ac3-43a6-b0dd-90604330d2eb" aria-labelledby="tooltip-f653e109-f25b-4133-8ade-7811dc4b040f" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-f653e109-f25b-4133-8ade-7811dc4b040f" for="icon-button-cc38eec8-9ac3-43a6-b0dd-90604330d2eb" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: min(var(--overlay-width-small), 100vw);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
        
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MjY4NTUwODA0IiwidCI6MTc3NDc3MzMxNX0=--2fe8ed746566712abcc803ef6175453d0c99a80682f648b77824e53bbed0ab32" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/20260160/my-first-game/tree/main?resume=1">Open in codespace</a>




    
      
    








<react-app app-name="code-view" initial-path="/20260160/my-first-game/blob/main/my-first-game.py" style="display: block; min-height: calc(100vh - 64px);" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-data-router-enabled="true" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"codeViewBlobRoute":{"csv":null,"csvError":null,"headerInfo":{"toc":null},"issueTemplate":null,"discussionTemplate":null,"richText":null,"renderedFileInfo":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"screen","kind":"constant","ident_start":97,"ident_end":103,"extent_start":97,"extent_end":146,"fully_qualified_name":"screen","ident_utf16":{"start":{"line_number":8,"utf16_col":0},"end":{"line_number":8,"utf16_col":6}},"extent_utf16":{"start":{"line_number":8,"utf16_col":0},"end":{"line_number":8,"utf16_col":49}}},{"name":"clock","kind":"constant","ident_start":218,"ident_end":223,"extent_start":218,"extent_end":245,"fully_qualified_name":"clock","ident_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":5}},"extent_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":27}}},{"name":"particles","kind":"constant","ident_start":246,"ident_end":255,"extent_start":246,"extent_end":260,"fully_qualified_name":"particles","ident_utf16":{"start":{"line_number":12,"utf16_col":0},"end":{"line_number":12,"utf16_col":9}},"extent_utf16":{"start":{"line_number":12,"utf16_col":0},"end":{"line_number":12,"utf16_col":14}}},{"name":"Particle","kind":"class","ident_start":268,"ident_end":276,"extent_start":262,"extent_end":2146,"fully_qualified_name":"Particle","ident_utf16":{"start":{"line_number":14,"utf16_col":6},"end":{"line_number":14,"utf16_col":14}},"extent_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":77,"utf16_col":28}}},{"name":"__init__","kind":"function","ident_start":286,"ident_end":294,"extent_start":282,"extent_end":789,"fully_qualified_name":"Particle.__init__","ident_utf16":{"start":{"line_number":15,"utf16_col":8},"end":{"line_number":15,"utf16_col":16}},"extent_utf16":{"start":{"line_number":15,"utf16_col":4},"end":{"line_number":30,"utf16_col":55}}},{"name":"update","kind":"function","ident_start":799,"ident_end":805,"extent_start":795,"extent_end":1181,"fully_qualified_name":"Particle.update","ident_utf16":{"start":{"line_number":32,"utf16_col":8},"end":{"line_number":32,"utf16_col":14}},"extent_utf16":{"start":{"line_number":32,"utf16_col":4},"end":{"line_number":49,"utf16_col":24}}},{"name":"get_color","kind":"function","ident_start":1191,"ident_end":1200,"extent_start":1187,"extent_end":1427,"fully_qualified_name":"Particle.get_color","ident_utf16":{"start":{"line_number":51,"utf16_col":8},"end":{"line_number":51,"utf16_col":17}},"extent_utf16":{"start":{"line_number":51,"utf16_col":4},"end":{"line_number":56,"utf16_col":24}}},{"name":"draw","kind":"function","ident_start":1437,"ident_end":1441,"extent_start":1433,"extent_end":2095,"fully_qualified_name":"Particle.draw","ident_utf16":{"start":{"line_number":58,"utf16_col":8},"end":{"line_number":58,"utf16_col":12}},"extent_utf16":{"start":{"line_number":58,"utf16_col":4},"end":{"line_number":74,"utf16_col":73}}},{"name":"alive","kind":"function","ident_start":2105,"ident_end":2110,"extent_start":2101,"extent_end":2146,"fully_qualified_name":"Particle.alive","ident_utf16":{"start":{"line_number":76,"utf16_col":8},"end":{"line_number":76,"utf16_col":13}},"extent_utf16":{"start":{"line_number":76,"utf16_col":4},"end":{"line_number":77,"utf16_col":28}}},{"name":"fade_background","kind":"function","ident_start":2196,"ident_end":2211,"extent_start":2192,"extent_end":2382,"fully_qualified_name":"fade_background","ident_utf16":{"start":{"line_number":80,"utf16_col":4},"end":{"line_number":80,"utf16_col":19}},"extent_utf16":{"start":{"line_number":80,"utf16_col":0},"end":{"line_number":83,"utf16_col":30}}},{"name":"running","kind":"constant","ident_start":2384,"ident_end":2391,"extent_start":2384,"extent_end":2398,"fully_qualified_name":"running","ident_utf16":{"start":{"line_number":85,"utf16_col":0},"end":{"line_number":85,"utf16_col":7}},"extent_utf16":{"start":{"line_number":85,"utf16_col":0},"end":{"line_number":85,"utf16_col":14}}}]}},"codeViewLayoutRoute":{"repo":{"id":1183046968,"defaultBranch":"main","name":"my-first-game","ownerLogin":"20260160","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2026-03-16T17:10:50.000+09:00","ownerAvatar":"https://avatars.githubusercontent.com/u/268550804?v=4","public":true,"private":false,"isOrgOwned":false},"currentUser":{"id":268550804,"login":"20260160","userEmail":"20260160@vision.hoseo.edu"},"uploadToken":"hyp-uCD1TYT5MYwOqNMeEmbWZzkAX9X3AYzCvTZ4MzID6eX6l23yRAy-N5Gl-DOpzyVmqQ8VJc3HvR8bheJ90Q","allShortcutsEnabled":true,"treeExpanded":true,"path":"my-first-game.py","symbolsExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1774179975.0","canEdit":false,"currentOid":"c9a063c5dd389b53a38a5165d01ebaa026c3b48d"},"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-742b41342e9c3630.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-ef646bf92158ca23.js","githubDevUrl":"https://github.dev/"},"codeViewFileTreeLayoutRoute":{"fileTree":{"":{"items":[{"name":"practice","path":"practice","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"my-first-game.py","path":"my-first-game.py","contentType":"file"}],"totalCount":3}},"fileTreeProcessingTime":10.828092,"foldersToFetch":[]},"codeViewBlobLayoutRoute":{"codeLineWrapEnabled":false,"refInfo":{"name":"main","listCacheKey":"v0:1774179975.0","canEdit":true,"refType":"branch","currentOid":"c9a063c5dd389b53a38a5165d01ebaa026c3b48d","canEditOnDefaultBranch":true,"fileExistsOnDefault":true},"path":"my-first-game.py","blob":{"copilotSWEAgentEnabled":false,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/20260160/my-first-game/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"my-first-game.py","displayUrl":"https://github.com/20260160/my-first-game/blob/main/my-first-game.py?raw=true","headerInfo":{"blobSize":"2.99 KB","deleteTooltip":"Delete this file","editTooltip":"Edit this file","ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"onBranch":true,"shortPath":"699a9d7","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2F20260160%2Fmy-first-game%2Fblob%2Fmain%2Fmy-first-game.py","isCSV":false,"isRichtext":false,"lineInfo":{"truncatedLoc":"114","truncatedSloc":"87"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"isIssueTemplate":false,"isDiscussionTemplate":false,"language":"Python","languageID":303,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/20260160/my-first-game/blob/main/my-first-game.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/20260160/my-first-game/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/20260160/my-first-game/raw/refs/heads/main/my-first-game.py","renderImageOrRaw":false,"shortPath":null,"symbolsEnabled":true,"tabSize":4,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null},"copilotInfo":null,"copilotAccessAllowed":true,"copilotSpacesEnabled":true,"modelsAccessAllowed":false,"modelsRepoIntegrationEnabled":false,"isMarketplaceEnabled":true},"codeViewBlobLayoutRoute.StyledBlob":{"rawLines":["import pygame","import random","import math","","pygame.init()","","# 화면 설정","WIDTH, HEIGHT = 900, 600","screen = pygame.display.set_mode((WIDTH, HEIGHT))","pygame.display.set_caption(\"🌈 Ultimate Fancy Particle Playground\")","","clock = pygame.time.Clock()","particles = []","","class Particle:","    def __init__(self, x, y):","        self.x = x","        self.y = y","","        # 속도","        angle = random.uniform(0, math.pi * 2)","        speed = random.uniform(3, 8)","        self.vx = math.cos(angle) * speed","        self.vy = math.sin(angle) * speed","","        # 생명과 크기","        self.life = random.randint(60, 120)","        self.max_life = self.life","        self.size = random.randint(4, 9)","        self.hue = random.random()  # 색상 변화용","        self.wind_offset = random.uniform(0, math.pi*2)","","    def update(self):","        # 중력","        self.vy += 0.06","","        # 마찰","        self.vx *= 0.99","        self.vy *= 0.99","","        # 바람 효과","        self.vx += math.sin(pygame.time.get_ticks() * 0.002 + self.wind_offset) * 0.15","","        # 위치 이동","        self.x += self.vx","        self.y += self.vy","","        # 생명 감소","        self.life -= 1","        self.hue += 0.02","","    def get_color(self):","        # 무지개 그라데이션 느낌","        r = int(127 + 127 * math.sin(self.hue))","        g = int(127 + 127 * math.sin(self.hue + 2))","        b = int(127 + 127 * math.sin(self.hue + 4))","        return (r, g, b)","","    def draw(self, surf):","        if self.life \u003c= 0:","            return","","        alpha = self.life / self.max_life","        size = int(self.size * alpha)","        color = self.get_color()","","        # 글로우 효과 (3개 레이어 겹치기)","        for i in range(3, 0, -1):","            glow_size = size + i*4","            glow_surf = pygame.Surface((glow_size*2, glow_size*2), pygame.SRCALPHA)","            pygame.draw.circle(glow_surf, (*color, int(50*alpha)), (glow_size, glow_size), glow_size)","            surf.blit(glow_surf, (self.x - glow_size, self.y - glow_size))","","        # 중심 원","        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), size)","","    def alive(self):","        return self.life \u003e 0","","# 배경 페이드 (잔상 + 살짝 흐림)","def fade_background(surface):","    fade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)","    fade.fill((0, 0, 0, 15))  # 낮은 알파 → 부드러운 잔상","    surface.blit(fade, (0, 0))","","running = True","","while running:","    for event in pygame.event.get():","        if event.type == pygame.QUIT:","            running = False","","    mouse = pygame.mouse.get_pos()","    buttons = pygame.mouse.get_pressed()","","    # 마우스 클릭하면 파티클 생성","    if buttons[0]:","        for _ in range(12):  # 한 번에 많이 생성","            particles.append(Particle(mouse[0], mouse[1]))","","    fade_background(screen)","","    # 파티클 업데이트 \u0026 그리기","    for p in particles:","        p.update()","        p.draw(screen)","","    # 살아있는 파티클만 유지","    particles = [p for p in particles if p.alive()]","","    pygame.display.flip()","    clock.tick(60)","","pygame.quit()"],"stylingDirectives":null,"colorizedLines":["\u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e","\u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003erandom\u003c/span\u003e","\u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003emath\u003c/span\u003e","","\u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003einit\u003c/span\u003e()","","\u003cspan class=pl-c\u003e# 화면 설정\u003c/span\u003e","\u003cspan class=pl-c1\u003eWIDTH\u003c/span\u003e, \u003cspan class=pl-c1\u003eHEIGHT\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-c1\u003e900\u003c/span\u003e, \u003cspan class=pl-c1\u003e600\u003c/span\u003e","\u003cspan class=pl-s1\u003escreen\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003edisplay\u003c/span\u003e.\u003cspan class=pl-c1\u003eset_mode\u003c/span\u003e((\u003cspan class=pl-c1\u003eWIDTH\u003c/span\u003e, \u003cspan class=pl-c1\u003eHEIGHT\u003c/span\u003e))","\u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003edisplay\u003c/span\u003e.\u003cspan class=pl-c1\u003eset_caption\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;🌈 Ultimate Fancy Particle Playground\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-s1\u003eclock\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003etime\u003c/span\u003e.\u003cspan class=pl-c1\u003eClock\u003c/span\u003e()","\u003cspan class=pl-s1\u003eparticles\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e []","","\u003cspan class=pl-k\u003eclass\u003c/span\u003e \u003cspan class=pl-v\u003eParticle\u003c/span\u003e:","    \u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003e__init__\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e, \u003cspan class=pl-s1\u003ex\u003c/span\u003e, \u003cspan class=pl-s1\u003ey\u003c/span\u003e):","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ex\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003ex\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ey\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003ey\u003c/span\u003e","","        \u003cspan class=pl-c\u003e# 속도\u003c/span\u003e","        \u003cspan class=pl-s1\u003eangle\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003erandom\u003c/span\u003e.\u003cspan class=pl-c1\u003euniform\u003c/span\u003e(\u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003epi\u003c/span\u003e \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-c1\u003e2\u003c/span\u003e)","        \u003cspan class=pl-s1\u003espeed\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003erandom\u003c/span\u003e.\u003cspan class=pl-c1\u003euniform\u003c/span\u003e(\u003cspan class=pl-c1\u003e3\u003c/span\u003e, \u003cspan class=pl-c1\u003e8\u003c/span\u003e)","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evx\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003ecos\u003c/span\u003e(\u003cspan class=pl-s1\u003eangle\u003c/span\u003e) \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-s1\u003espeed\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evy\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003esin\u003c/span\u003e(\u003cspan class=pl-s1\u003eangle\u003c/span\u003e) \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-s1\u003espeed\u003c/span\u003e","","        \u003cspan class=pl-c\u003e# 생명과 크기\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003elife\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003erandom\u003c/span\u003e.\u003cspan class=pl-c1\u003erandint\u003c/span\u003e(\u003cspan class=pl-c1\u003e60\u003c/span\u003e, \u003cspan class=pl-c1\u003e120\u003c/span\u003e)","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003emax_life\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003elife\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003esize\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003erandom\u003c/span\u003e.\u003cspan class=pl-c1\u003erandint\u003c/span\u003e(\u003cspan class=pl-c1\u003e4\u003c/span\u003e, \u003cspan class=pl-c1\u003e9\u003c/span\u003e)","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ehue\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003erandom\u003c/span\u003e.\u003cspan class=pl-c1\u003erandom\u003c/span\u003e()  \u003cspan class=pl-c\u003e# 색상 변화용\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ewind_offset\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003erandom\u003c/span\u003e.\u003cspan class=pl-c1\u003euniform\u003c/span\u003e(\u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003epi\u003c/span\u003e\u003cspan class=pl-c1\u003e*\u003c/span\u003e\u003cspan class=pl-c1\u003e2\u003c/span\u003e)","","    \u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003eupdate\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e):","        \u003cspan class=pl-c\u003e# 중력\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evy\u003c/span\u003e \u003cspan class=pl-c1\u003e+=\u003c/span\u003e \u003cspan class=pl-c1\u003e0.06\u003c/span\u003e","","        \u003cspan class=pl-c\u003e# 마찰\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evx\u003c/span\u003e \u003cspan class=pl-c1\u003e*=\u003c/span\u003e \u003cspan class=pl-c1\u003e0.99\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evy\u003c/span\u003e \u003cspan class=pl-c1\u003e*=\u003c/span\u003e \u003cspan class=pl-c1\u003e0.99\u003c/span\u003e","","        \u003cspan class=pl-c\u003e# 바람 효과\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evx\u003c/span\u003e \u003cspan class=pl-c1\u003e+=\u003c/span\u003e \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003esin\u003c/span\u003e(\u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003etime\u003c/span\u003e.\u003cspan class=pl-c1\u003eget_ticks\u003c/span\u003e() \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-c1\u003e0.002\u003c/span\u003e \u003cspan class=pl-c1\u003e+\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ewind_offset\u003c/span\u003e) \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-c1\u003e0.15\u003c/span\u003e","","        \u003cspan class=pl-c\u003e# 위치 이동\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ex\u003c/span\u003e \u003cspan class=pl-c1\u003e+=\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evx\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ey\u003c/span\u003e \u003cspan class=pl-c1\u003e+=\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003evy\u003c/span\u003e","","        \u003cspan class=pl-c\u003e# 생명 감소\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003elife\u003c/span\u003e \u003cspan class=pl-c1\u003e-=\u003c/span\u003e \u003cspan class=pl-c1\u003e1\u003c/span\u003e","        \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ehue\u003c/span\u003e \u003cspan class=pl-c1\u003e+=\u003c/span\u003e \u003cspan class=pl-c1\u003e0.02\u003c/span\u003e","","    \u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003eget_color\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e):","        \u003cspan class=pl-c\u003e# 무지개 그라데이션 느낌\u003c/span\u003e","        \u003cspan class=pl-s1\u003er\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eint\u003c/span\u003e(\u003cspan class=pl-c1\u003e127\u003c/span\u003e \u003cspan class=pl-c1\u003e+\u003c/span\u003e \u003cspan class=pl-c1\u003e127\u003c/span\u003e \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003esin\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ehue\u003c/span\u003e))","        \u003cspan class=pl-s1\u003eg\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eint\u003c/span\u003e(\u003cspan class=pl-c1\u003e127\u003c/span\u003e \u003cspan class=pl-c1\u003e+\u003c/span\u003e \u003cspan class=pl-c1\u003e127\u003c/span\u003e \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003esin\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ehue\u003c/span\u003e \u003cspan class=pl-c1\u003e+\u003c/span\u003e \u003cspan class=pl-c1\u003e2\u003c/span\u003e))","        \u003cspan class=pl-s1\u003eb\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eint\u003c/span\u003e(\u003cspan class=pl-c1\u003e127\u003c/span\u003e \u003cspan class=pl-c1\u003e+\u003c/span\u003e \u003cspan class=pl-c1\u003e127\u003c/span\u003e \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-s1\u003emath\u003c/span\u003e.\u003cspan class=pl-c1\u003esin\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ehue\u003c/span\u003e \u003cspan class=pl-c1\u003e+\u003c/span\u003e \u003cspan class=pl-c1\u003e4\u003c/span\u003e))","        \u003cspan class=pl-k\u003ereturn\u003c/span\u003e (\u003cspan class=pl-s1\u003er\u003c/span\u003e, \u003cspan class=pl-s1\u003eg\u003c/span\u003e, \u003cspan class=pl-s1\u003eb\u003c/span\u003e)","","    \u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003edraw\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e, \u003cspan class=pl-s1\u003esurf\u003c/span\u003e):","        \u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003elife\u003c/span\u003e \u003cspan class=pl-c1\u003e\u0026lt;=\u003c/span\u003e \u003cspan class=pl-c1\u003e0\u003c/span\u003e:","            \u003cspan class=pl-k\u003ereturn\u003c/span\u003e","","        \u003cspan class=pl-s1\u003ealpha\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003elife\u003c/span\u003e \u003cspan class=pl-c1\u003e/\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003emax_life\u003c/span\u003e","        \u003cspan class=pl-s1\u003esize\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eint\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003esize\u003c/span\u003e \u003cspan class=pl-c1\u003e*\u003c/span\u003e \u003cspan class=pl-s1\u003ealpha\u003c/span\u003e)","        \u003cspan class=pl-s1\u003ecolor\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003eget_color\u003c/span\u003e()","","        \u003cspan class=pl-c\u003e# 글로우 효과 (3개 레이어 겹치기)\u003c/span\u003e","        \u003cspan class=pl-k\u003efor\u003c/span\u003e \u003cspan class=pl-s1\u003ei\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e \u003cspan class=pl-en\u003erange\u003c/span\u003e(\u003cspan class=pl-c1\u003e3\u003c/span\u003e, \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-c1\u003e-\u003c/span\u003e\u003cspan class=pl-c1\u003e1\u003c/span\u003e):","            \u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003esize\u003c/span\u003e \u003cspan class=pl-c1\u003e+\u003c/span\u003e \u003cspan class=pl-s1\u003ei\u003c/span\u003e\u003cspan class=pl-c1\u003e*\u003c/span\u003e\u003cspan class=pl-c1\u003e4\u003c/span\u003e","            \u003cspan class=pl-s1\u003eglow_surf\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003eSurface\u003c/span\u003e((\u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e\u003cspan class=pl-c1\u003e*\u003c/span\u003e\u003cspan class=pl-c1\u003e2\u003c/span\u003e, \u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e\u003cspan class=pl-c1\u003e*\u003c/span\u003e\u003cspan class=pl-c1\u003e2\u003c/span\u003e), \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003eSRCALPHA\u003c/span\u003e)","            \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003edraw\u003c/span\u003e.\u003cspan class=pl-c1\u003ecircle\u003c/span\u003e(\u003cspan class=pl-s1\u003eglow_surf\u003c/span\u003e, (\u003cspan class=pl-c1\u003e*\u003c/span\u003e\u003cspan class=pl-s1\u003ecolor\u003c/span\u003e, \u003cspan class=pl-en\u003eint\u003c/span\u003e(\u003cspan class=pl-c1\u003e50\u003c/span\u003e\u003cspan class=pl-c1\u003e*\u003c/span\u003e\u003cspan class=pl-s1\u003ealpha\u003c/span\u003e)), (\u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e, \u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e), \u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e)","            \u003cspan class=pl-s1\u003esurf\u003c/span\u003e.\u003cspan class=pl-c1\u003eblit\u003c/span\u003e(\u003cspan class=pl-s1\u003eglow_surf\u003c/span\u003e, (\u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ex\u003c/span\u003e \u003cspan class=pl-c1\u003e-\u003c/span\u003e \u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e, \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ey\u003c/span\u003e \u003cspan class=pl-c1\u003e-\u003c/span\u003e \u003cspan class=pl-s1\u003eglow_size\u003c/span\u003e))","","        \u003cspan class=pl-c\u003e# 중심 원\u003c/span\u003e","        \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003edraw\u003c/span\u003e.\u003cspan class=pl-c1\u003ecircle\u003c/span\u003e(\u003cspan class=pl-s1\u003esurf\u003c/span\u003e, \u003cspan class=pl-s1\u003ecolor\u003c/span\u003e, (\u003cspan class=pl-en\u003eint\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ex\u003c/span\u003e), \u003cspan class=pl-en\u003eint\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003ey\u003c/span\u003e)), \u003cspan class=pl-s1\u003esize\u003c/span\u003e)","","    \u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003ealive\u003c/span\u003e(\u003cspan class=pl-s1\u003eself\u003c/span\u003e):","        \u003cspan class=pl-k\u003ereturn\u003c/span\u003e \u003cspan class=pl-s1\u003eself\u003c/span\u003e.\u003cspan class=pl-c1\u003elife\u003c/span\u003e \u003cspan class=pl-c1\u003e\u0026gt;\u003c/span\u003e \u003cspan class=pl-c1\u003e0\u003c/span\u003e","","\u003cspan class=pl-c\u003e# 배경 페이드 (잔상 + 살짝 흐림)\u003c/span\u003e","\u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003efade_background\u003c/span\u003e(\u003cspan class=pl-s1\u003esurface\u003c/span\u003e):","    \u003cspan class=pl-s1\u003efade\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003eSurface\u003c/span\u003e((\u003cspan class=pl-c1\u003eWIDTH\u003c/span\u003e, \u003cspan class=pl-c1\u003eHEIGHT\u003c/span\u003e), \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003eSRCALPHA\u003c/span\u003e)","    \u003cspan class=pl-s1\u003efade\u003c/span\u003e.\u003cspan class=pl-c1\u003efill\u003c/span\u003e((\u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-c1\u003e15\u003c/span\u003e))  \u003cspan class=pl-c\u003e# 낮은 알파 → 부드러운 잔상\u003c/span\u003e","    \u003cspan class=pl-s1\u003esurface\u003c/span\u003e.\u003cspan class=pl-c1\u003eblit\u003c/span\u003e(\u003cspan class=pl-s1\u003efade\u003c/span\u003e, (\u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-c1\u003e0\u003c/span\u003e))","","\u003cspan class=pl-s1\u003erunning\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-c1\u003eTrue\u003c/span\u003e","","\u003cspan class=pl-k\u003ewhile\u003c/span\u003e \u003cspan class=pl-s1\u003erunning\u003c/span\u003e:","    \u003cspan class=pl-k\u003efor\u003c/span\u003e \u003cspan class=pl-s1\u003eevent\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003eevent\u003c/span\u003e.\u003cspan class=pl-c1\u003eget\u003c/span\u003e():","        \u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003eevent\u003c/span\u003e.\u003cspan class=pl-c1\u003etype\u003c/span\u003e \u003cspan class=pl-c1\u003e==\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003eQUIT\u003c/span\u003e:","            \u003cspan class=pl-s1\u003erunning\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-c1\u003eFalse\u003c/span\u003e","","    \u003cspan class=pl-s1\u003emouse\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003emouse\u003c/span\u003e.\u003cspan class=pl-c1\u003eget_pos\u003c/span\u003e()","    \u003cspan class=pl-s1\u003ebuttons\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003emouse\u003c/span\u003e.\u003cspan class=pl-c1\u003eget_pressed\u003c/span\u003e()","","    \u003cspan class=pl-c\u003e# 마우스 클릭하면 파티클 생성\u003c/span\u003e","    \u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003ebuttons\u003c/span\u003e[\u003cspan class=pl-c1\u003e0\u003c/span\u003e]:","        \u003cspan class=pl-k\u003efor\u003c/span\u003e \u003cspan class=pl-s1\u003e_\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e \u003cspan class=pl-en\u003erange\u003c/span\u003e(\u003cspan class=pl-c1\u003e12\u003c/span\u003e):  \u003cspan class=pl-c\u003e# 한 번에 많이 생성\u003c/span\u003e","            \u003cspan class=pl-s1\u003eparticles\u003c/span\u003e.\u003cspan class=pl-c1\u003eappend\u003c/span\u003e(\u003cspan class=pl-en\u003eParticle\u003c/span\u003e(\u003cspan class=pl-s1\u003emouse\u003c/span\u003e[\u003cspan class=pl-c1\u003e0\u003c/span\u003e], \u003cspan class=pl-s1\u003emouse\u003c/span\u003e[\u003cspan class=pl-c1\u003e1\u003c/span\u003e]))","","    \u003cspan class=pl-en\u003efade_background\u003c/span\u003e(\u003cspan class=pl-s1\u003escreen\u003c/span\u003e)","","    \u003cspan class=pl-c\u003e# 파티클 업데이트 \u0026amp; 그리기\u003c/span\u003e","    \u003cspan class=pl-k\u003efor\u003c/span\u003e \u003cspan class=pl-s1\u003ep\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e \u003cspan class=pl-s1\u003eparticles\u003c/span\u003e:","        \u003cspan class=pl-s1\u003ep\u003c/span\u003e.\u003cspan class=pl-c1\u003eupdate\u003c/span\u003e()","        \u003cspan class=pl-s1\u003ep\u003c/span\u003e.\u003cspan class=pl-c1\u003edraw\u003c/span\u003e(\u003cspan class=pl-s1\u003escreen\u003c/span\u003e)","","    \u003cspan class=pl-c\u003e# 살아있는 파티클만 유지\u003c/span\u003e","    \u003cspan class=pl-s1\u003eparticles\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e [\u003cspan class=pl-s1\u003ep\u003c/span\u003e \u003cspan class=pl-k\u003efor\u003c/span\u003e \u003cspan class=pl-s1\u003ep\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e \u003cspan class=pl-s1\u003eparticles\u003c/span\u003e \u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003ep\u003c/span\u003e.\u003cspan class=pl-c1\u003ealive\u003c/span\u003e()]","","    \u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003edisplay\u003c/span\u003e.\u003cspan class=pl-c1\u003eflip\u003c/span\u003e()","    \u003cspan class=pl-s1\u003eclock\u003c/span\u003e.\u003cspan class=pl-c1\u003etick\u003c/span\u003e(\u003cspan class=pl-c1\u003e60\u003c/span\u003e)","","\u003cspan class=pl-s1\u003epygame\u003c/span\u003e.\u003cspan class=pl-c1\u003equit\u003c/span\u003e()"]}},"title":"my-first-game/my-first-game.py at main · 20260160/my-first-game","appPayload":{},"meta":{"title":"my-first-game/my-first-game.py at main · 20260160/my-first-game"}}</script>
  <div data-target="react-app.reactRoot"><meta name="github-code-view-meta-stats" id="github-code-view-meta-stats" data-hydrostats="publish"> <!-- --> <a hidden="" id="code-view-repo-link" href="https://github.com/20260160/my-first-game" data-discover="true"></a> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot--KH-d"><div class="prc-PageLayout-PageLayoutWrapper-2BhU2" data-width="full"><div class="prc-PageLayout-PageLayoutContent-BneH9"><div class="CodeViewFileTreeLayout-module__sidebar__n_Aau" tabindex="0"><div class="prc-PageLayout-PaneWrapper-pHPop ReposFileTreePane-module__Pane__rBZpI ReposFileTreePane-module__HidePaneWithTreeOverlay__mFFGX" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="start" data-sticky="true"><div class="prc-PageLayout-HorizontalDivider-JLVqp prc-PageLayout-PaneHorizontalDivider-9tbnE" data-variant-regular="none" data-variant-narrow="none" data-position="start" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-AyzHK" data-resizable="true" style="--spacing: var(--spacing-none); --pane-min-width: 256px; --pane-max-width: 953px; --pane-width-size: var(--pane-width-large); --pane-width: 320px;"><div><div id="repos-file-tree" class="ReposFileTreePane-module__PaneContents__SJjfF"><div class="ReposFileTreePane-module__Box_1__PpIop"><div class="d-flex width-full tmp-mb-3 flex-items-center"><h2 class="use-tree-pane-module__Heading__s4QbZ prc-Heading-Heading-MtWFE"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="prc-Button-ButtonBase-9n-Xk position-relative ExpandFileTreeButton-module__expandButton__hDOcv fgColor-muted prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_99lmjal1d_" data-hotkey="Control+b"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="se" aria-hidden="true" id="_R_99lmjal1d_" popover="auto">Collapse file tree</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+b"></button></h2><h2 class="CodeViewFileTreeLayout-module__heading__A1Iqk">Files</h2></div><div class="ReposFileTreePane-module__Box_2__g74WI"><div class="ReposFileTreePane-module__Box_3__D6cTp"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="main branch" data-testid="anchor-button" data-icv-name="Switch branches/tags" class="prc-Button-ButtonBase-9n-Xk react-repos-tree-pane-ref-selector width-full ref-selector-class RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn__a3WK3" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector" data-hotkey="w"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer__yaf4p"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader__XtXRG"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer__Di3rk"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText__w_fmP">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="ReposFileTreePane-module__Box_4__DG4pa"><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk ReposFileTreePane-module__IconButton__rGggU prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_r_c_" href="https://github.com/20260160/my-first-game/new/main" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_r_c_" popover="auto">Add file</span><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk SearchButton-module__IconButton__SBlqu ReposFileTreePane-module__SearchButtonWithLeftBorder__TBrDc prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_qhlmjal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" popover="auto"><span id="_R_qhlmjal1d_">Search this repository<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->forward slash<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">forward slash</span><span aria-hidden="true">/</span></span></kbd></span></span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="/"></button></div></div></div><div class="ReposFileTreePane-module__FileResultsList__zmSnM"><span class="d-flex FileResultsList-module__FilesSearchBox__ivVkc TextInput-wrapper prc-components-TextInputWrapper-Hpdqi prc-components-TextInputBaseWrapper-wY-n0" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id="_R_1almjal1d_" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby="_R_1almjal1d_ _R_1almjal1dH1_" data-component="input" class="prc-components-Input-IwWrt" value=""><span class="TextInput-icon" id="_R_1almjal1dH1_" aria-hidden="true"><kbd>t</kbd></span></span></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="t,Shift+T"></button><button hidden="" data-hotkey="t,Shift+T"></button><div class="ReposFileTreePane-module__Box_5__Zy_o6"><div style="height:1px;margin-top:-1px;width:100%;flex-shrink:0"></div><div><div class="react-tree-show-tree-items"><div class="ReposFileTreeView-module__Box__vkb5W" data-testid="repos-file-tree-container"><nav aria-label="File Tree Navigation"><span class="prc-src-InternalVisuallyHidden-2YaI6"><div></div></span><ul role="tree" aria-label="Files" data-truncate-text="true" class="prc-TreeView-TreeViewRootUlStyles-Mzrmj"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practice-item" role="treeitem" aria-labelledby="_r_0_" aria-describedby="_r_1_" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_0_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_1_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>practice</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id=".gitignore-item" role="treeitem" aria-labelledby="_r_4_" aria-describedby="_r_5_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id="_r_4_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_5_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="0" id="my-first-game.py-item" role="treeitem" aria-labelledby="_r_8_" aria-describedby="_r_9_" aria-level="1" aria-current="true" aria-selected="true"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id="_r_8_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_9_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>my-first-game.py</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="prc-PageLayout-VerticalDivider-9QRmK prc-PageLayout-PaneVerticalDivider-le57g" data-variant-narrow="none" data-variant-regular="line" data-variant-wide="line" data-position="start" style="--spacing:var(--spacing-none)"><div class="prc-PageLayout-DraggableHandle-9s6B4" role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="953" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0"></div></div></div></div><div class="prc-PageLayout-ContentWrapper-gR9eG" data-is-hidden-narrow="true"><div class="prc-PageLayout-Content-xWL-A" data-width="full" style="--spacing:var(--spacing-none)"><div class="SharedPageLayout-module__content__IwGAp" data-selector="repos-split-pane-content" tabindex="0"> <!-- --> <div class="container CodeViewHeader-module__Box__JkPOb"><div class="CodeViewHeader-module__StickyHeader__Qn7UN" id="StickyHeader"><div class="CodeViewHeader-module__Box_1__SbNDV"><div class="CodeViewHeader-module__Box_2__TB46f"><div class="CodeViewHeader-module__Box_6__qKUtX"><div class="Breadcrumb-module__container__Vxvev Breadcrumb-module__lg__Rjz0A"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Breadcrumb-module__nav__rQFDj"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Breadcrumb-module__list__ZH6zr"><li class="Breadcrumb-module__listItem__Ib0x_"><a class="Breadcrumb-module__repoLink__O2Nbs prc-Link-Link-9ZwDx" data-testid="breadcrumbs-repo-link" href="https://github.com/20260160/my-first-game/tree/main" data-discover="true">my-first-game</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Breadcrumb-module__filename__equZR"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__lg__Rjz0A" aria-hidden="true">/</span><h1 class="Breadcrumb-module__filenameHeading__MNMtw Breadcrumb-module__lg__Rjz0A prc-Heading-Heading-MtWFE" tabindex="-1" id="file-name-id-wide">my-first-game.py</h1></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk ml-2 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_R_ddajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="CopyToClipboardButton-module__tooltip__BhMvU prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-label="Copy path" aria-hidden="true" id="_R_ddajal1d_" popover="auto" style="top: 137.5px; left: 553.062px;">Copy path</span></div></div><div class="react-code-view-header-element--wide"><div class="CodeViewHeader-module__Box_7___0R6c"><div class="d-flex gap-2"><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" style="display:none" class="prc-Button-ButtonBase-9n-Xk NavigationMenu-module__Button__LpKgm" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click NavigationMenu-module__IconButton__HpX3G prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_7p6dajal1d_" id="_R_96dajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_R_7p6dajal1d_" popover="auto">More file actions</span></div></div></div><div class="react-code-view-header-element--narrow"><div class="CodeViewHeader-module__Box_7___0R6c"><div class="d-flex gap-2"><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" style="display:none" class="prc-Button-ButtonBase-9n-Xk NavigationMenu-module__Button__LpKgm" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click NavigationMenu-module__IconButton__HpX3G prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_7p7dajal1d_" id="_R_97dajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_R_7p7dajal1d_" popover="auto">More file actions</span></div></div></div></div></div></div></div><div class="CodeView-module__contentWrapper__cG2JH"><div class="react-code-view-bottom-padding"><div class="BlobTopBanners-module__Box__v_nvx"></div></div> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="r,Shift+R"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="d-flex flex-column border rounded-2 tmp-mb-3 pl-1"><div class="LatestCommit-module__Box__B25ZT"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="LatestCommit-module__Box_1__YkEgg"><div class="LatestCommit-module__attributionWrapper__QX2mz"><div class="CommitAttribution-module__CommitAttributionContainer__I_rfs"><div data-testid="author-avatar" class="Box-sc-62in7e-0 AuthorAvatar-module__AuthorAvatarContainer__n0MVc"><img data-component="Avatar" class="AuthorAvatar-module__authorAvatarImage__a3R8x prc-Avatar-Avatar-0xaUi" alt="author" width="20" height="20" data-testid="github-avatar" aria-label="author" src="./week02_files/gravatar-user-420.png" style="--avatarSize-regular: 20px;"><div class="AuthorDisplayName-module__truncate__d1MRu prc-Truncate-Truncate-2G1eo" data-inline="true" title="turtle" style="--truncate-max-width: 125px;"><span class="Text__StyledText-sc-1klmep6-0 iqjEaj AuthorDisplayName-module__Text__OP5Q9 prc-Text-Text-9mHv3">turtle</span></div></div><span class=""></span></div></div><div class="d-none d-sm-flex LatestCommit-module__Box_2__pSPKJ"><div class="Truncate flex-items-center f5"><span class="Truncate-text prc-Text-Text-9mHv3" data-testid="latest-commit-html"><a data-hovercard-url="/20260160/my-first-game/commit/d751518fe65b54031617459ec61dd7fa57b8ce4b/hovercard" data-pjax="true" class="Link--secondary" href="https://github.com/20260160/my-first-game/commit/d751518fe65b54031617459ec61dd7fa57b8ce4b" aria-keyshortcuts="Alt+ArrowUp">3rd edit</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time tense="past" datetime="2026-03-22T11:20:42.000Z" title="Mar 22, 2026, 8:20 PM GMT+9"><template shadowrootmode="open">last week</template>Mar 22, 2026</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-9ZwDx" aria-label="Commit d751518" data-hovercard-url="/20260160/my-first-game/commit/d751518fe65b54031617459ec61dd7fa57b8ce4b/hovercard" data-hovercard-type="commit" octo-click="hovercard-link-click" octo-dimensions="link_type:self" aria-keyshortcuts="Alt+ArrowUp" href="https://github.com/20260160/my-first-game/commit/d751518fe65b54031617459ec61dd7fa57b8ce4b" data-discover="true">d751518</a>&nbsp;·&nbsp;<relative-time tense="past" datetime="2026-03-22T11:20:42.000Z" title="Mar 22, 2026, 8:20 PM GMT+9"><template shadowrootmode="open">last week</template>Mar 22, 2026</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a href="https://github.com/20260160/my-first-game/commits/main/my-first-game.py" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="prc-Button-ButtonBase-9n-Xk LatestCommit-module__IconButton__mkJr_ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_h_"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_h_" popover="auto">Open commit details</span></div><div class="d-flex d-lg-none"><a aria-label="View commit history for this file." href="https://github.com/20260160/my-first-game/commits/main/my-first-game.py" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="_R_15lalajal1d_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" role="tooltip" aria-hidden="true" id="_R_15lalajal1d_" popover="auto">History</span></div></div></div></div></div><div class="d-flex flex-row"><div class="container BlobViewContent-module__blobContainer__DtH2d BlobViewContent-module__blobContainerWithPanel__bcTSz"><div class="react-code-size-details-banner BlobViewContent-module__codeSizeDetails__e5sUw"><div class="react-code-size-details-banner CodeSizeDetails-module__Box__VcD6l"><div class="text-mono CodeSizeDetails-module__Box_1__GVxQL"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1__lE93V prc-Truncate-Truncate-2G1eo" data-inline="true" title="2.99 KB" style="--truncate-max-width:100%"><span>114 lines (87 loc) · 2.99 KB</span></div></div></div></div><div class="react-blob-view-header-sticky BlobViewContent-module__stickyHeader__VwxB5" id="repos-sticky-header"><div class="BlobViewHeader-module__Box__yhm9u"><div class="react-blob-sticky-header"><div class="FileNameStickyHeader-module__outerWrapper__ZL4Xc FileNameStickyHeader-module__outerWrapperHidden__Zpynk"><div class="FileNameStickyHeader-module__Box_5__dmNXA"><div class="Breadcrumb-module__container__Vxvev Breadcrumb-module__md__Wb1Gs"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Breadcrumb-module__nav__rQFDj"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Breadcrumb-module__list__ZH6zr"><li class="Breadcrumb-module__listItem__Ib0x_"><a class="Breadcrumb-module__repoLink__O2Nbs prc-Link-Link-9ZwDx" data-testid="breadcrumbs-repo-link" href="https://github.com/20260160/my-first-game/tree/main" data-discover="true">my-first-game</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Breadcrumb-module__filename__equZR"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__md__Wb1Gs" aria-hidden="true">/</span><h1 class="Breadcrumb-module__filenameHeading__MNMtw Breadcrumb-module__md__Wb1Gs prc-Heading-Heading-MtWFE" tabindex="-1" id="sticky-file-name-id">my-first-game.py</h1></div></div><button type="button" class="prc-Button-ButtonBase-9n-Xk FileNameStickyHeader-module__Button__LSEU_ FileNameStickyHeader-module__GoToTopButton__nxAFn" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Top</span></span></button></div></div></div><div class="BlobViewHeader-module__Box_1__VEmuQ"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">File metadata and controls</h2><div class="BlobViewHeader-module__Box_2__icUs2"><ul aria-label="File view" class="prc-SegmentedControl-SegmentedControl-lqIXp BlobTabButtons-module__SegmentedControl__jen2u" data-variant="default" data-size="small"><li class="prc-SegmentedControl-Item-tSCQh" data-selected=""><button aria-current="true" class="prc-SegmentedControl-Button-E48xz" type="button" style="--separator-color:transparent" data-hotkey="Control+/ Control+c"><span class="prc-SegmentedControl-Content-1COlk segmentedControl-content"><div class="prc-SegmentedControl-Text-7S2y2 segmentedControl-text" data-text="Code">Code</div></span></button></li><li class="prc-SegmentedControl-Item-tSCQh"><button aria-current="false" class="prc-SegmentedControl-Button-E48xz" type="button" style="--separator-color:var(--borderColor-default)" data-hotkey="b,Shift+B,Control+/ Control+b"><span class="prc-SegmentedControl-Content-1COlk segmentedControl-content"><div class="prc-SegmentedControl-Text-7S2y2 segmentedControl-text" data-text="Blame">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+c"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><div class="react-code-size-details-in-header CodeSizeDetails-module__Box__VcD6l"><div class="text-mono CodeSizeDetails-module__Box_1__GVxQL"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1__lE93V prc-Truncate-Truncate-2G1eo" data-inline="true" title="2.99 KB" style="--truncate-max-width:100%"><span>114 lines (87 loc) · 2.99 KB</span></div></div></div></div><div class="BlobViewHeader-module__Box_3__ng6v2"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><button data-component="IconButton" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_R_6qfj6alajal1d_" id="_R_qfj6alajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-space" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 13.25V2.75C0 1.784.784 1 1.75 1H5c.551 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1h6.75c.966 0 1.75.784 1.75 1.75v3.638a.75.75 0 0 1-1.5 0V4.75a.25.25 0 0 0-.25-.25H7.5a1.75 1.75 0 0 1-1.4-.7l-.9-1.2a.25.25 0 0 0-.2-.1H1.75a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h5.663l.076.004a.75.75 0 0 1 0 1.492L7.413 15H1.75A1.75 1.75 0 0 1 0 13.25Z"></path><path d="M12.265 9.16a.248.248 0 0 1 .467 0l.237.649a3.726 3.726 0 0 0 2.219 2.218l.649.238a.249.249 0 0 1 0 .467l-.649.237a3.728 3.728 0 0 0-2.219 2.219l-.237.649a.249.249 0 0 1-.467 0l-.238-.649a3.726 3.726 0 0 0-2.218-2.219l-.649-.237a.248.248 0 0 1 0-.467l.649-.238a3.725 3.725 0 0 0 2.218-2.218l.238-.649Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_R_6qfj6alajal1d_" popover="auto">Add to space</span><button data-component="IconButton" type="button" data-testid="copilot-ask-menu" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_R_jj6alajal1d_" id="blob-view-header-copilot-icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_R_jj6alajal1d_" popover="auto">Ask Copilot about this file</span><div class="react-blob-header-edit-and-raw-actions BlobViewHeader-module__Box_4__J4Y4W"><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a href="https://github.com/20260160/my-first-game/raw/refs/heads/main/my-first-game.py" data-testid="raw-button" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov BlobViewHeader-module__LinkButton__X9kx2" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" data-hotkey="Control+/ Control+r"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Raw</span></span></a></div><div><button data-component="IconButton" type="button" data-testid="copy-raw-button" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_R_6arj6alajal1d_" data-hotkey="Control+Shift+C"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_R_6arj6alajal1d_" popover="auto">Copy raw file</span></div><div><button data-component="IconButton" type="button" data-testid="download-raw-button" class="prc-Button-ButtonBase-9n-Xk BlobViewHeader-module__downloadButton__ef459 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_R_3arj6alajal1d_" data-hotkey="Control+Shift+S"><svg aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_R_3arj6alajal1d_" popover="auto">Download raw file</span></div></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+r"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+C"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+S"></button><a class="js-github-dev-shortcut d-none prc-Link-Link-9ZwDx" href="https://github.dev/" data-hotkey="., Control+Shift+/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="., Control+Shift+/"></button><a class="js-github-dev-new-tab-shortcut d-none prc-Link-Link-9ZwDx" href="https://github.dev/" target="_blank" data-hotkey="Shift+.,Shift+&gt;,&gt;"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Shift+.,Shift+&gt;,&gt;"></button><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a data-component="IconButton" type="button" data-testid="edit-button" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_R_1krj6alajal1d_" href="https://github.com/20260160/my-first-game/edit/main/my-first-game.py" data-discover="true" data-hotkey="e,Shift+E"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_R_1krj6alajal1d_" popover="auto">Edit this file</span></div><div><button data-component="IconButton" type="button" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_R_1ukrj6alajal1d_" id="_R_2krj6alajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_R_1ukrj6alajal1d_" popover="auto">More edit options</span></div></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><button data-component="IconButton" type="button" aria-pressed="true" aria-expanded="true" aria-controls="symbols-pane" data-testid="symbols-button" class="prc-Button-ButtonBase-9n-Xk BlobViewHeader-module__IconButton_2__RyjZg prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_R_vj6alajal1d_" id="symbols-button" data-hotkey="Control+i"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_R_vj6alajal1d_" popover="auto">Close symbols panel</span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click BlobViewHeader-module__IconButton__XrMQY prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_R_3t7j6alajal1d_" id="_R_57j6alajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_R_3t7j6alajal1d_" popover="auto">Edit and raw actions</span></div></div></div></div><div></div></div><div class="BlobViewContent-module__blobContentWrapper__JS0W6"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="BlobContent-module__blobContentSection__VOgZq" style="margin-top:46px"><div class="CodeBlob-module__codeBlobWrapper__RS6In" style="padding-top:8px;padding-bottom:8px"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="position-relative"><div class="CodeBlob-module__codeBlobInner__tfjuQ"><div class="CodeBlob-module__cursorContainer__tiLPm"><div style="height: 2280px;"><div aria-hidden="true" data-testid="navigation-cursor" class="code-navigation-cursor" style="top: 0px; left: 92px;"> </div><button hidden="" data-testid="NavigationCursorEnter" data-hotkey="Control+Enter" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightedLine" data-hotkey="Shift+J" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightAndExpandMenu" data-hotkey="Alt+Shift+C,Alt+Shift+Ç" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageDown" data-hotkey="PageDown" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageUp" data-hotkey="PageUp" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div><textarea id="read-only-cursor-text-area" data-testid="read-only-cursor-text-area" aria-label="file content" aria-readonly="true" inputmode="none" tabindex="0" aria-multiline="true" aria-haspopup="false" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" spellcheck="false" autocorrect="off" autocapitalize="off" autocomplete="off" data-ms-editor="false" class="react-blob-textarea react-blob-print-hide" style="resize: none; margin-top: -2px; padding-left: 92px; padding-right: 70px; width: 100%; background-color: unset; box-sizing: border-box; color: transparent; position: absolute; border: none; tab-size: 4; outline: none; overflow: auto hidden; height: 2300px; font-size: 12px; line-height: 20px; overflow-wrap: normal; overscroll-behavior-x: none; white-space: pre; z-index: 1;">import pygame
import random
import math

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Ultimate Fancy Particle Playground")

clock = pygame.time.Clock()
particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # 속도
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(3, 8)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        # 생명과 크기
        self.life = random.randint(60, 120)
        self.max_life = self.life
        self.size = random.randint(4, 9)
        self.hue = random.random()  # 색상 변화용
        self.wind_offset = random.uniform(0, math.pi*2)

    def update(self):
        # 중력
        self.vy += 0.06

        # 마찰
        self.vx *= 0.99
        self.vy *= 0.99

        # 바람 효과
        self.vx += math.sin(pygame.time.get_ticks() * 0.002 + self.wind_offset) * 0.15

        # 위치 이동
        self.x += self.vx
        self.y += self.vy

        # 생명 감소
        self.life -= 1
        self.hue += 0.02

    def get_color(self):
        # 무지개 그라데이션 느낌
        r = int(127 + 127 * math.sin(self.hue))
        g = int(127 + 127 * math.sin(self.hue + 2))
        b = int(127 + 127 * math.sin(self.hue + 4))
        return (r, g, b)

    def draw(self, surf):
        if self.life &lt;= 0:
            return

        alpha = self.life / self.max_life
        size = int(self.size * alpha)
        color = self.get_color()

        # 글로우 효과 (3개 레이어 겹치기)
        for i in range(3, 0, -1):
            glow_size = size + i*4
            glow_surf = pygame.Surface((glow_size*2, glow_size*2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*color, int(50*alpha)), (glow_size, glow_size), glow_size)
            surf.blit(glow_surf, (self.x - glow_size, self.y - glow_size))

        # 중심 원
        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), size)

    def alive(self):
        return self.life &gt; 0

# 배경 페이드 (잔상 + 살짝 흐림)
def fade_background(surface):
    fade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    fade.fill((0, 0, 0, 15))  # 낮은 알파 → 부드러운 잔상
    surface.blit(fade, (0, 0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    # 마우스 클릭하면 파티클 생성
    if buttons[0]:
        for _ in range(12):  # 한 번에 많이 생성
            particles.append(Particle(mouse[0], mouse[1]))

    fade_background(screen)

    # 파티클 업데이트 &amp; 그리기
    for p in particles:
        p.update()
        p.draw(screen)

    # 살아있는 파티클만 유지
    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()</textarea><button hidden="" data-testid="" data-hotkey="Alt+F1,Control+Alt+˙,Control+Alt+h" data-hotkey-scope="read-only-cursor-text-area"></button><div style="pointer-events: none;"><div class="CodeLines-module__scrollContainerHidden__g7TeZ" tabindex="0"><div class="react-code-file-contents CodeLines-module__codeFileContents__TXelD" role="presentation" aria-hidden="true" data-tab-size="4" data-paste-markdown-skip="true" data-hpc="true" style="tab-size: 4; max-width: unset; width: 1146px;"><div class="react-line-numbers-no-virtualization" style="pointer-events: auto; position: relative; z-index: 2;"><div class="react-no-virtualization-wrapper-lines"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div><div data-line-number="2" class="react-line-number react-code-text" style="padding-right: 16px;">2</div><div data-line-number="3" class="react-line-number react-code-text" style="padding-right: 16px;">3</div><div data-line-number="4" class="react-line-number react-code-text" style="padding-right: 16px;">4</div><div data-line-number="5" class="react-line-number react-code-text" style="padding-right: 16px;">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right: 16px;">6</div><div data-line-number="7" class="react-line-number react-code-text" style="padding-right: 16px;">7</div><div data-line-number="8" class="react-line-number react-code-text" style="padding-right: 16px;">8</div><div data-line-number="9" class="react-line-number react-code-text" style="padding-right: 16px;">9</div><div data-line-number="10" class="react-line-number react-code-text" style="padding-right: 16px;">10</div><div data-line-number="11" class="react-line-number react-code-text" style="padding-right: 16px;">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right: 16px;">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right: 16px;">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right: 16px;">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right: 16px;">15<span class="LineNumber-module__codeAlert__WexRo LineNumber-module__codeAlertRight__hdWmf"><div aria-label="Collapse code section" role="button" tabindex="0" class="LineNumber-module__codeFoldingChevron__sY2Yt"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="16" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">16<span class="LineNumber-module__codeAlert__WexRo LineNumber-module__codeAlertRight__hdWmf"><div aria-label="Collapse code section" role="button" tabindex="0" class="LineNumber-module__codeFoldingChevron__sY2Yt"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="17" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">17</div><div data-line-number="18" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">18</div><div data-line-number="19" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">19</div><div data-line-number="20" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">20</div><div data-line-number="21" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">21</div><div data-line-number="22" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">22</div><div data-line-number="23" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">23</div><div data-line-number="24" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">24</div><div data-line-number="25" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">25</div><div data-line-number="26" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">26</div><div data-line-number="27" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">27</div><div data-line-number="28" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">28</div><div data-line-number="29" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">29</div><div data-line-number="30" class="child-of-line-14 child-of-line-15  react-line-number react-code-text" style="padding-right: 16px;">30</div><div data-line-number="31" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">31</div><div data-line-number="32" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">32</div><div data-line-number="33" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">33<span class="LineNumber-module__codeAlert__WexRo LineNumber-module__codeAlertRight__hdWmf"><div aria-label="Collapse code section" role="button" tabindex="0" class="LineNumber-module__codeFoldingChevron__sY2Yt"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="34" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">34</div><div data-line-number="35" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">35</div><div data-line-number="36" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">36</div><div data-line-number="37" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">37</div><div data-line-number="38" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">38</div><div data-line-number="39" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">39</div><div data-line-number="40" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">40</div><div data-line-number="41" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">41</div><div data-line-number="42" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">42</div><div data-line-number="43" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">43</div><div data-line-number="44" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">44</div><div data-line-number="45" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">45</div><div data-line-number="46" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">46</div><div data-line-number="47" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">47</div><div data-line-number="48" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">48</div><div data-line-number="49" class="child-of-line-14 child-of-line-32  react-line-number react-code-text" style="padding-right: 16px;">49</div><div data-line-number="50" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">50</div><div data-line-number="51" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">51</div><div data-line-number="52" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">52<span class="LineNumber-module__codeAlert__WexRo LineNumber-module__codeAlertRight__hdWmf"><div aria-label="Collapse code section" role="button" tabindex="0" class="LineNumber-module__codeFoldingChevron__sY2Yt"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="53" class="child-of-line-14 child-of-line-51  react-line-number react-code-text" style="padding-right: 16px;">53</div><div data-line-number="54" class="child-of-line-14 child-of-line-51  react-line-number react-code-text" style="padding-right: 16px;">54</div><div data-line-number="55" class="child-of-line-14 child-of-line-51  react-line-number react-code-text" style="padding-right: 16px;">55</div><div data-line-number="56" class="child-of-line-14 child-of-line-51  react-line-number react-code-text" style="padding-right: 16px;">56</div><div data-line-number="57" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">57</div><div data-line-number="58" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">58</div><div data-line-number="59" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">59<span class="LineNumber-module__codeAlert__WexRo LineNumber-module__codeAlertRight__hdWmf"><div aria-label="Collapse code section" role="button" tabindex="0" class="LineNumber-module__codeFoldingChevron__sY2Yt"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="60" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">60</div></div><div class="react-no-virtualization-wrapper-lines"><div data-line-number="61" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">61</div><div data-line-number="62" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">62</div><div data-line-number="63" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">63</div><div data-line-number="64" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">64</div><div data-line-number="65" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">65</div><div data-line-number="66" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">66</div><div data-line-number="67" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">67</div><div data-line-number="68" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">68</div><div data-line-number="69" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">69</div><div data-line-number="70" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">70</div><div data-line-number="71" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">71</div><div data-line-number="72" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">72</div><div data-line-number="73" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">73</div><div data-line-number="74" class="child-of-line-14 child-of-line-58  react-line-number react-code-text" style="padding-right: 16px;">74</div><div data-line-number="75" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">75</div><div data-line-number="76" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">76</div><div data-line-number="77" class="child-of-line-14  react-line-number react-code-text" style="padding-right: 16px;">77</div><div data-line-number="78" class="react-line-number react-code-text" style="padding-right: 16px;">78</div><div data-line-number="79" class="react-line-number react-code-text" style="padding-right: 16px;">79</div><div data-line-number="80" class="react-line-number react-code-text" style="padding-right: 16px;">80</div><div data-line-number="81" class="react-line-number react-code-text" style="padding-right: 16px;">81</div><div data-line-number="82" class="react-line-number react-code-text" style="padding-right: 16px;">82</div><div data-line-number="83" class="react-line-number react-code-text" style="padding-right: 16px;">83</div><div data-line-number="84" class="react-line-number react-code-text" style="padding-right: 16px;">84</div><div data-line-number="85" class="react-line-number react-code-text" style="padding-right: 16px;">85</div><div data-line-number="86" class="react-line-number react-code-text" style="padding-right: 16px;">86</div><div data-line-number="87" class="react-line-number react-code-text" style="padding-right: 16px;">87</div><div data-line-number="88" class="react-line-number react-code-text" style="padding-right: 16px;">88</div><div data-line-number="89" class="react-line-number react-code-text" style="padding-right: 16px;">89</div><div data-line-number="90" class="react-line-number react-code-text" style="padding-right: 16px;">90</div><div data-line-number="91" class="react-line-number react-code-text" style="padding-right: 16px;">91</div><div data-line-number="92" class="react-line-number react-code-text" style="padding-right: 16px;">92</div><div data-line-number="93" class="react-line-number react-code-text" style="padding-right: 16px;">93</div><div data-line-number="94" class="react-line-number react-code-text" style="padding-right: 16px;">94</div><div data-line-number="95" class="react-line-number react-code-text" style="padding-right: 16px;">95</div><div data-line-number="96" class="react-line-number react-code-text" style="padding-right: 16px;">96</div><div data-line-number="97" class="react-line-number react-code-text" style="padding-right: 16px;">97</div><div data-line-number="98" class="react-line-number react-code-text" style="padding-right: 16px;">98</div><div data-line-number="99" class="react-line-number react-code-text" style="padding-right: 16px;">99</div><div data-line-number="100" class="react-line-number react-code-text" style="padding-right: 16px;">100</div><div data-line-number="101" class="react-line-number react-code-text" style="padding-right: 16px;">101</div><div data-line-number="102" class="react-line-number react-code-text" style="padding-right: 16px;">102</div><div data-line-number="103" class="react-line-number react-code-text" style="padding-right: 16px;">103</div><div data-line-number="104" class="react-line-number react-code-text" style="padding-right: 16px;">104</div><div data-line-number="105" class="react-line-number react-code-text" style="padding-right: 16px;">105</div><div data-line-number="106" class="react-line-number react-code-text" style="padding-right: 16px;">106</div><div data-line-number="107" class="react-line-number react-code-text" style="padding-right: 16px;">107</div><div data-line-number="108" class="react-line-number react-code-text" style="padding-right: 16px;">108</div><div data-line-number="109" class="react-line-number react-code-text" style="padding-right: 16px;">109</div><div data-line-number="110" class="react-line-number react-code-text" style="padding-right: 16px;">110</div><div data-line-number="111" class="react-line-number react-code-text" style="padding-right: 16px;">111</div><div data-line-number="112" class="react-line-number react-code-text" style="padding-right: 16px;">112</div><div data-line-number="113" class="react-line-number react-code-text" style="padding-right: 16px;">113</div><div data-line-number="114" class="react-line-number react-code-text" style="padding-right: 16px;">114</div></div></div><div class="react-code-lines"><div inert=""><div class="react-no-virtualization-wrapper"><div id="LC1" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">import</span> <span class="pl-s1">pygame</span></div>
<div id="LC2" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">import</span> <span class="pl-s1">random</span></div>
<div id="LC3" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">import</span> <span class="pl-s1">math</span></div>
<div id="LC4" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC5" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">pygame</span>.<span class="pl-c1">init</span>()</div>
<div id="LC6" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC7" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># 화면 설정</span></div>
<div id="LC8" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c1">WIDTH</span>, <span class="pl-c1">HEIGHT</span> <span class="pl-c1">=</span> <span class="pl-c1">900</span>, <span class="pl-c1">600</span></div>
<div id="LC9" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">screen</span> <span class="pl-c1">=</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">display</span>.<span class="pl-c1">set_mode</span>((<span class="pl-c1">WIDTH</span>, <span class="pl-c1">HEIGHT</span>))</div>
<div id="LC10" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">pygame</span>.<span class="pl-c1">display</span>.<span class="pl-c1">set_caption</span>(<span class="pl-s">"🌈 Ultimate Fancy Particle Playground"</span>)</div>
<div id="LC11" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC12" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">clock</span> <span class="pl-c1">=</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">time</span>.<span class="pl-c1">Clock</span>()</div>
<div id="LC13" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">particles</span> <span class="pl-c1">=</span> []</div>
<div id="LC14" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC15" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">class</span> <span class="pl-v">Particle</span>:</div>
<div id="LC16" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">self</span>, <span class="pl-s1">x</span>, <span class="pl-s1">y</span>):</div>
<div id="LC17" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">x</span> <span class="pl-c1">=</span> <span class="pl-s1">x</span></div>
<div id="LC18" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">y</span> <span class="pl-c1">=</span> <span class="pl-s1">y</span></div>
<div id="LC19" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">
</div>
<div id="LC20" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-c"># 속도</span></div>
<div id="LC21" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">angle</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-c1">uniform</span>(<span class="pl-c1">0</span>, <span class="pl-s1">math</span>.<span class="pl-c1">pi</span> <span class="pl-c1">*</span> <span class="pl-c1">2</span>)</div>
<div id="LC22" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">speed</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-c1">uniform</span>(<span class="pl-c1">3</span>, <span class="pl-c1">8</span>)</div>
<div id="LC23" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">vx</span> <span class="pl-c1">=</span> <span class="pl-s1">math</span>.<span class="pl-c1">cos</span>(<span class="pl-s1">angle</span>) <span class="pl-c1">*</span> <span class="pl-s1">speed</span></div>
<div id="LC24" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">vy</span> <span class="pl-c1">=</span> <span class="pl-s1">math</span>.<span class="pl-c1">sin</span>(<span class="pl-s1">angle</span>) <span class="pl-c1">*</span> <span class="pl-s1">speed</span></div>
<div id="LC25" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">
</div>
<div id="LC26" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-c"># 생명과 크기</span></div>
<div id="LC27" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">life</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">60</span>, <span class="pl-c1">120</span>)</div>
<div id="LC28" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">max_life</span> <span class="pl-c1">=</span> <span class="pl-s1">self</span>.<span class="pl-c1">life</span></div>
<div id="LC29" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">size</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">4</span>, <span class="pl-c1">9</span>)</div>
<div id="LC30" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-15 ">        <span class="pl-s1">self</span>.<span class="pl-c1">hue</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-c1">random</span>()  <span class="pl-c"># 색상 변화용</span></div>
<div id="LC31" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">        <span class="pl-s1">self</span>.<span class="pl-c1">wind_offset</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-c1">uniform</span>(<span class="pl-c1">0</span>, <span class="pl-s1">math</span>.<span class="pl-c1">pi</span><span class="pl-c1">*</span><span class="pl-c1">2</span>)</div>
<div id="LC32" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">
</div>
<div id="LC33" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">    <span class="pl-k">def</span> <span class="pl-en">update</span>(<span class="pl-s1">self</span>):</div>
<div id="LC34" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-c"># 중력</span></div>
<div id="LC35" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-s1">self</span>.<span class="pl-c1">vy</span> <span class="pl-c1">+=</span> <span class="pl-c1">0.06</span></div>
<div id="LC36" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">
</div>
<div id="LC37" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-c"># 마찰</span></div>
<div id="LC38" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-s1">self</span>.<span class="pl-c1">vx</span> <span class="pl-c1">*=</span> <span class="pl-c1">0.99</span></div>
<div id="LC39" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-s1">self</span>.<span class="pl-c1">vy</span> <span class="pl-c1">*=</span> <span class="pl-c1">0.99</span></div>
<div id="LC40" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">
</div>
<div id="LC41" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-c"># 바람 효과</span></div>
<div id="LC42" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-s1">self</span>.<span class="pl-c1">vx</span> <span class="pl-c1">+=</span> <span class="pl-s1">math</span>.<span class="pl-c1">sin</span>(<span class="pl-s1">pygame</span>.<span class="pl-c1">time</span>.<span class="pl-c1">get_ticks</span>() <span class="pl-c1">*</span> <span class="pl-c1">0.002</span> <span class="pl-c1">+</span> <span class="pl-s1">self</span>.<span class="pl-c1">wind_offset</span>) <span class="pl-c1">*</span> <span class="pl-c1">0.15</span></div>
<div id="LC43" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">
</div>
<div id="LC44" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-c"># 위치 이동</span></div>
<div id="LC45" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-s1">self</span>.<span class="pl-c1">x</span> <span class="pl-c1">+=</span> <span class="pl-s1">self</span>.<span class="pl-c1">vx</span></div>
<div id="LC46" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-s1">self</span>.<span class="pl-c1">y</span> <span class="pl-c1">+=</span> <span class="pl-s1">self</span>.<span class="pl-c1">vy</span></div>
<div id="LC47" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">
</div>
<div id="LC48" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-c"># 생명 감소</span></div>
<div id="LC49" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-32 ">        <span class="pl-s1">self</span>.<span class="pl-c1">life</span> <span class="pl-c1">-=</span> <span class="pl-c1">1</span></div>
<div id="LC50" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">        <span class="pl-s1">self</span>.<span class="pl-c1">hue</span> <span class="pl-c1">+=</span> <span class="pl-c1">0.02</span></div>
<div id="LC51" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">
</div>
<div id="LC52" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">    <span class="pl-k">def</span> <span class="pl-en">get_color</span>(<span class="pl-s1">self</span>):</div>
<div id="LC53" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-51 ">        <span class="pl-c"># 무지개 그라데이션 느낌</span></div>
<div id="LC54" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-51 ">        <span class="pl-s1">r</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-c1">127</span> <span class="pl-c1">+</span> <span class="pl-c1">127</span> <span class="pl-c1">*</span> <span class="pl-s1">math</span>.<span class="pl-c1">sin</span>(<span class="pl-s1">self</span>.<span class="pl-c1">hue</span>))</div>
<div id="LC55" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-51 ">        <span class="pl-s1">g</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-c1">127</span> <span class="pl-c1">+</span> <span class="pl-c1">127</span> <span class="pl-c1">*</span> <span class="pl-s1">math</span>.<span class="pl-c1">sin</span>(<span class="pl-s1">self</span>.<span class="pl-c1">hue</span> <span class="pl-c1">+</span> <span class="pl-c1">2</span>))</div>
<div id="LC56" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-51 ">        <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-c1">127</span> <span class="pl-c1">+</span> <span class="pl-c1">127</span> <span class="pl-c1">*</span> <span class="pl-s1">math</span>.<span class="pl-c1">sin</span>(<span class="pl-s1">self</span>.<span class="pl-c1">hue</span> <span class="pl-c1">+</span> <span class="pl-c1">4</span>))</div>
<div id="LC57" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">        <span class="pl-k">return</span> (<span class="pl-s1">r</span>, <span class="pl-s1">g</span>, <span class="pl-s1">b</span>)</div>
<div id="LC58" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">
</div>
<div id="LC59" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">    <span class="pl-k">def</span> <span class="pl-en">draw</span>(<span class="pl-s1">self</span>, <span class="pl-s1">surf</span>):</div>
<div id="LC60" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">        <span class="pl-k">if</span> <span class="pl-s1">self</span>.<span class="pl-c1">life</span> <span class="pl-c1">&lt;=</span> <span class="pl-c1">0</span>:</div></div>
<div class="react-no-virtualization-wrapper"><div id="LC61" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">            <span class="pl-k">return</span></div>
<div id="LC62" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">
</div>
<div id="LC63" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">        <span class="pl-s1">alpha</span> <span class="pl-c1">=</span> <span class="pl-s1">self</span>.<span class="pl-c1">life</span> <span class="pl-c1">/</span> <span class="pl-s1">self</span>.<span class="pl-c1">max_life</span></div>
<div id="LC64" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">        <span class="pl-s1">size</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">self</span>.<span class="pl-c1">size</span> <span class="pl-c1">*</span> <span class="pl-s1">alpha</span>)</div>
<div id="LC65" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">        <span class="pl-s1">color</span> <span class="pl-c1">=</span> <span class="pl-s1">self</span>.<span class="pl-c1">get_color</span>()</div>
<div id="LC66" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">
</div>
<div id="LC67" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">        <span class="pl-c"># 글로우 효과 (3개 레이어 겹치기)</span></div>
<div id="LC68" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">3</span>, <span class="pl-c1">0</span>, <span class="pl-c1">-</span><span class="pl-c1">1</span>):</div>
<div id="LC69" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">            <span class="pl-s1">glow_size</span> <span class="pl-c1">=</span> <span class="pl-s1">size</span> <span class="pl-c1">+</span> <span class="pl-s1">i</span><span class="pl-c1">*</span><span class="pl-c1">4</span></div>
<div id="LC70" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">            <span class="pl-s1">glow_surf</span> <span class="pl-c1">=</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">Surface</span>((<span class="pl-s1">glow_size</span><span class="pl-c1">*</span><span class="pl-c1">2</span>, <span class="pl-s1">glow_size</span><span class="pl-c1">*</span><span class="pl-c1">2</span>), <span class="pl-s1">pygame</span>.<span class="pl-c1">SRCALPHA</span>)</div>
<div id="LC71" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">            <span class="pl-s1">pygame</span>.<span class="pl-c1">draw</span>.<span class="pl-c1">circle</span>(<span class="pl-s1">glow_surf</span>, (<span class="pl-c1">*</span><span class="pl-s1">color</span>, <span class="pl-en">int</span>(<span class="pl-c1">50</span><span class="pl-c1">*</span><span class="pl-s1">alpha</span>)), (<span class="pl-s1">glow_size</span>, <span class="pl-s1">glow_size</span>), <span class="pl-s1">glow_size</span>)</div>
<div id="LC72" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">            <span class="pl-s1">surf</span>.<span class="pl-c1">blit</span>(<span class="pl-s1">glow_surf</span>, (<span class="pl-s1">self</span>.<span class="pl-c1">x</span> <span class="pl-c1">-</span> <span class="pl-s1">glow_size</span>, <span class="pl-s1">self</span>.<span class="pl-c1">y</span> <span class="pl-c1">-</span> <span class="pl-s1">glow_size</span>))</div>
<div id="LC73" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">
</div>
<div id="LC74" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 child-of-line-58 ">        <span class="pl-c"># 중심 원</span></div>
<div id="LC75" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">        <span class="pl-s1">pygame</span>.<span class="pl-c1">draw</span>.<span class="pl-c1">circle</span>(<span class="pl-s1">surf</span>, <span class="pl-s1">color</span>, (<span class="pl-en">int</span>(<span class="pl-s1">self</span>.<span class="pl-c1">x</span>), <span class="pl-en">int</span>(<span class="pl-s1">self</span>.<span class="pl-c1">y</span>)), <span class="pl-s1">size</span>)</div>
<div id="LC76" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">
</div>
<div id="LC77" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-14 ">    <span class="pl-k">def</span> <span class="pl-en">alive</span>(<span class="pl-s1">self</span>):</div>
<div id="LC78" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-c1">life</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span></div>
<div id="LC79" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC80" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># 배경 페이드 (잔상 + 살짝 흐림)</span></div>
<div id="LC81" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">def</span> <span class="pl-en">fade_background</span>(<span class="pl-s1">surface</span>):</div>
<div id="LC82" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">fade</span> <span class="pl-c1">=</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">Surface</span>((<span class="pl-c1">WIDTH</span>, <span class="pl-c1">HEIGHT</span>), <span class="pl-s1">pygame</span>.<span class="pl-c1">SRCALPHA</span>)</div>
<div id="LC83" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">fade</span>.<span class="pl-c1">fill</span>((<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">15</span>))  <span class="pl-c"># 낮은 알파 → 부드러운 잔상</span></div>
<div id="LC84" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">surface</span>.<span class="pl-c1">blit</span>(<span class="pl-s1">fade</span>, (<span class="pl-c1">0</span>, <span class="pl-c1">0</span>))</div>
<div id="LC85" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC86" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">running</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span></div>
<div id="LC87" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC88" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">while</span> <span class="pl-s1">running</span>:</div>
<div id="LC89" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">for</span> <span class="pl-s1">event</span> <span class="pl-c1">in</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">event</span>.<span class="pl-c1">get</span>():</div>
<div id="LC90" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">if</span> <span class="pl-s1">event</span>.<span class="pl-c1">type</span> <span class="pl-c1">==</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">QUIT</span>:</div>
<div id="LC91" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-s1">running</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span></div>
<div id="LC92" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC93" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">mouse</span> <span class="pl-c1">=</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">mouse</span>.<span class="pl-c1">get_pos</span>()</div>
<div id="LC94" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">buttons</span> <span class="pl-c1">=</span> <span class="pl-s1">pygame</span>.<span class="pl-c1">mouse</span>.<span class="pl-c1">get_pressed</span>()</div>
<div id="LC95" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC96" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"># 마우스 클릭하면 파티클 생성</span></div>
<div id="LC97" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">if</span> <span class="pl-s1">buttons</span>[<span class="pl-c1">0</span>]:</div>
<div id="LC98" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">for</span> <span class="pl-s1">_</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">12</span>):  <span class="pl-c"># 한 번에 많이 생성</span></div>
<div id="LC99" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-s1">particles</span>.<span class="pl-c1">append</span>(<span class="pl-en">Particle</span>(<span class="pl-s1">mouse</span>[<span class="pl-c1">0</span>], <span class="pl-s1">mouse</span>[<span class="pl-c1">1</span>]))</div>
<div id="LC100" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC101" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-en">fade_background</span>(<span class="pl-s1">screen</span>)</div>
<div id="LC102" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC103" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"># 파티클 업데이트 &amp; 그리기</span></div>
<div id="LC104" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">for</span> <span class="pl-s1">p</span> <span class="pl-c1">in</span> <span class="pl-s1">particles</span>:</div>
<div id="LC105" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-s1">p</span>.<span class="pl-c1">update</span>()</div>
<div id="LC106" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-s1">p</span>.<span class="pl-c1">draw</span>(<span class="pl-s1">screen</span>)</div>
<div id="LC107" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC108" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"># 살아있는 파티클만 유지</span></div>
<div id="LC109" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">particles</span> <span class="pl-c1">=</span> [<span class="pl-s1">p</span> <span class="pl-k">for</span> <span class="pl-s1">p</span> <span class="pl-c1">in</span> <span class="pl-s1">particles</span> <span class="pl-k">if</span> <span class="pl-s1">p</span>.<span class="pl-c1">alive</span>()]</div>
<div id="LC110" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC111" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">pygame</span>.<span class="pl-c1">display</span>.<span class="pl-c1">flip</span>()</div>
<div id="LC112" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">clock</span>.<span class="pl-c1">tick</span>(<span class="pl-c1">60</span>)</div>
<div id="LC113" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC114" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">pygame</span>.<span class="pl-c1">quit</span>()</div></div></div><div class="symbol-highlight react-code-text StickyLineObserverOverlay-module__stickyLineObserver__rhc2u" data-testid="sticky-line-observer" style="top: 260px; height: 20px;"></div><div class="symbol-highlight react-code-text StickyLineObserverOverlay-module__stickyLineObserver__rhc2u" data-testid="sticky-line-observer" style="top: 280px; height: 20px;"></div><div class="symbol-highlight react-code-text StickyLineObserverOverlay-module__stickyLineObserver__rhc2u" data-testid="sticky-line-observer" style="top: 620px; height: 20px;"></div><div class="symbol-highlight react-code-text StickyLineObserverOverlay-module__stickyLineObserver__rhc2u" data-testid="sticky-line-observer" style="top: 1000px; height: 20px;"></div><div class="symbol-highlight react-code-text StickyLineObserverOverlay-module__stickyLineObserver__rhc2u" data-testid="sticky-line-observer" style="top: 1140px; height: 20px;"></div></div><button hidden="" data-hotkey="Control+a"></button></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div></section></div></div><div class="BlobViewContent-module__symbolsPanelSpacer__Vuo_9"></div><div class="Panel-module__Box__AdYCI panel-content-narrow-styles inner-panel-content-not-narrow" style="top:0px;z-index:4;background:var(--bgColor-default, var(--color-canvas-default));position:sticky;border-radius:0px 0px 6px 6px;border-top:0"><div id="symbols-pane"><div class="CodeNavSymbolNavigation-module__container__kfSZY" aria-labelledby="symbols-pane-header"><div class="CodeNavSymbolNavigation-module__headerRow__HVKGZ"><h2 class="CodeNavSymbolNavigation-module__headerTitle__e4wuX" id="symbols-pane-header" tabindex="-1">Symbols</h2><button data-component="IconButton" type="button" data-hotkey="Escape" class="prc-Button-ButtonBase-9n-Xk CodeNavSymbolNavigation-module__closeButton__XOIhD prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_4baalajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-x" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="w" aria-hidden="true" id="_R_4baalajal1d_" popover="auto">Close symbols</span></div><p class="CodeNavSymbolNavigation-module__description__n1e85">Find definitions and references for functions and other symbols in this file by clicking a symbol below or in the code.</p><span class="CodeNavSymbolNavigation-module__filterInput__DQChX TextInput-wrapper prc-components-TextInputWrapper-Hpdqi prc-components-TextInputBaseWrapper-wY-n0" data-block="true" data-trailing-action="true" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id="_R_raalajal1d_" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-filter" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M.75 3h14.5a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1 0-1.5ZM3 7.75A.75.75 0 0 1 3.75 7h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 3 7.75Zm3 4a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg></span><input type="text" placeholder="Filter symbols" aria-label="Filter symbols" aria-controls="filter-results" aria-expanded="true" aria-autocomplete="list" role="combobox" aria-describedby="_R_raalajal1d_ _R_raalajal1dH1_" data-component="input" class="prc-components-Input-IwWrt" name="Filter symbols" value=""><span class="TextInput-icon" id="_R_raalajal1dH1_" aria-hidden="true"><span class="CodeNavSymbolNavigation-module__shortcutsBox__oT2Mn"><kbd>r</kbd></span></span></span><div class="CodeNavSymbolNavigation-module__treeWrapper__b4i2M"><div id="filter-results" class="CodeNavSymbolTree-module__filterResults__tenjX"><span class="prc-src-InternalVisuallyHidden-2YaI6"><div></div></span><ul role="tree" aria-label="Code Navigation" data-omit-spacer="false" data-truncate-text="true" class="prc-TreeView-TreeViewRootUlStyles-Mzrmj"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="0" id="0screen" role="treeitem" aria-labelledby="_R_d3aalajal1d_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id="_R_d3aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.variable"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.variable">const</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="screen" style="--truncate-max-width:125px"><span>screen</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="1clock" role="treeitem" aria-labelledby="_R_l3aalajal1d_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id="_R_l3aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.variable"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.variable">const</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="clock" style="--truncate-max-width:125px"><span>clock</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="2particles" role="treeitem" aria-labelledby="_R_t3aalajal1d_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id="_R_t3aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.variable"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.variable">const</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="particles" style="--truncate-max-width:125px"><span>particles</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="3Particle" role="treeitem" aria-labelledby="_R_153aalajal1d_" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_R_153aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.constant"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.constant">class</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="Particle" style="--truncate-max-width:125px"><span>Particle</span></div></div></span></div></div><ul role="group" style="list-style:none;padding:0;margin:0" aria-label="class  Particle"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="0__init__" role="treeitem" aria-labelledby="_R_2r53aalajal1d_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_R_2r53aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.entity"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.entity">func</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="__init__" style="--truncate-max-width:125px"><span>__init__</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="1update" role="treeitem" aria-labelledby="_R_4r53aalajal1d_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_R_4r53aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.entity"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.entity">func</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="update" style="--truncate-max-width:125px"><span>update</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="2get_color" role="treeitem" aria-labelledby="_R_6r53aalajal1d_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_R_6r53aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.entity"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.entity">func</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="get_color" style="--truncate-max-width:125px"><span>get_color</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="3draw" role="treeitem" aria-labelledby="_R_8r53aalajal1d_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_R_8r53aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.entity"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.entity">func</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="draw" style="--truncate-max-width:125px"><span>draw</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="4alive" role="treeitem" aria-labelledby="_R_ar53aalajal1d_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_R_ar53aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.entity"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.entity">func</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="alive" style="--truncate-max-width:125px"><span>alive</span></div></div></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="4fade_background" role="treeitem" aria-labelledby="_R_1d3aalajal1d_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id="_R_1d3aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.entity"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.entity">func</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="fade_background" style="--truncate-max-width:125px"><span>fade_background</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="5running" role="treeitem" aria-labelledby="_R_1l3aalajal1d_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id="_R_1l3aalajal1d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><div class="CodeNavSymbolTree-module__treeContent__opWeK"><div class="SymbolIndicator-module__symbolWrapper__mSRj8 SymbolIndicator-module__symbolWrapperCompact__UNWj3"><div class="SymbolIndicator-module__symbolBackground__tphNO" style="background-color:prettylights.syntax.variable"></div><div class="SymbolIndicator-module__symbolLabel__qg6oQ SymbolIndicator-module__symbolLabelSmall__rzeMO" style="color:prettylights.syntax.variable">const</div></div>  <div class="CodeNavSymbolTree-module__truncate__GO8ge prc-Truncate-Truncate-2G1eo" title="running" style="--truncate-max-width:125px"><span>running</span></div></div></span></div></div></li></ul></div></div></div></div></div></div> </div> <!-- --> </div></div></div></div></div></div><div class="ScrollMarksContainer-module__scrollMarksContainer__Eu7uU" id="find-result-marks-container"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+F6,Control+Shift+F6"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__R_1___">{"resolvedServerColorMode":"night"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer tmp-pt-7 tmp-pb-6 f6 color-fg-muted color-border-subtle p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path>
</svg>
</a>
      <span>
        © 2026 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">


          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-locale="en" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/20260160"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/20260160"]:before,
      .user-mention[href$="/20260160"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true"></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive"></div></body></html>