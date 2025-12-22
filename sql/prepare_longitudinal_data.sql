-- Prepare longitudinal dataset for mixed-effects models
-- Each row = one subject at one time point

SELECT
    p.patient_id,
    v.visit_date,
    v.time_point,              -- e.g. baseline = 0, follow-up = 1,2,...
    p.sex,
    p.age_at_baseline,
    v.outcome_value,           -- dependent variable
    v.exposure_status,         -- main exposure
    v.covariate_1,
    v.covariate_2
FROM patients p
JOIN visits v
    ON p.patient_id = v.patient_id
WHERE v.outcome_value IS NOT NULL
ORDER BY p.patient_id, v.time_point;
