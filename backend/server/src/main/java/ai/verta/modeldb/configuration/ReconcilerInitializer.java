package ai.verta.modeldb.configuration;

import ai.verta.modeldb.ServiceSet;
import ai.verta.modeldb.common.configuration.RunLiquibaseSeparately.RunLiquibaseWithMainService;
import ai.verta.modeldb.common.futures.FutureExecutor;
import ai.verta.modeldb.common.futures.FutureJdbi;
import ai.verta.modeldb.common.reconcilers.ReconcilerConfig;
import ai.verta.modeldb.config.MDBConfig;
import ai.verta.modeldb.config.TestConfig;
import ai.verta.modeldb.reconcilers.SoftDeleteExperimentRuns;
import ai.verta.modeldb.reconcilers.SoftDeleteExperiments;
import ai.verta.modeldb.reconcilers.SoftDeleteProjects;
import ai.verta.modeldb.reconcilers.SoftDeleteRepositories;
import ai.verta.modeldb.reconcilers.UpdateExperimentTimestampReconcile;
import ai.verta.modeldb.reconcilers.UpdateProjectTimestampReconcile;
import ai.verta.modeldb.reconcilers.UpdateRepositoryTimestampReconcile;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.opentelemetry.api.OpenTelemetry;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Conditional;
import org.springframework.context.annotation.Configuration;

@NoArgsConstructor
@Getter
@Configuration
public class ReconcilerInitializer {
  private static final Logger LOGGER = LogManager.getLogger(ReconcilerInitializer.class);
  @JsonProperty private SoftDeleteProjects softDeleteProjects;
  @JsonProperty private SoftDeleteExperiments softDeleteExperiments;
  @JsonProperty private SoftDeleteExperimentRuns softDeleteExperimentRuns;
  @JsonProperty private SoftDeleteRepositories softDeleteRepositories;
  @JsonProperty private SoftDeleteRepositories softDeleteDatasets;
  @JsonProperty private UpdateRepositoryTimestampReconcile updateRepositoryTimestampReconcile;
  @JsonProperty private UpdateExperimentTimestampReconcile updateExperimentTimestampReconcile;
  @JsonProperty private UpdateProjectTimestampReconcile updateProjectTimestampReconcile;

  @Bean
  @Conditional({RunLiquibaseWithMainService.class})
  public ReconcilerInitializer initialize(
      MDBConfig config,
      ServiceSet services,
      FutureExecutor executor,
      FutureJdbi futureJdbi,
      OpenTelemetry openTelemetry) {
    LOGGER.info("Enter in ReconcilerUtils: initialize()");

    ReconcilerConfig reconcilerConfig =
        ReconcilerConfig.builder().isTestReconciler(config instanceof TestConfig).build();

    softDeleteProjects =
        new SoftDeleteProjects(
            reconcilerConfig, services.getMdbRoleService(), futureJdbi, executor, openTelemetry);
    softDeleteExperiments =
        new SoftDeleteExperiments(
            reconcilerConfig, services.getMdbRoleService(), futureJdbi, executor, openTelemetry);
    softDeleteExperimentRuns =
        new SoftDeleteExperimentRuns(
            reconcilerConfig, services.getMdbRoleService(), futureJdbi, executor, openTelemetry);
    softDeleteRepositories =
        new SoftDeleteRepositories(
            reconcilerConfig,
            services.getMdbRoleService(),
            false,
            futureJdbi,
            executor,
            openTelemetry);
    softDeleteDatasets =
        new SoftDeleteRepositories(
            reconcilerConfig,
            services.getMdbRoleService(),
            true,
            futureJdbi,
            executor,
            openTelemetry);
    updateRepositoryTimestampReconcile =
        new UpdateRepositoryTimestampReconcile(
            reconcilerConfig, futureJdbi, executor, config, openTelemetry);
    updateExperimentTimestampReconcile =
        new UpdateExperimentTimestampReconcile(
            reconcilerConfig, futureJdbi, executor, openTelemetry);
    updateProjectTimestampReconcile =
        new UpdateProjectTimestampReconcile(reconcilerConfig, futureJdbi, executor, openTelemetry);

    LOGGER.info("Exit from ReconcilerUtils: initialize()");
    return this;
  }
}
